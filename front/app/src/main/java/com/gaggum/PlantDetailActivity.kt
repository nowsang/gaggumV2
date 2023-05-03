package com.gaggum

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import com.gaggum.databinding.ActivityPlantDetailBinding
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.text.SimpleDateFormat
import java.time.format.DateTimeFormatter
import java.util.Calendar
import java.util.Date

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
        val service = RetrofitObject.service
        service
            .getPlantDetailData(plantId)
            .enqueue(object : Callback<GetPlantDetailResponseBody> {
                override fun onResponse(
                    call: Call<GetPlantDetailResponseBody>,
                    response: Response<GetPlantDetailResponseBody>,
                ) {
                    if (response.isSuccessful) {
                        val res = response.body()!!.data[0]

                        val today = Calendar.getInstance()

                        val startDate = res.plantCreateDate.slice(2..9) + " " + res.plantCreateDate.slice(11..18)
                        val sf = SimpleDateFormat("yyyy-MM-dd 00:00:00")
                        val date = sf.parse(startDate)
                        val calcDate = (today.time.time - date.time) / (60 * 60 * 24 * 1000)
                        Log.e("today", today.toString())
                        Log.e("date", date.toString())
                        Log.e("calcdate", calcDate.toString())
                        Log.e("today.time.time", today.time.time.toString())
                        Log.e("date.time", date.time.toString())
                        Log.e("날짜", res.plantCreateDate)

                        binding.plantDetailName.text = res.plantName
                        binding.plantDetailSpecies.text = res.plantSpecies
                        binding.plantDetailMemo.text = res.plantMemo
                        binding.plantDetailWateringCycle.text = "${res.plantWateringCycle}일"
                        binding.plantDetailWateringAmount.text = "${res.plantWateringAmount}ML"
                        binding.plantDetailWateringDay.text = res.plantLastWateringDate.slice(2..9)
                        binding.plantDetailDday.text = "$calcDate"

                    }
                }

                override fun onFailure(call: Call<GetPlantDetailResponseBody>, t: Throwable) {
                    Log.e("실패", t.toString())
                }

            })
    }
}