package com.gaggum

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class SplashActivity : AppCompatActivity() {

    private lateinit var auth : FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        auth = Firebase.auth

        Log.e("사용자", auth.currentUser?.uid.toString())

        if (auth.currentUser?.uid == null) {
            Toast.makeText(this, "로그인 실패", Toast.LENGTH_LONG).show()
            Handler().postDelayed({
                startActivity(Intent(this, SigninActivity::class.java))
                finish()
            }, 2000)
        } else {
            Toast.makeText(this, "로그인 성공", Toast.LENGTH_LONG).show()
            Handler().postDelayed({
                startActivity(Intent(this, KeyCertificationActivity::class.java))
                finish()
            }, 2000)
        }

    }

}