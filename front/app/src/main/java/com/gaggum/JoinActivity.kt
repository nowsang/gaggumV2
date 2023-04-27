package com.gaggum

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class JoinActivity : AppCompatActivity() {

    private lateinit var auth : FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_join)

        auth = Firebase.auth

        val joinBtn = findViewById<Button>(R.id.joinBtn)
        joinBtn.setOnClickListener {

            val email = findViewById<EditText>(R.id.joinEmailArea)?.text.toString()
            val password = findViewById<EditText>(R.id.joinPasswordArea)?.text.toString()

            Log.e("email", email)
            Log.e("password", password)

            if (email == "" || password == "") {
                Toast.makeText(this, "이메일과 비밀번호를 입력해주세요", Toast.LENGTH_SHORT).show()
            } else {
            auth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(this) { task ->
                    Log.e("task", task.toString())
                    if (task.isSuccessful) {
                        Toast.makeText(this, "회원가입 성공", Toast.LENGTH_LONG).show()
//                        val intent = Intent(this, KeyCertificationActivity::class.java)
                        val intent = Intent(this, MainActivity::class.java)
                        startActivity(intent)
                    } else {
                        Toast.makeText(this, "회원가입 실패", Toast.LENGTH_LONG).show()
//                        val intent = Intent(this, SigninActivity::class.java)
//                        startActivity(intent)
                    }
                }

            }


        }


    }

}