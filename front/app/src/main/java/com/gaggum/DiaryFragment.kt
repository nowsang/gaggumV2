package com.gaggum

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.Toast
import androidx.navigation.Navigation
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class DiaryFragment : Fragment() {

//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_diary, container, false)


        val getAllDiariesBtn = view.findViewById<Button>(R.id.getAllDiariesBtn)
        getAllDiariesBtn.setOnClickListener {

            val service = RetrofitObject.service
            service
                .getAllDiary(1).enqueue(object : Callback<GetAllDiariesResponseBody> {
                    override fun onResponse(
                        call: Call<GetAllDiariesResponseBody>,
                        response: Response<GetAllDiariesResponseBody>
                    ) {

                        Log.e("결과", response.toString())
                        if (response.isSuccessful) {
                            var diaries = response.body()?.data!![1]
                            Toast.makeText(context, diaries.toString(), Toast.LENGTH_LONG).show()
                            if (diaries != null) {

                            } else {
                                Toast.makeText(
                                    requireContext(),
                                    "다이어리 목록이 없습니다.",
                                    Toast.LENGTH_SHORT
                                ).show()
                            }
                        } else {
                            Toast.makeText(requireContext(), "다이어리 목록을 가져오는 데 실패했습니다.", Toast.LENGTH_SHORT)
                                .show()
                        }
                    }

                    override fun onFailure(
                        call: retrofit2.Call<GetAllDiariesResponseBody>,
                        t: Throwable
                    ) {
                        Toast.makeText(requireContext(), "다이어리 목록을 가져오는 데 실패했습니다.", Toast.LENGTH_SHORT).show()
                    }
                })

        }


        return view
    }
}

