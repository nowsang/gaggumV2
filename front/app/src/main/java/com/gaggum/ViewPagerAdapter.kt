package com.gaggum

import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.RecyclerView.Recycler
import com.bumptech.glide.Glide

class ViewPagerAdapter(var slides : List<allPlants>, val context: Context) : RecyclerView.Adapter<ViewPagerAdapter.SlideViewHolder>() {

    inner class SlideViewHolder(view : View) : RecyclerView.ViewHolder(view) {
        val imageView : ImageView = view.findViewById(R.id.pv_item_img)
        val textView : TextView = view.findViewById(R.id.pv_item_text)
    }

    override fun getItemCount(): Int {
        return slides.size
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): SlideViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.pv_item, parent, false)
        return SlideViewHolder(view)
    }

    override fun onBindViewHolder(holder: SlideViewHolder, position: Int) {
        val slide = slides[position]
        Glide
            .with(context)
            .load(slide.plantImg)
            .into(holder.imageView)
        holder.textView.text = slide.plantName
        holder.imageView.setOnClickListener {
            val intent = Intent(context, PlantDetailActivity::class.java)
            intent.putExtra("plantId", slide.plantId)
            context.startActivity(intent)
        }

        holder.textView.setOnClickListener {
            val intent = Intent(context, PlantDetailActivity::class.java)
            intent.putExtra("plantId", slide.plantId)
            context.startActivity(intent)
        }

    }

}