package com.gaggum

import com.google.gson.annotations.SerializedName
//import com.tickaroo.tikxml.annotation.Element
import com.tickaroo.tikxml.annotation.PropertyElement
import com.tickaroo.tikxml.annotation.Xml
import org.simpleframework.xml.Element
import org.simpleframework.xml.ElementArray
import org.simpleframework.xml.ElementList
import org.simpleframework.xml.ElementMap
import org.simpleframework.xml.Root
import org.simpleframework.xml.Text


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

)data class EditDiaryResponseData(
    val info: String,

    )
data class createDiaryRequestBody (
    @SerializedName("plant_id")
    val plantId: Int?,
    @SerializedName("diary_title")
    val diaryTitle: String?,
    @SerializedName("diary_memo")
    val diaryMemo: String?,
    @SerializedName("diary_img")
    val diaryImg: String?,
)
data class createDiaryResponseBody (
    @SerializedName("data")
    val data:EditDiaryResponseData
)
data class deleteDiaryRequestBody (
    @SerializedName("diary_id")
    val diaryId: Int?,
)
data class deleteDiaryResponseBody (
    @SerializedName("data")
    val data:EditDiaryResponseData
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


@Root(name = "document", strict = false)
data class FlowerResponseBody @JvmOverloads constructor(
    @field:Element(name = "root")
    var root : flowerRoot? = null
) {
    @Root(name = "root", strict = false)
    data class flowerRoot @JvmOverloads constructor(
        @field:Element(name = "resultCode")
        var resultCode: Int? = null,

        @field:Element(name = "resultMsg")
        var resultMsg: String? = null,

        @field:Element(name = "repcategory")
        var repcategory: String? = null,

        @field:ElementList(name = "result", required = false, inline = true)
        var result: ArrayList<flowerResult>? = null
    )

    @Root(name = "result", strict = false)
    data class flowerResult @JvmOverloads constructor(
        @field:Element(name = "dataNo", required = false)
        var dataNo: Int? = null,

        @field:Element(name = "fMonth", required = false)
        var fMonth: Int? = null,

        @field:Element(name = "fDay", required = false)
        var fDay: Int? = null,

        @field:Element(name = "flowNm", required = false)
        var flowNm: String? = null,

        @field:Element(name = "fSctNm", required = false)
        var fSctNm: String? = null,

        @field:Element(name = "fEngNm", required = false)
        var fEngNm: String? = null,

        @field:Element(name = "flowLang", required = false)
        var flowLang: String? = null,

        @field:Element(name = "fContent", required = false)
        var fContent: String? = null,

        @field:Element(name = "fUse", required = false)
        var fUse: String? = null,

        @field:Element(name = "fGrow", required = false)
        var fGrow: String? = null,

        @field:Element(name = "fType", required = false)
        var fType: String? = null,

        @field:Element(name = "fileName1", required = false)
        var fileName1: String? = null,

        @field:Element(name = "fileName2", required = false)
        var fileName2: String? = null,

        @field:Element(name = "fileName3", required = false)
        var fileName3: String? = null,

        @field:Element(name = "imgUrl1", required = false)
        var imgUrl1: String? = null,

        @field:Element(name = "imgUrl2", required = false)
        var imgUrl2: String? = null,

        @field:Element(name = "imgUrl3", required = false)
        var imgUrl3: String? = null,

        @field:Element(name = "publishOrg", required = false)
        var publishOrg: String? = null,

    )
}


data class NeedWaterResponseBody(
    @SerializedName("data") var data : ArrayList<allPlants>
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

data class UpdateWateringDateRequestBody (
    @SerializedName("plant_id") val plantId : Int
)


