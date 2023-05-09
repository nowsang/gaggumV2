package com.gaggum

import android.annotation.SuppressLint
import android.app.AlertDialog
import android.content.Context
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.Window
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView
import retrofit2.Response
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

class DiaryAdapter(private val diaryList: List<diaryInfo>, private val context: Context, private val diaryFragment: DiaryFragment) :
    RecyclerView.Adapter<DiaryAdapter.DiaryViewHolder>() {

    class DiaryViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val diaryTitle: TextView = itemView.findViewById(R.id.diaryTitle)
        val diaryMemo: TextView = itemView.findViewById(R.id.diaryMemo)
        val diaryDate: TextView = itemView.findViewById(R.id.diaryDate)
        val diaryImg: TextView = itemView.findViewById(R.id.diaryImg)
        val diaryId: TextView = itemView.findViewById(R.id.diaryId)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DiaryViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.diary_item, parent, false)
        return DiaryViewHolder(itemView)
    }

    @SuppressLint("NewApi")
    override fun onBindViewHolder(holder: DiaryViewHolder, position: Int) {
        val currentItem = diaryList[position]

        holder.diaryTitle.text = currentItem.diaryTitle
        holder.diaryMemo.text = currentItem.diaryMemo
        holder.diaryImg.text = currentItem.diaryImg
        holder.diaryId.text = currentItem.diaryId.toString() //이렇게돼도 인트맞나..

        val dateString = currentItem.diaryDate
        val formatter = DateTimeFormatter.ISO_DATE_TIME
        val dateTime = LocalDateTime.parse(dateString, formatter)
        val formattedDate = dateTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd"))
        holder.diaryDate.text = formattedDate

        holder.itemView.setOnClickListener {
            showDiaryDetailsDialog(holder.itemView.context, currentItem)
        }
    }

    override fun getItemCount() = diaryList.size

    private fun showDiaryDetailsDialog(context: Context, diary: diaryInfo) {
        val dialogView = LayoutInflater.from(context).inflate(R.layout.diary_detail_modal, null)

        dialogView.findViewById<EditText>(R.id.dialog_diary_title).setText(diary.diaryTitle)
        dialogView.findViewById<EditText>(R.id.dialog_diary_memo).setText(diary.diaryMemo)

        val alertDialog = AlertDialog.Builder(context)
            .setView(dialogView)
            .setPositiveButton("저장") { dialog, _ ->
                val updatedTitle = dialogView.findViewById<EditText>(R.id.dialog_diary_title).text.toString()
                val updatedMemo = dialogView.findViewById<EditText>(R.id.dialog_diary_memo).text.toString()

                // 수정된 데이터를 서버로 보내는 코드
                updateDiaryOnServer(diary.diaryId, updatedTitle, updatedMemo)

                dialog.dismiss()
            }
            .setNegativeButton("취소") { dialog, _ ->
                dialog.dismiss()
            }
            .create()
        alertDialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
//        alertDialog.window?.requestFeature(Window.FEATURE_NO_TITLE)

        alertDialog.show()
    }



    // 서버에 다이어리를 업데이트하는 함수를 여기에 추가해 주세요.
    private fun updateDiaryOnServer(diaryId: Int, updatedTitle: String, updatedMemo: String) {
        // 서버와 통신하여 다이어리를 업데이트하는 코드를 여기에 작성해주세요.


        val service = RetrofitObject.service
        service.editDiary(editDiaryRequestBody(diaryId,updatedTitle,updatedMemo)).enqueue(object : retrofit2.Callback<editDiaryResponseBody> {
            override fun onResponse(
                call: retrofit2.Call<editDiaryResponseBody>,
                response: Response<editDiaryResponseBody>
            ) {

                Log.e("결과", response.toString())
                val msg = response.body()?.data
                Log.e("메세지",msg.toString())
                if (response.isSuccessful) {
                    Toast.makeText(context, "수정 완료", Toast.LENGTH_SHORT).show()
                    diaryFragment.getDiariesFromServer(diaryFragment.requireView())
                } else {
                    Toast.makeText(context, "수정에 실패했습니다.", Toast.LENGTH_SHORT).show()
                }
            }
            override fun onFailure(
                call: retrofit2.Call<editDiaryResponseBody>,
                t: Throwable
            ) {
                Toast.makeText(context, "수정에 실패했습니다.", Toast.LENGTH_SHORT)
                    .show()
//                Log.e("아무거나",t.toString())
            }

        })
    }
}
