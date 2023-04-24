const express = require("express");
const router = express.Router();
const diraies = require("../servies/diary");

/* GET diaries. */
router.get("/", async function (req, res, next) {
  try {
    res.json(await diraies.getDiaries(req.query.page));
  } catch (err) {
    console.error(`Error while getting diaries `, err.message);
    next(err);
  }
});
router.get("/date", async function (req, res, next) {
  let { diaryDate } = req.query;
  try {
    res.json(await diraies.getDiariesByDate(diaryDate));
  } catch (err) {
    console.error(`Error while getting diaries by date `, err.message);
    next(err);
  }
});
router.get("/name", async function (req, res, next) {
  let { plantName } = req.query;
  try {
    res.json(await diraies.getDiariesByName(plantName));
  } catch (err) {
    console.error(`Error while getting diaries by plantName `, err.message);
    next(err);
  }
});
router.post("/edit", async function (req, res, next) {
  try {
    res.json(await diraies.editDiary(req.body));
  } catch (err) {
    console.error(`Error while edit diary`, err.message);
    next(err);
  }
});
router.post("/delete", async function (req, res, next) {
  try {
    res.json(await diraies.deleteDiary(req.body));
  } catch (err) {
    console.error(`Error while edit diary`, err.message);
    next(err);
  }
});

module.exports = router;
