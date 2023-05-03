package com.gaggum

import retrofit2.Call
import retrofit2.http.*
import java.time.LocalDate
import java.util.Calendar

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


    @Headers("Content-Type:application/xml; charset=utf-8")
    @GET("NihhsTodayFlowerInfo01/selectTodayFlower01")
    fun getFlowerData(
        @Query("serviceKey") serviceKey: String,
        @Query("fMonth") fMonth: Int,
        @Query("fDay") fDay: Int,
    ) : Call<FlowerResponseBody>

    @Headers("Content-Type:application/json")
    @GET("api/plant/needwater")
    fun getNeedWaterList(
        @Query("turtleId") turtleId: Int
    ) : Call<NeedWaterResponseBody>

    @Headers("Content-Type:application/json")
    @GET("api/plant/allplants")
    fun getAllPlantsData(
        @Query("turtleId") turtleId: Int
    ) : Call<GetAllPlantsResponseBody>


}