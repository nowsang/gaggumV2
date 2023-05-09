package com.gaggum

import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AlertDialog
import com.bumptech.glide.Glide
import com.gaggum.databinding.ActivityPlantDetailBinding
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.text.SimpleDateFormat
import java.time.format.DateTimeFormatter
import java.util.Calendar
import java.util.Date
import java.time.LocalDate
import java.time.Period
import android.content.DialogInterface
import android.content.Intent
import android.widget.Toast

class PlantDetailActivity : AppCompatActivity() {

    private lateinit var binding : ActivityPlantDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPlantDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var plantId = intent.getIntExtra("plantId", 0)
        getPlantDetail(plantId)

        binding.plantDetailBtn.setOnClickListener {
            showingDialog(plantId)
        }
    }

    fun showingDialog(plantId : Int) {
        val alertDialogBuilder = AlertDialog.Builder(this)
        alertDialogBuilder.setTitle("급수 최신화")
        alertDialogBuilder.setMessage("급수일을 최신화 하시겠습니까?")

        alertDialogBuilder.setPositiveButton("확인") { dialog, _ ->
            val service = RetrofitObject.service
            service
                .updateWateringDate(UpdateWateringDateRequestBody(plantId))
                .enqueue(object : Callback<Any> {
                    override fun onResponse(call: Call<Any>, response: Response<Any>) {
                        Toast.makeText(baseContext, "급수 최신화가 완료되었습니다.", Toast.LENGTH_SHORT).show()
                        getPlantDetail(plantId)
                        dialog.dismiss()
                    }

                    override fun onFailure(call: Call<Any>, t: Throwable) {
                        Toast.makeText(baseContext, "급수 최신화에 실패하였습니다.", Toast.LENGTH_SHORT).show()
                    }

                })
        }

        alertDialogBuilder.setNegativeButton("취소") { dialog, _ ->
            dialog.dismiss()
        }

        val alertDialog = alertDialogBuilder.create()
        alertDialog.show()

    }

    fun getPlantDetail(plantId : Int) {
        val service = RetrofitObject.service
        service
            .getPlantDetailData(plantId)
            .enqueue(object : Callback<GetPlantDetailResponseBody> {
                @RequiresApi(Build.VERSION_CODES.O)
                override fun onResponse(
                    call: Call<GetPlantDetailResponseBody>,
                    response: Response<GetPlantDetailResponseBody>,
                ) {
                    if (response.isSuccessful) {
                        val res = response.body()!!.data[0]

                        val today = LocalDate.now()
                        val targetDate = LocalDate.of(2023, 5, 1)

                        val period = Period.between(targetDate, today)
                        val daysPassed = period.days + (period.months * 30) + (period.years * 365)

                        Log.e("날짜", res.plantCreateDate)

                        Glide
                            .with(baseContext)
                            .load(res.plantImg)
                            .into(binding.plantDetailImg)

                        if (res.plantSunlight == 1) {
                            binding.plantDetailSunlight.setImageResource(R.drawable.sun_1)
                        } else {
                            binding.plantDetailSunlight.setImageResource(R.drawable.sun_0)
                        }

                        binding.plantDetailName.text = res.plantName
                        binding.plantDetailSpecies.text = res.plantSpecies
                        binding.plantDetailMemo.text = res.plantMemo
                        binding.plantDetailWateringCycle.text = "${res.plantWateringCycle}일"
                        binding.plantDetailWateringAmount.text = "${res.plantWateringAmount}ML"
                        binding.plantDetailWateringDay.text = res.plantLastWateringDate.slice(2..9)
                        binding.plantDetailDday.text = "함께한지 ${daysPassed}일이 지났어요"

                    }
                }

                override fun onFailure(call: Call<GetPlantDetailResponseBody>, t: Throwable) {
                    Log.e("실패", t.toString())
                }

            })
    }
}

