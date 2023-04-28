package com.gaggum

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase

class MyPlantActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_my_plant)

        val database = Firebase.database
        val myRef = database.getReference("message")

        myRef.setValue("Hello World!")

    }

}