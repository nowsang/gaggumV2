const express = require("express");
const router = express.Router();
const s3 = require("../aws/s3");
const turtles = require("../servies/turtle");

/* GET turtle. */
router.get("/", async function (req, res, next) {
  try {
    res.json(await turtles.getTurtle(req.query.page));
  } catch (err) {
    console.error(`Error while getting turtle `, err.message);
    next(err);
  }
});
router.post("/", async function (req, res, next) {
  try {
    res.json(await turtles.getTurtleByKey(req.body));
  } catch (err) {
    console.error(`Error while getting turtle `, err.message);
    next(err);
  }
});

module.exports = router;
