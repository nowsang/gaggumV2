package com.gaggum

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.navigation.Navigation
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import android.widget.ArrayAdapter

class DiaryFragment : Fragment() {
    private lateinit var diaries: List<diaryInfo>
//    private val fixedYears = listOf("2020", "2021", "2022", "2023", "2024", "2025")
//    private val fixedMonths = (1..12).map { String.format("%02d", it) }
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_diary, container, false)

        val recyclerView = view.findViewById<RecyclerView>(R.id.singRV)
        recyclerView.layoutManager = LinearLayoutManager(context)

        getDiariesFromServer(view)

        return view
    }

    private fun getDiariesFromServer(view: View) {
        val service = RetrofitObject.service
        service.getAllDiary(1).enqueue(object : Callback<GetAllDiariesResponseBody> {
            override fun onResponse(
                call: Call<GetAllDiariesResponseBody>,
                response: Response<GetAllDiariesResponseBody>
            ) {
                Log.e("결과", response.toString())
                if (response.isSuccessful) {
                    diaries = response.body()?.data ?: emptyList()
                    Toast.makeText(context, diaries.toString(), Toast.LENGTH_LONG).show()
                    if (diaries.isNotEmpty()) {
                        setUpDiaryViews(diaries, view)
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
                Toast.makeText(requireContext(), "다이어리 목록을 가져오는 데 실패했습니다.", Toast.LENGTH_SHORT)
                    .show()
            }
        })
    }

    private fun setUpDiaryViews(diaries: List<diaryInfo>, view: View) {
        val recyclerView = view.findViewById<RecyclerView>(R.id.singRV)
        recyclerView.adapter = DiaryAdapter(diaries)

        val testTitles = diaries.map { it.diaryTitle }.distinct()
        setupSpinner(view, testTitles)

        setupYearMonthSpinners(view) // 인자 diaries를 제거합니다.
    }

    private fun setupSpinner(view: View, testTitles: List<String>) {
        val spinner = view.findViewById<Spinner>(R.id.spinner)
        val allTitles = listOf("전체보기") + testTitles
        val arrayAdapter =
            ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, allTitles)
        arrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spinner.adapter = arrayAdapter

        spinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(
                parent: AdapterView<*>?,
                spinnerView: View?,
                position: Int,
                id: Long
            ) {
                val selectedTitle = allTitles[position]
                val filteredDiaries = if (selectedTitle == "전체보기") {
                    diaries
                } else {
                    diaries.filter { it.diaryTitle == selectedTitle }
                }
                val recyclerView = view.findViewById<RecyclerView>(R.id.singRV)
                recyclerView.adapter = DiaryAdapter(filteredDiaries)
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {
                // Do nothing
            }
        }
    }

    private fun setupYearMonthSpinners(view: View) {
        val years = listOf("전체", "2020", "2021", "2022", "2023", "2024", "2025")
        val yearSpinner = view.findViewById<Spinner>(R.id.yearSpinner)
        val yearAdapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, years)
        yearAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        yearSpinner.adapter = yearAdapter

        val months = listOf("전체", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        val monthSpinner = view.findViewById<Spinner>(R.id.monthSpinner)
        val monthAdapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, months)
        monthAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        monthSpinner.adapter = monthAdapter

        yearSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>?, spinnerView: View?, position: Int, id: Long) {
                val selectedYear = years[position]
                val selectedMonth = months[monthSpinner.selectedItemPosition]
                filterDiariesByYearAndMonth(selectedYear, selectedMonth, diaries, view)
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {
                // Do nothing
            }
        }

        monthSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>?, spinnerView: View?, position: Int, id: Long) {
                val selectedYear = years[yearSpinner.selectedItemPosition]
                val selectedMonth = months[position]
                filterDiariesByYearAndMonth(selectedYear, selectedMonth, diaries, view)
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {
                // Do nothing
            }
        }
    }

    private fun filterDiariesByYearAndMonth(selectedYear: String, selectedMonth: String, diaries: List<diaryInfo>, view: View?) {
        val filteredDiaries = diaries.filter {
            (it.diaryDate.substring(0, 4) == selectedYear || selectedYear == "전체") &&
                    (it.diaryDate.substring(5, 7) == selectedMonth || selectedMonth == "전체")
        }
        val recyclerView = view?.findViewById<RecyclerView>(R.id.singRV)
        recyclerView?.adapter = DiaryAdapter(filteredDiaries)
    }
}