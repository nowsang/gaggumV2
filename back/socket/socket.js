const express = require("express");
const app = express();
const plants = require("../servies/plant");
const diaries = require("../servies/diary");
const s3 = require("../aws/s3");
// 로직 1. WebSocket 서버, WebClient 통신 규약 정의
// const server = require("http").createServer(app);
const server = require("http").createServer(app);

// const io = require("socket.io")(server)
const io = require("socket.io")(server, {
  cors: {
    origin: [
      "http://k8b101.p.ssafy.io:3001",
      "http://k8b101.p.ssafy.io",
      "http://localhost:8080",
      "http://localhost:3001",
      "http://localhost:3000",
      "http://192.168.1.72:3000",
      "http://192.168.1.72:8080",
    ],
    methods: ["GET", "POST"],
    transports: ["websocket", "polling"],
    credentials: true,
  },
});

// 로직 2. 포트번호 지정
function socketStart() {
  const port1 = process.env.port || 3001;

  server.listen(port1, () => {
    console.log(`listening on *:${port1}`);
  });

  // 터틀봇의 소켓 이름.
  const roomName = "team";
  

  io.on("connection", (socket) => {
    socket.join(roomName);

    console.log("connected from server");

    socket.on("run_motor", (data) => {
      console.log("run_motor", data.mode);      
      // motor control  (pot, watering)
      if (data.mode == 'motor_status') {
        socket.to(roomName).emit("run_motor", data);
        console.log("motor_status", data);
      }

      // motor watering_end -> {{mode : "water_end"}, {plant : plant1}}
      else if (data.mode == "water_end") {
        socket.emit("run_motor", data);
        // -1 or plant1 or both
        console.log("water_end", data.plant)
      }     
      
    })

    // Map Auto Scan
    socket.on("run_walltracking", (data) => {
      // Front -> Back -> ROS
      socket.to(roomName).emit("run_walltracking", data);
      console.log("run_walltracking", data);

      if (data == -1) {
        console.log("맵 종료 됨");
        socket.emit("run_walltracking", data);
      }
    });

    // 시뮬레이터 환경변수(시간, 날씨), 로봇 위치 정보 전달(백 -> ROS)
    socket.on("time_control", (data) => {
      console.log("time_control", data.hour);      
      // 프론트 페이지로 simulator 전달
      // socket.to(roomName).emit("simulator_info", data);
      

      //현재 시간이 물주는 시간인지 체크
      if (data.hour == 13) {
        (async () => {
          // db에서 물줘야하는 식물 리스트 가져오기
          let turtle_id = 1;
          let waterNeedPlants = await plants.getWaterNeedPlant(turtle_id);
          console.log("물줘야하는 식물들", waterNeedPlants);
          waterNeedPlants.mode = 100;
          // ROS로 급수 필요 식물 리스트 전달
          socket.to(roomName).emit("auto_move", waterNeedPlants);
        })();
      } else if (data.hour == 15) {
        (async () => {
          // db에서 햇빛이 필요한 식물과 햇빛 위치를 가져오기
          let sunNeedPlants = await plants.getSunNeedPlant();
          let sunSpots = await plants.getSunSpot();
          console.log("햇빛 필요 식물들", sunNeedPlants);
          sunNeedPlants.mode = 200;
          sunNeedPlants.sunSpots = sunSpots.data;
          // ROS로 햇빛 필요 식물 리스트 전달
          socket.to(roomName).emit("auto_move", sunNeedPlants);
        })();
      }
    });

    // 물 주는 동작 완료()
    // plant_original_name, plant_img 두가지를 들고있는 객체들의 리스트를 data에 넣어주세요
    socket.on("diary_regist", (data) => {
      console.log("diary_regist_plants", data);
      s3.uploadDiaryFile(data.plant_original_name, data.plant_img);
      diaries.createDiary(data);

      // for (let i = 0; i < data.length(); i++) {
      //   s3.uploadDiaryFile(
      //     data[i].plant_original_name,
      //     data[i].plant_img
      //   );
      //   diaries.createDiary(data[i]);
      // }
    });

    // 카메라
    socket.on("streaming_image", (data) => {
      console.log("streaming_image", data);
      //ROs -> Front로 전달
      socket.to(roomName).emit("streaming_image", data);

      // front에서 들어오는 data -> ROS로 전달 (이 페이지의 목적 : ROS에서 계속 Back으로 emit 요청하는 것을 막기위해 flag 조절하려고)
      if (data == "front") {
        socket.to(roomName).emit("streaming_image", data);
      }
    });


    // 터틀봇 수동조작 파트 앞, 뒤, 오른쪽, 왼쪽
    socket.on("manual_control", (data) => {
      console.log("manual_control", data.data)
      socket.to(roomName).emit("manual_control", data.data);
    })

    // 터틀봇 수동조작 파트 앞, 뒤, 오른쪽, 왼쪽
    socket.on("go_straight", (data) => {
      socket.to(roomName).emit("go_straight", data);
      console.log("앞");
    });

    socket.on("go_back", (data) => {
      socket.to(roomName).emit("go_back", data);
      console.log("뒤");
    });

    socket.on("go_left", (data) => {
      socket.to(roomName).emit("go_left", data);
      console.log("왼쪽");
    });

    socket.on("go_right", (data) => {
      socket.to(roomName).emit("go_right", data);
      console.log("오른쪽");
    });

    socket.on("disconnect", () => {
      console.log("disconnected from server");
    });

    // // 전달받은 이미지를 jpg 파일로 저장
    // socket.on('streaming', (message) => {
    //     socket.to(roomName).emit('sendStreaming', message);
    //     // console.log(message);
    //     buffer = Buffer.from(message, "base64");
    //     fs.writeFileSync(path.join(picPath, "/../client/cam.jpg"), buffer);
    // });
  });
}

module.exports = {
  socketStart,
};
