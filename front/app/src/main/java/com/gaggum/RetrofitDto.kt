package com.gaggum

import com.google.gson.annotations.SerializedName
import com.tickaroo.tikxml.annotation.Element
import com.tickaroo.tikxml.annotation.PropertyElement
import com.tickaroo.tikxml.annotation.Xml
import java.time.format.DateTimeFormatter
import java.util.Date
import java.util.Objects

data class KeyCertRequestBody (
    @SerializedName("turtle_key")
    val turtleKey: String?
)

data class KeyCertResponseBody (
    @SerializedName("data")
    val data: ArrayList<turtleInfo>
)

data class turtleInfo (
    @SerializedName("turtle_id")
    val turtleId: Int
)

data class GetAllDiariesResponseBody(
    @SerializedName("data")
    val data: List<diaryInfo>
)

data class editDiaryRequestBody (
    @SerializedName("diary_id")
    val diaryId: Int?,
    @SerializedName("diary_title")
    val diaryTitle: String?,
    @SerializedName("diary_memo")
    val diaryMemo: String?,
)

data class editDiaryResponseBody (
    @SerializedName("data")
    val data:EditDiaryResponseData
)

data class EditDiaryResponseData(
    val info: String,

)
data class diaryInfo (
    @SerializedName("diary_title")
    val diaryTitle: String,
    @SerializedName("diary_memo")
    val diaryMemo: String,
    @SerializedName("diary_date")
    val diaryDate: String,
    @SerializedName("diary_img")
    val diaryImg: String,
    @SerializedName("diary_id")
    val diaryId: Int
)

data class WeatherResponseBody(
    @SerializedName("weather") var weather : ArrayList<Weather>,
    @SerializedName("main") var main : weatherMain,
)

data class Weather(
    @SerializedName("id") var id : Int,
    @SerializedName("main") var main : String?,
    @SerializedName("description") var description : String?,
    @SerializedName("icon") var icon : String?
)

data class weatherMain(
    @SerializedName("temp") var temp : Double,
    @SerializedName("temp_min") var minTemp : Double,
    @SerializedName("temp_max") var maxTemp : Double
)


@Xml(name = "document")
data class FlowerResponseBody(
    @Element(name = "root") val root : flowerRoot?
)

@Xml(name = "root")
data class flowerRoot(
    @PropertyElement(name = "resultCode") var resultCode: Int?,
    @PropertyElement(name = "resultMsg") var resultMsg: String?,
    @PropertyElement(name = "repcategory") var repcategory: String?,
    @Element(name = "result") var result: flowerResult?
)

@Xml(name = "result")
data class flowerResult(
    @PropertyElement(name = "dataNo") var dataNo: String?,
    @PropertyElement(name = "fMonth") var fMonth: Int?,
    @PropertyElement(name = "fDay") var fDay: Int?,
    @PropertyElement(name = "flowNm") var flowNm: String?,
    @PropertyElement(name = "flowLang") var flowLang: String?,
    @PropertyElement(name = "imgUrl1") var imgUrl1: String?,

)

data class NeedWaterResponseBody(
    @SerializedName("data") var data : ArrayList<String>
)

data class GetAllPlantsResponseBody(
    @SerializedName("data") var data : ArrayList<allPlants>
)

data class allPlants (
    @SerializedName("plant_id") var plantId : Int,
    @SerializedName("turtle_id") var turtleId : Int,
    @SerializedName("plant_name") var plantName : String,
    @SerializedName("plant_species") var plantSpecies : String,
    @SerializedName("plant_img") var plantImg : String
)

data class GetPlantDetailResponseBody (
    @SerializedName("data") var data : ArrayList<plantDetailData>
)

data class plantDetailData (
    @SerializedName("plant_id") var plantId : Int,
    @SerializedName("turtle_id") var turtleId: Int,
    @SerializedName("plant_name") var plantName : String,
    @SerializedName("plant_species") var plantSpecies: String,
    @SerializedName("plant_memo") var plantMemo : String,
    @SerializedName("plant_img") var plantImg : String,
    @SerializedName("plant_isdelete") var plantIsDelete : Int,
    @SerializedName("plant_create_date") var plantCreateDate : String,
    @SerializedName("plant_position_x") var plantPositionX : Double,
    @SerializedName("plant_position_y") var plantPositionY : Double,
    @SerializedName("plant_watering_cycle") var plantWateringCycle : Int,
    @SerializedName("plant_watering_amount") var plantWateringAmount : Int,
    @SerializedName("plant_last_watering_date") var plantLastWateringDate : String,
    @SerializedName("plant_sunlight") var plantSunlight : Int,
    @SerializedName("plant_detected_name") var plantDetectedName : String

)


