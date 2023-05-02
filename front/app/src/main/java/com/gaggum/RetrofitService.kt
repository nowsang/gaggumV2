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

    @Headers("Content-Type:application/json")
    @GET("data/2.5/weather")
    fun getWeatherData(
        @Query("lat") lat: String,
        @Query("lon") lon: String,
        @Query("appid") appid: String
    ) : Call<WeatherResponseBody>


}