package com.gaggum

import com.google.gson.annotations.SerializedName

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

data class diaryInfo (
    @SerializedName("diary_title")
    val diaryTitle: String,
    @SerializedName("diary_memo")
    val diaryMemo: String
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
