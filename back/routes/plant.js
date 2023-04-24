const express = require("express");
const router = express.Router();
const plants = require("../servies/plant");
const s3 = require("../aws/s3");

/* GET plant. */
router.get("/", async function (req, res, next) {
  try {
    res.json(await plants.getPlants(req.query.page));
  } catch (err) {
    console.error(`Error while getting plant `, err.message);
    next(err);
  }
});

router.get("/needwater", async function (req, res, next) {
  try {
    res.json(await plants.getWaterNeedPlant(req.query.page));
  } catch (err) {
    console.error(`Error while getting plant `, err.message);
    next(err);
  }
});

router.get("/number", async function (req, res, next) {
  let { plantNumber } = req.query;
  try {
    res.json(await plants.getPlants(plantNumber));
  } catch (err) {
    console.error(`Error while getting plant by number `, err.message);
    next(err);
  }
});

router.post("/water", async function (req, res, next) {
  try {
    res.json(await plants.waterPlant(req.body));
  } catch (err) {
    console.error(`Error while watering plant`, err.message);
    next(err);
  }
});

router.post("/edit", async function (req, res, next) {
  try {
    res.json(await plants.editPlant(req.body));
  } catch (err) {
    console.error(`Error while watering plant`, err.message);
    next(err);
  }
});

router.post("/delete", async function (req, res, next) {
  try {
    res.json(await plants.deletePlant(req.body));
  } catch (err) {
    console.error(`Error while watering plant`, err.message);
    next(err);
  }
});

router.post("/create", async function (req, res, next) {
  try {
    s3.uploadFile(req.body.plant_original_name,req.body.plant_img);
    res.json(await plants.createPlant(req.body));
  } catch (err) {
    
    console.error(`Error while watering plant`, err.message);
    next(err);
  }
});

module.exports = router;
