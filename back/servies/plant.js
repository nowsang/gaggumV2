const db = require("./db");
const helper = require("../helper");

async function getPlants(turtleId) {
  try {
    const rows = await db.query(`SELECT * from plants WHERE plant_isdelete=0 AND turtle_id = ${turtleId}`);
    const data = helper.emptyOrRows(rows);
    return {
      data,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function getWaterNeedPlant(turtleId) {
  try {
    const rows = await db.query(
      `SELECT * from plants WHERE turtle_id = ${turtleId} and (curdate()-plant_last_watering_date)>=plant_watering_cycle;`
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
async function getPlantById(param) {
  try {
    const rows = await db.query(
      `SELECT * from plants WHERE plant_id = ${param} AND plant_isdelete = 0`
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
      `SELECT * from plants WHERE plant_detected_name = '${param}' AND plant_isdelete = 0`
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
        WHERE plant_id = ${body.plant_id} AND plant_isdelete = 0`
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
        WHERE plant_id = ${body.plant_id} AND plant_isdelete = 0`
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
        WHERE plant_id = ${body.plant_id} AND plant_isdelete = 0`
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
      `insert into plants(turtle_id,plant_name,plant_species,plant_memo,plant_position_x,plant_position_y,plant_img,plant_watering_cycle,plant_watering_amount,plant_last_watering_date,plant_sunlight,plant_create_date,plant_detected_name,sunspot_id)
      values (${body.turtle_id},"${body.plant_name}","${body.plant_species}","${body.plant_memo}",${body.plant_position_x},${body.plant_position_y},"https://ssafybucket.s3.ap-northeast-2.amazonaws.com/image/${body.plant_detected_name}",${body.plant_watering_cycle},${body.plant_watering_amount},curdate(),${body.plant_sunlight},curdate(),"${body.plant_detected_name}",0);`
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
  getPlantById,
  waterPlant,
  getWaterNeedPlant,
  editPlant,
  deletePlant,
  createPlant,
  getPlantByOriginName,
  getSunNeedPlant,
};
