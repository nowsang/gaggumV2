const db = require("./db");
const helper = require("../helper");
const config = require("../config");
const plants = require("../servies/plant");
const s3 = require("../aws/s3");

async function getDiaries(turtleId) {
  try {
    const rows = await db.query(
      `select diary_id, diary_title, diary_memo, diary_img, diary_date, diary_isdelete
      from diaries d
      join plants p on d.plant_id = p.plant_id
      where p.turtle_id = ${turtleId} and d.diary_isdelete=0
      order by diary_date desc;`
    );
    const data = helper.emptyOrRows(rows);

    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function getDiariesByDate(body) {
  try {
    console.log(body);
    const rows = await db.query(
      `select diary_id, diary_title, diary_memo, diary_img, diary_date, diary_isdelete
      from diaries d
      join plants p on d.plant_id = p.plant_id
      where p.turtle_id = ${body.turtle_id} and d.diary_isdelete=0 and d.diary_date
      order by diary_date desc;`
    );
    const data = helper.emptyOrRows(rows);
    console.log(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function getDiariesByName(param) {
  try {
    console.log(param);
    const rows = await db.query(
      `select * from
      diaries d join plants p ON d.plant_number = p.plant_number
      WHERE p.turtle_id = ${body.turtle_id} AND p.plant_name LIKE "${body.plant_name}%" AND diary_isdelete = 0 ORDER BY diary_date DESC`
    );
    const data = helper.emptyOrRows(rows);
    console.log(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function editDiary(body) {
  try {
    const rows = await db.query(
      `UPDATE diaries
        SET diary_title = "${body.diary_title}", diary_memo = "${body.diary_memo}"
        WHERE diary_id = ${body.diary_id}`
    );
    const data = helper.emptyOrRows(rows);
    console.log(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function deleteDiary(body) {
  try {
    const rows = await db.query(
      `UPDATE diaries
        SET diary_isdelete = 1
        WHERE diary_id = ${body.diary_id}`
    );
    const data = helper.emptyOrRows(rows);
    console.log(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function createDiary(body) {
  try {
    var now = new Date();
    var ndate = now.getDate();
    var nmonth = now.getMonth() + 1;
    const plantData = await plants.getPlantByOriginName(
      body.plant_original_name
    );
    console.log("plantData", plantData);
    //await plants.waterPlant(plantData.data[0]);
    const rows = await db.query(
      `INSERT INTO diaries(plant_id, diary_title, diary_img, diary_memo, diary_date)
      values (${plantData.data[0].plant_id},"${plantData.data[0].plant_name} ${nmonth}월 ${ndate}일","https://ssafybucket.s3.ap-northeast-2.amazonaws.com/image/diary/${plantData.data[0].plant_id}/${nmonth}월${ndate}일","${plantData.data[0].plant_name} 물주기",curdate());
      `
    );
    const data = helper.emptyOrRows(rows);
    console.log(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function createDiaryByUser(body) {
  try {
    var now = new Date();
    var ndate = now.getDate();
    var nmonth = now.getMonth() + 1;
    s3.uploadDiaryFile(body.plant_id, body.diary_img);
    const rows = await db.query(
      `INSERT INTO diaries(plant_id, diary_title, diary_img, diary_memo, diary_date)
      values (${body.plant_id},"${body.diary_title}","https://ssafybucket.s3.ap-northeast-2.amazonaws.com/image/diary/${body.plant_id}/${nmonth}월${ndate}일","${body.diary_memo}",curdate());
      `
    );
    const data = helper.emptyOrRows(rows);
    console.log(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
module.exports = {
  getDiaries,
  getDiariesByDate,
  getDiariesByName,
  editDiary,
  deleteDiary,
  createDiary,
  createDiaryByUser,
};
