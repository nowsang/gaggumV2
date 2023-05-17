const db = require("./db");
const helper = require("../helper");
const config = require("../config");

async function getTurtle(page = 1) {
  try {
    const offset = helper.getOffset(page, config.listPerPage);
    const rows = await db.query(
      `SELECT * from turtles LIMIT ${offset},${config.listPerPage}`
    );
    const data = helper.emptyOrRows(rows);
    const meta = { page };

    return {
      data,
      meta,
    };
  } catch (error) {
    console.error(error);
    throw error;
  }
}
async function getTurtleByKey(body) {
  try {
    console.log(body.turtle_key);
    const rows = await db.query(
      `SELECT turtle_id from turtles WHERE turtle_key = "${body.turtle_key}"`
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
  getTurtle,
  getTurtleByKey,
};
