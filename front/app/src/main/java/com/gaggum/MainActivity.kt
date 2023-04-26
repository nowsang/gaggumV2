package com.gaggum

import android.content.Context
import android.location.LocationListener
import android.location.LocationManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.gson.JsonObject
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Query

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* 날씨 API */
        val OPEN_WEATHER_MAP_API_KEY = "be002738467412a6651e4278dd3f8c76"
        val OPEN_WEATHER_MAP_BASE_URL = "http://api.openweathermap.org/data/2.5/"


    }

}