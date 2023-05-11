const fs = require("fs");
const AWS = require("aws-sdk");
const dotenv = require("dotenv");
const config = require("../config");

dotenv.config();
const location = "ap-northeast-2";
const s3 = new AWS.S3({
  accessKeyId: config.awsKey.accessKey,
  secretAccessKey: config.awsKey.secretAccessKey,
});

const uploadFile = (name, base64) => {
  //const base64Data = new Buffer.from(imgfile.re)
  const base64Data = new Buffer.from(base64, "base64");
  const params = {
    Bucket: "ssafybucket",
    Key: "image/" + name,
    Body: base64Data,
    ContentType: `image/png`,
  };

  s3.upload(params, function (err, data) {
    if (err) {
      throw err;
    }
    console.log(`File uploaded successfully. ${data}`);
  });
};
const uploadDiaryFile = (name, base64) => {
  //const base64Data = new Buffer.from(imgfile.re)
  var now = new Date();
  var ndate = now.getDate();
  var nmonth = now.getMonth() + 1;

  console.log("uploadDiaryFile", name, base64);
  const base64Data = new Buffer.from(base64, "base64");
  const params = {
    Bucket: "ssafybucket",
    Key: "image/diary/" + name + "/" + nmonth + "월" + ndate + "일",
    Body: base64Data,
    ContentType: `image/png`,
  };

  s3.upload(params, function (err, data) {
    if (err) {
      throw err;
    }
    console.log(`File uploaded successfully. ${data}`);
  });
};
const uploadUserDiaryFile = (name,time, base64) => {
  //const base64Data = new Buffer.from(imgfile.re)
  console.log("uploadDiaryFile", name, base64);
  const base64Data = new Buffer.from(base64, "base64");
  const params = {
    Bucket: "ssafybucket",
    Key: "image/diary/" + name + "/" + time,
    Body: base64Data,
    ContentType: `image/png`,
  };

  s3.upload(params, function (err, data) {
    if (err) {
      throw err;
    }
    console.log(`File uploaded successfully. ${data}`);
  });
};

module.exports = {
  uploadFile,
  uploadDiaryFile,
  uploadUserDiaryFile,
};
