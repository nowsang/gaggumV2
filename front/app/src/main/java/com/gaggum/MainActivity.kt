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
import androidx.navigation.NavController
import com.google.android.gms.location.FusedLocationProviderClient
import com.google.android.gms.location.LocationServices
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase
import java.util.Locale
//socket
import io.socket.client.IO
import io.socket.client.Socket
import io.socket.emitter.Emitter
import java.net.URISyntaxException
//nav
import androidx.navigation.Navigation
import androidx.navigation.fragment.NavHostFragment
import androidx.navigation.ui.setupWithNavController
import com.google.android.material.bottomnavigation.BottomNavigationView
import androidx.navigation.ui.onNavDestinationSelected

class MainActivity : AppCompatActivity() {
    //    private lateinit var socket: Socket
    private lateinit var fusedLocationClient: FusedLocationProviderClient
    lateinit var mSocket : Socket
    private lateinit var navController: NavController

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Set up navigation
        val navHostFragment = supportFragmentManager.findFragmentById(R.id.nav_host_fragment) as NavHostFragment
        navController = navHostFragment.navController
        val bottomNavigationView = findViewById<BottomNavigationView>(R.id.bottomNavigationView)
        bottomNavigationView.setupWithNavController(navController)

        // Socket.io
        try {
            //핸드폰 유선 연결 시 1.핸드폰이랑 노트북 같은 와이파이 쓸 것 2.IPv4 주소를 아래 주소에 입력
            mSocket = IO.socket("http://192.168.217.177:3000")
            mSocket.connect()
            Log.d("Connected", "OK")
        } catch (e: URISyntaxException) {
            Log.d("ERR", e.toString())
        }
        mSocket.on(Socket.EVENT_CONNECT, onConnect)



        /* 위치 권한 체크 및 요청 */


    }

    val onConnect = Emitter.Listener {
        mSocket.emit("connectReceive","OK")
    }
}
