package com.gaggum

import android.annotation.SuppressLint
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter


class DiaryAdapter(private val diaryList: List<diaryInfo>) :
    RecyclerView.Adapter<DiaryAdapter.DiaryViewHolder>() {

    class DiaryViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val diaryTitle: TextView = itemView.findViewById(R.id.diaryTitle)
        val diaryMemo: TextView = itemView.findViewById(R.id.diaryMemo)
        val diaryDate: TextView = itemView.findViewById(R.id.diaryDate)
        val diaryImg: TextView = itemView.findViewById(R.id.diaryImg)

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

        val dateString = currentItem.diaryDate
        val formatter = DateTimeFormatter.ISO_DATE_TIME // 린트로 해결
        val dateTime = LocalDateTime.parse(dateString, formatter)
        val formattedDate = dateTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd"))
        holder.diaryDate.text = formattedDate
//        holder.diaryDate.text = currentItem.diaryDate

    }

    override fun getItemCount() = diaryList.size
}
