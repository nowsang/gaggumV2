package com.gaggum

import android.annotation.SuppressLint
import android.app.AlertDialog
import android.content.Context
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Handler
import android.os.Looper
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.Window
import android.widget.*
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.load.MultiTransformation
import com.bumptech.glide.load.resource.bitmap.Rotate
import com.bumptech.glide.load.resource.bitmap.RoundedCorners
import com.bumptech.glide.request.RequestOptions
import retrofit2.Response
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

class DiaryAdapter(private val diaryList: List<diaryInfo>, private val context: Context, private val diaryFragment: DiaryFragment) :
    RecyclerView.Adapter<DiaryAdapter.DiaryViewHolder>() {
    fun getItem(position: Int): diaryInfo {
        Log.e("다이어리 프래그먼트", diaryFragment.toString())
        return diaryList[position]
    }
    class DiaryViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val diaryTitle: EditText = itemView.findViewById(R.id.diaryTitle)
        val diaryMemo: EditText = itemView.findViewById(R.id.diaryMemo)
        val diaryDate: TextView = itemView.findViewById(R.id.diaryDate)
        val diaryImg: ImageView = itemView.findViewById(R.id.diaryImg)
        val diaryId: TextView = itemView.findViewById(R.id.diaryId)
        val deleteBtn: Button = itemView.findViewById(R.id.deleteBtn)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DiaryViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.diary_item, parent, false)
        return DiaryViewHolder(itemView)
    }


    @SuppressLint("NewApi")
    override fun onBindViewHolder(holder: DiaryViewHolder, position: Int) {
        val currentItem = getItem(position)
        holder.deleteBtn.setOnClickListener {
            deleteDiaryOnServer(currentItem.diaryId)
            // 여기서 position을 사용하여 로컬 목록에서 해당 항목을 제거하고 목록이 갱신되도록 합니다.
            (diaryList as ArrayList).removeAt(position)
            notifyItemRemoved(position)
            notifyItemRangeChanged(position, diaryList.size)
        }

        holder.diaryTitle.setText(currentItem.diaryTitle)
        holder.diaryMemo.setText(currentItem.diaryMemo)
        // 이미지 로딩
        val imageUrl = currentItem.diaryImg
        Glide.with(context)
            .load(imageUrl)
            .centerCrop()
            .apply(RequestOptions().transform(MultiTransformation(Rotate(90), RoundedCorners(24))))
//            .apply(RequestOptions().transform(RoundedCorners(8)))
            .placeholder(R.drawable.nav_my_plant) // 기본 이미지를 설정합니다. 필요한 경우 파일 이름을 바꿔주세요.
            .error(R.drawable.nav_my_plant) // 이미지 로딩에 실패한 경우 표시할 이미지를 설정합니다. 필요한 경우 파일 이름을 바꿔주세요.
            .into(holder.diaryImg)

        holder.diaryId.text = currentItem.diaryId.toString() // 이렇게 해도 Int 형이 맞습니다.

        val dateString = currentItem.diaryDate
        val formatter = DateTimeFormatter.ISO_DATE_TIME
        val dateTime = LocalDateTime.parse(dateString, formatter)
        val formattedDate = dateTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd"))
        holder.diaryDate.text = formattedDate


        val titleHandler = Handler(Looper.getMainLooper())
        val titleRunnable = Runnable {
            val updatedTitle = holder.diaryTitle.text.toString()
            updateDiaryOnServer(currentItem.diaryId, updatedTitle, currentItem.diaryMemo)
        }

        holder.diaryTitle.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
            }

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
            }

            override fun afterTextChanged(s: Editable?) {
                titleHandler.removeCallbacks(titleRunnable)
                titleHandler.postDelayed(titleRunnable, 500) // 1000ms delay
            }
        })

        val memoHandler = Handler(Looper.getMainLooper())
        val memoRunnable = Runnable {
            val updatedMemo = holder.diaryMemo.text.toString()
            updateDiaryOnServer(currentItem.diaryId, currentItem.diaryTitle, updatedMemo)
        }

        holder.diaryMemo.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
            }

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
            }

            override fun afterTextChanged(s: Editable?) {
                memoHandler.removeCallbacks(memoRunnable)
                memoHandler.postDelayed(memoRunnable, 500) // 1000ms delay
            }
        })

        // 추가 작업을 수행하십시오 (예: 삭제 버튼 설정, 작성 날짜 표시 등)
    }

    override fun getItemCount() = diaryList.size

//    private fun showDiaryDetailsDialog(context: Context, diary: diaryInfo) {
//        val dialogView = LayoutInflater.from(context).inflate(R.layout.diary_detail_modal, null)
//
//        dialogView.findViewById<EditText>(R.id.dialog_diary_title).setText(diary.diaryTitle)
//        dialogView.findViewById<EditText>(R.id.dialog_diary_memo).setText(diary.diaryMemo)
//
//        val alertDialog = AlertDialog.Builder(context)
//            .setView(dialogView)
//            .setPositiveButton("저장") { dialog, _ ->
//                val updatedTitle = dialogView.findViewById<EditText>(R.id.dialog_diary_title).text.toString()
//                val updatedMemo = dialogView.findViewById<EditText>(R.id.dialog_diary_memo).text.toString()
//
//                // 수정된 데이터를 서버로 보내는 코드
//                updateDiaryOnServer(diary.diaryId, updatedTitle, updatedMemo)
//
//                dialog.dismiss()
//            }
//            .setNegativeButton("취소") { dialog, _ ->
//                dialog.dismiss()
//            }
//            .create()
//        alertDialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
////        alertDialog.window?.requestFeature(Window.FEATURE_NO_TITLE)
//
//        alertDialog.show()
//    }




    private fun updateDiaryOnServer(diaryId: Int, updatedTitle: String, updatedMemo: String) {
        // 서버와 통신하여 다이어리를 업데이트하는 코드


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
//                    Toast.makeText(context, "수정 완료", Toast.LENGTH_SHORT).show()
//                    diaryFragment.getDiariesFromServer(diaryFragment.requireView())
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

    private fun deleteDiaryOnServer(diaryId: Int) {
        val service = RetrofitObject.service
        service.deleteDiary(deleteDiaryRequestBody(diaryId)).enqueue(object : retrofit2.Callback<deleteDiaryResponseBody> {
            override fun onResponse(
                call: retrofit2.Call<deleteDiaryResponseBody>,
                response: Response<deleteDiaryResponseBody>
            ) {

                Log.e("결과", response.toString())
                val msg = response.body()?.data
                Log.e("메세지",msg.toString())
                if (response.isSuccessful) {
                    Toast.makeText(context, "삭제 완료", Toast.LENGTH_SHORT).show()
//                    diaryFragment.getDiariesFromServer(diaryFragment.requireView())
                } else {
                    Toast.makeText(context, "삭제에 실패했습니다.", Toast.LENGTH_SHORT).show()
                }
            }
            override fun onFailure(
                call: retrofit2.Call<deleteDiaryResponseBody>,
                t: Throwable
            ) {
                Toast.makeText(context, "삭제에 실패했습니다.2", Toast.LENGTH_SHORT)
                    .show()
//                Log.e("아무거나",t.toString())
            }

        })
    }
}
