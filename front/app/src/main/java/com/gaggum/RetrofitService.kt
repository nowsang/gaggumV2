package com.gaggum

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.Headers
import retrofit2.http.POST

interface RetrofitService {
    @Headers("Content-Type: application/json")
    @POST("api/turtle")
    fun checkTurtleKey(@Body turtle_key : KeyCertRequestBody) : Call<KeyCertResponseBody>

}