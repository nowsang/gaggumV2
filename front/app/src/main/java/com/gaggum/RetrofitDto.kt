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
