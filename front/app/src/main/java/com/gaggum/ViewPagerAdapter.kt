package com.gaggum

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide

class ViewPagerAdapter(plants : ArrayList<allPlants>) : RecyclerView.Adapter<ViewPagerAdapter.PagerViewHolder>() {

    var plants = plants

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PagerViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.pv_item, parent, false)
        return PagerViewHolder(view)
    }

    override fun onBindViewHolder(holder: PagerViewHolder, position: Int) {
        holder.bind(plants[position])
    }

    override fun getItemCount(): Int {
        return plants.size
    }
    inner class PagerViewHolder(itemView : View) : RecyclerView.ViewHolder(itemView) {
        private val plantImg = itemView.findViewById<ImageView>(R.id.pv_item)
        fun bind(item : allPlants) {
            Glide
                .with(itemView)
                .load(item.plantImg)
                .into(plantImg)
        }
    }
}