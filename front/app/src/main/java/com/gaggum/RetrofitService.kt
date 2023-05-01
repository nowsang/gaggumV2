package com.gaggum

import retrofit2.Call
import retrofit2.http.*

interface RetrofitService {
    @Headers("Content-Type:application/json")
    @POST("api/turtle")
    fun checkTurtleKey(@Body turtle_key : KeyCertRequestBody) : Call<KeyCertResponseBody>

    @Headers("Content-Type:application/json")
    @GET("api/diary")
    fun getAllDiary(@Query("turtleId") turtleId: Int  ) : Call<GetAllDiariesResponseBody>

}