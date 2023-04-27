package com.gaggum

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.telecom.Call
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import com.google.gson.annotations.SerializedName
import retrofit2.Response
import retrofit2.http.POST

class KeyCertificationActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_key_certification)

//        data class KeyData (
//            @SerializedName("turtle_id")
//            val turtleId: Int,
//
//            @SerializedName("turtle_key")
//            val turtleKey: String
//        )


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
                            var result = response.body()!!.data.size
                            if (result > 0) {
                                result = response.body()!!.data[0].turtleId
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