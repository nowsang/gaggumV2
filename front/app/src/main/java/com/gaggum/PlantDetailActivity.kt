package com.gaggum

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.gaggum.databinding.ActivityPlantDetailBinding

class PlantDetailActivity : AppCompatActivity() {

    private lateinit var binding : ActivityPlantDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPlantDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var plantId = intent.getIntExtra("plantId", 0)
        getPlantDetail(plantId)
    }

    fun getPlantDetail(plantId : Int) {

    }
}