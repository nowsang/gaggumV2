const db = require("./db");
const helper = require("../helper");

async function getPlants() {
  try {
    const rows = await db.query(`SELECT * from plants WHERE plant_isdelete=0`);
    const data = helper.emptyOrRows(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function getWaterNeedPlant() {
  try {
    const rows = await db.query(
      `SELECT * from plants WHERE (curdate()-plant_last_watering_date)>=plant_watering_cycle;`
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
async function getSunNeedPlant() {
  try {
    const rows = await db.query(
      `SELECT * from plants WHERE plant_sunlight==1;`
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
async function getPlantByNumber(param) {
  try {
    const rows = await db.query(
      `SELECT * from plants WHERE plant_number = ${param} AND plant_isdelete = 0`
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
async function getPlantByOriginName(param) {
  try {
    const rows = await db.query(
      `SELECT * from plants WHERE plant_original_name = '${param}' AND plant_isdelete = 0`
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
async function waterPlant(body) {
  try {
    const rows = await db.query(
      `UPDATE plants
        SET plant_last_watering_date = now()
        WHERE plant_number = ${body.plant_number} AND plant_isdelete = 0`
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
async function editPlant(body) {
  try {
    const rows = await db.query(
      `UPDATE plants
        SET plant_name = ${body.plant_name}, plant_memo = ${body.plant_memo}, plant_watering_cycle = ${body.plant_watering_cycle}, plant_watering_amount = ${body.plant_watering_amount} 
        WHERE plant_number = ${body.plant_number} AND plant_isdelete = 0`
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
async function deletePlant(body) {
  try {
    const rows = await db.query(
      `UPDATE plants
        SET plant_isdelete = 1
        WHERE plant_number = ${body.plant_number} AND plant_isdelete = 0`
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
async function createPlant(body) {
  try {
    const rows = await db.query(
      `insert into plants(user_number,plant_name,plant_species,plant_memo,plant_position_x,plant_position_y,plant_img,plant_watering_cycle,plant_watering_amount,plant_last_watering_date,plant_sunlight,plant_create_date,plant_original_name,sunspot_number)
      values (1,"${body.plant_name}","${body.plant_species}","${body.plant_memo}",${body.plant_position_x},${body.plant_position_y},"https://ssafybucket.s3.ap-northeast-2.amazonaws.com/image/${body.plant_original_name}",${body.plant_watering_cycle},${body.plant_watering_amount},curdate(),${body.plant_sunlight},curdate(),"${body.plant_original_name}",0);`
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

module.exports = {
  getPlants,
  getPlantByNumber,
  waterPlant,
  getWaterNeedPlant,
  editPlant,
  deletePlant,
  createPlant,
  getPlantByOriginName,
  getSunNeedPlant,
};
