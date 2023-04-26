package com.gaggum

import android.annotation.SuppressLint
import android.content.ContentProviderClient
import android.content.Intent
import android.content.pm.PackageManager
import android.location.Geocoder
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.core.app.ActivityCompat
import com.google.android.gms.location.FusedLocationProviderClient
import com.google.android.gms.location.LocationServices
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase
import java.util.Locale


class MainActivity : AppCompatActivity() {

    private lateinit var fusedLocationClient: FusedLocationProviderClient

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* 날씨 API */
        val OPEN_WEATHER_MAP_API_KEY = "be002738467412a6651e4278dd3f8c76"
        val OPEN_WEATHER_MAP_BASE_URL = "http://api.openweathermap.org/data/2.5/"

        /* 위치 권한 체크 및 요청 */



        /* 로그아웃 */
        val logoutBtn = findViewById<Button>(R.id.logoutBtn)
        logoutBtn.setOnClickListener {
            Firebase.auth.signOut()
            val intent = Intent(this, SigninActivity::class.java)
            startActivity(intent)
        }


    }

}