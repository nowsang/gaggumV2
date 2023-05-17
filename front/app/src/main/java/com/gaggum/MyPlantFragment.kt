package com.gaggum

import android.content.Context
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.room.Room
import com.gaggum.databinding.FragmentMyPlantBinding
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import retrofit2.Call
import retrofit2.Response
import retrofit2.Callback
import java.util.Objects


class MyPlantFragment : Fragment() {

    private lateinit var mainActivity : MainActivity
    private lateinit var allPlantsList : ArrayList<allPlants>
    private lateinit var myPlantRVAdapter: MyPlantRVAdapter

    // Room DB
    private lateinit var db : ClientDatabase
    private var turtleId : Int = 0
    private lateinit var user : String

    override fun onAttach(context: Context) {
        super.onAttach(context)
        mainActivity = context as MainActivity
        db = Room.databaseBuilder(context, ClientDatabase::class.java, "ClientDatabase")
            .build()
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        // Inflate the layout for this fragment
        val binding = FragmentMyPlantBinding.inflate(inflater, container, false)

        // Room DB
        user = Firebase.auth.currentUser!!.uid

        GlobalScope.launch(Dispatchers.IO) {
            val retrievedUser = db.clientDao().getTurtleId(user)
            if (retrievedUser != null) {
                withContext(Dispatchers.Main) {
                    turtleId = retrievedUser.turtleId
                    getAllPlants()

                }
            } else {
                Log.e("실패", "실패하였습니다.")
            }
        }

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
            .getAllPlantsData(turtleId)
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

