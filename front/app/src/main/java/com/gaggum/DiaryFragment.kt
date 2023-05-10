package com.gaggum

import android.app.AlertDialog
import android.app.Dialog
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Bundle
import android.util.Log
import android.view.Gravity
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import android.widget.ArrayAdapter
import android.view.WindowManager
import androidx.room.Room
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class DiaryFragment : Fragment() {
    private lateinit var diaries: List<diaryInfo>
//    private val fixedYears = listOf("2020", "2021", "2022", "2023", "2024", "2025")
//    private val fixedMonths = (1..12).map { String.format("%02d", it) }

    // Room DB
    private lateinit var db : ClientDatabase
    private var turtleId : Int = 0
    private lateinit var user : String

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_diary, container, false)
        db = Room.databaseBuilder(context!!, ClientDatabase::class.java, "ClientDatabase")
            .build()
        user = Firebase.auth.currentUser!!.uid

        GlobalScope.launch(Dispatchers.IO) {
            val retrievedUser = db.clientDao().getTurtleId(user)
            if (retrievedUser != null) {
                withContext(Dispatchers.Main) {
                    turtleId = retrievedUser.turtleId
                    getDiariesFromServer(view)

                }
            } else {
                Log.e("실패", "실패하였습니다.")
            }
        }



        val recyclerView = view.findViewById<RecyclerView>(R.id.singRV)
        recyclerView.layoutManager = LinearLayoutManager(context)

        getDiariesFromServer(view)

        return view
    }

    fun getDiariesFromServer(view: View) {
        val service = RetrofitObject.service
        service.getAllDiary(turtleId).enqueue(object : Callback<GetAllDiariesResponseBody> {
            override fun onResponse(
                call: Call<GetAllDiariesResponseBody>,
                response: Response<GetAllDiariesResponseBody>
            ) {
                Log.e("결과", response.toString())
                if (response.isSuccessful) {
                    diaries = response.body()?.data ?: emptyList()
//                    Toast.makeText(context, diaries.toString(), Toast.LENGTH_LONG).show()
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
        recyclerView.adapter = DiaryAdapter(diaries, requireContext(), this) // Add requireContext()

        val testTitles = diaries.map { it.diaryTitle }.distinct()

        val years = listOf("전체", "2020", "2021", "2022", "2023", "2024", "2025")
        val months = listOf("전체", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")

        setupButtons(view, testTitles, years, months)
    }


    private fun filterDiariesByTitleAndYearAndMonth(
        selectedTitle: String,
        selectedYear: String,
        selectedMonth: String,
        diaries: List<diaryInfo>,
        view: View
    ) {
        val filteredDiaries = diaries.filter {
            (it.diaryTitle == selectedTitle || selectedTitle == "전체보기") &&
                    (it.diaryDate.substring(0, 4) == selectedYear || selectedYear == "전체") &&
                    (it.diaryDate.substring(5, 7) == selectedMonth || selectedMonth == "전체")
        }
        val recyclerView = view.findViewById<RecyclerView>(R.id.singRV)
        recyclerView.adapter = DiaryAdapter(filteredDiaries, requireContext(), this)
    }

    private fun setupButtons(view: View, testTitles: List<String>, years: List<String>, months: List<String>) {
        val titleButton = view.findViewById<Button>(R.id.titleButton)
        val yearButton = view.findViewById<Button>(R.id.yearButton)
        val monthButton = view.findViewById<Button>(R.id.monthButton)

        titleButton.setOnClickListener {
            val items = listOf("전체보기") + testTitles
            showBottomDialog("이름 선택", items) { selectedItem ->
                titleButton.text = selectedItem
                val selectedYear = yearButton.text.toString()
                val selectedMonth = monthButton.text.toString()
                filterDiariesByTitleAndYearAndMonth(selectedItem, selectedYear, selectedMonth, diaries, view)
            }
        }

        yearButton.setOnClickListener {
            val items = years
            showBottomDialog("년도 선택", items) { selectedItem ->
                yearButton.text = selectedItem
                val selectedTitle = titleButton.text.toString()
                val selectedMonth = monthButton.text.toString()
                filterDiariesByTitleAndYearAndMonth(selectedTitle, selectedItem, selectedMonth, diaries, view)
            }
        }

        monthButton.setOnClickListener {
            val items = months
            showBottomDialog("월 선택", items) { selectedItem ->
                monthButton.text = selectedItem
                val selectedTitle = titleButton.text.toString()
                val selectedYear = yearButton.text.toString()
                filterDiariesByTitleAndYearAndMonth(selectedTitle, selectedYear, selectedItem, diaries, view)
            }
        }

    }

    private fun showOptionsDialog(options: List<String>, defaultOption: String, onOptionSelected: (String) -> Unit) {
        val builder = AlertDialog.Builder(requireContext())
        builder.setItems(options.toTypedArray()) { _, which ->
            val selectedOption = if (which == 0) defaultOption else options[which]
            onOptionSelected(selectedOption)
        }
        builder.create().show()
    }

    private fun showBottomDialog(title: String, items: List<String>, onItemSelected: (String) -> Unit) {
        val dialog = Dialog(requireContext(), R.style.BottomDialogAnimation)
        val dialogView = LayoutInflater.from(requireContext()).inflate(R.layout.dialog_bottom, null)

        val titleTextView = dialogView.findViewById<TextView>(R.id.dialogTitle)
        titleTextView.text = title

        val listView = dialogView.findViewById<ListView>(R.id.listView)
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_list_item_1, items)
        listView.adapter = adapter

        listView.setOnItemClickListener { _, _, position, _ ->
            onItemSelected(items[position])
            dialog.dismiss()
        }

        dialog.setContentView(dialogView)
        dialog.window?.setGravity(Gravity.BOTTOM)

        // 모달의 배경을 어둡게 처리
        dialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
        val layoutParams = WindowManager.LayoutParams().apply {
            copyFrom(dialog.window?.attributes)
            width = WindowManager.LayoutParams.MATCH_PARENT
            height = WindowManager.LayoutParams.WRAP_CONTENT
            gravity = Gravity.BOTTOM
            dimAmount = 0.5f
            flags = flags or WindowManager.LayoutParams.FLAG_DIM_BEHIND
        }
        dialog.window?.attributes = layoutParams

        // 배경을 클릭하면 모달이 닫히도록 설정
        dialogView.setOnClickListener {
            dialog.dismiss()
        }

        // 리스트뷰의 배경을 투명하게 설정하여 배경 클릭이 가능하게 함
        listView.setBackgroundColor(Color.TRANSPARENT)

        dialog.setOnCancelListener {
            dialog.dismiss()
        }

        // 추가: 배경을 클릭하면 모달이 닫히도록 설정
        dialog.setCanceledOnTouchOutside(true)

        dialog.show()
    }










}