package com.gaggum

import com.google.gson.annotations.SerializedName

data class KeyCertRequestBody (
    @SerializedName("turtle_key")
    val turtleKey: String?
)

data class KeyCertResponseBody (
    @SerializedName("data")
    val data: List<turtleInfo>
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
    val diaryMemo: String,
    @SerializedName("diary_date")
    val diaryDate: String,
    @SerializedName("diary_img")
    val diaryImg: String
)


