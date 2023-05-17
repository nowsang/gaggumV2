package com.gaggum

import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide

class MyPlantRVAdapter(context : Context) : RecyclerView.Adapter<MyPlantRVAdapter.ViewHolder>() {

    var plants = mutableListOf<allPlants>()
    var context = context

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val plantName = itemView.findViewById<TextView>(R.id.myPlantName)
        private val plantSpecies = itemView.findViewById<TextView>(R.id.myPlantSpecies)
        private val plantImg = itemView.findViewById<ImageView>(R.id.myPlantImg)

        fun bindItems(item: allPlants) {
            plantName.text = item.plantName
            plantSpecies.text = item.plantSpecies
            Glide.with(itemView).load(item.plantImg).into(plantImg)

            itemView.setOnClickListener {
                val intent = Intent(context, PlantDetailActivity::class.java)
                intent.putExtra("plantId", item.plantId)
                context.startActivity(intent)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.rv_item_my_plant, parent, false)
        return ViewHolder(view)
    }

    override fun getItemCount(): Int {
        return plants.size
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bindItems(plants[position])
    }


}