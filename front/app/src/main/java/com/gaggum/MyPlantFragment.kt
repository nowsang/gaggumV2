package com.gaggum

import android.content.Context
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.LinearLayoutManager
import com.gaggum.databinding.FragmentMyPlantBinding
import retrofit2.Call
import retrofit2.Response
import retrofit2.Callback
import java.util.Objects


class MyPlantFragment : Fragment() {

    private lateinit var mainActivity : MainActivity
    private lateinit var allPlantsList : ArrayList<allPlants>
    private lateinit var myPlantRVAdapter: MyPlantRVAdapter

    override fun onAttach(context: Context) {
        super.onAttach(context)
        mainActivity = context as MainActivity
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        // Inflate the layout for this fragment
        val binding = FragmentMyPlantBinding.inflate(inflater, container, false)
        getAllPlants()

        val plantRV = binding.myPlantRV
        myPlantRVAdapter = MyPlantRVAdapter(mainActivity)
        plantRV.adapter = myPlantRVAdapter
        plantRV.layoutManager = LinearLayoutManager(mainActivity)


        return binding.root
    }

    fun getAllPlants() {
        val service = RetrofitObject.service
        service
            .getAllPlantsData(1)
            .enqueue(object : Callback<GetAllPlantsResponseBody> {
                override fun onResponse(
                    call: Call<GetAllPlantsResponseBody>,
                    response: Response<GetAllPlantsResponseBody>
                ) {
                    if (response.isSuccessful) {
                        Log.e("성공", response.body()!!.toString())
                        allPlantsList = response.body()!!.data
                        myPlantRVAdapter.plants = allPlantsList
                        Log.e("식물리스트", allPlantsList.toString())
                        myPlantRVAdapter.notifyDataSetChanged()
                    }
                }

                override fun onFailure(call: Call<GetAllPlantsResponseBody>, t: Throwable) {
                    Log.e("실패", t.toString())
                }

            })
    }


}

