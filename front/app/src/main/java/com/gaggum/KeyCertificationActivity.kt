package com.gaggum

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.Settings.Global
import android.telecom.Call
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.room.Room
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

import retrofit2.Response


class KeyCertificationActivity : AppCompatActivity() {

    private lateinit var db : ClientDatabase
    val user = Firebase.auth.currentUser!!.uid

    private fun isAlreadyCert() {
        GlobalScope.launch(Dispatchers.IO) {
            Log.e("지금 유저", user)
            val retrievedUser = db.clientDao().getTurtleId(user)
            withContext(Dispatchers.Main) {
                if (retrievedUser!!.turtleId != null) {
                    val intent = Intent(baseContext, MainActivity::class.java)
                    intent.putExtra("turtleId", retrievedUser.turtleId)
                    startActivity(intent)
                }
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_key_certification)

        db = Room.databaseBuilder(applicationContext, ClientDatabase::class.java, "ClientDatabase")
            .fallbackToDestructiveMigration()
            .build()

        isAlreadyCert()

        val keyCertBtn = findViewById<Button>(R.id.keyCertBtn)
        keyCertBtn.setOnClickListener {

            val turtlebotKey = findViewById<EditText>(R.id.keyCertInputArea).text.toString()

            Log.e("터틀봇 키", turtlebotKey)

            val service = RetrofitObject.service
            service
                .checkTurtleKey(KeyCertRequestBody(turtlebotKey))
                .enqueue(object : retrofit2.Callback<KeyCertResponseBody> {
                    override fun onResponse(
                        call: retrofit2.Call<KeyCertResponseBody>,
                        response: Response<KeyCertResponseBody>
                    ) {

                        Log.e("결과", response.toString())
                        if (response.isSuccessful) {
                            val result = response.body()!!.data.size
                            val turtleKey = response.body()!!.data[0].turtleId
                            if (result > 0) {
                                val currUser = Client(0, user, turtleKey)
                                GlobalScope.launch(Dispatchers.IO) {
                                    db.clientDao().insert(currUser)
                                }
                                Log.e("currentUser", currUser.toString())
                                Toast.makeText(baseContext, "터틀봇이 확인되었습니다.", Toast.LENGTH_SHORT).show()
                                val intent = Intent(baseContext, MainActivity::class.java)
                                startActivity(intent)
                            } else {
                                Toast.makeText(baseContext, "터틀봇 인증에 실패하였습니다.", Toast.LENGTH_SHORT).show()
                            }
                        } else {
                            Toast.makeText(baseContext, "터틀봇 인증에 실패하였습니다.", Toast.LENGTH_SHORT).show()
                        }
                    }
                    override fun onFailure(call: retrofit2.Call<KeyCertResponseBody>, t: Throwable) {
                        Toast.makeText(baseContext, "터틀봇 인증 실패", Toast.LENGTH_SHORT).show()
                    }
                })

        }

    }

}