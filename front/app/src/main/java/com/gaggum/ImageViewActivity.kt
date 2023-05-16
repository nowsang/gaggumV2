package com.gaggum

import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import com.bumptech.glide.load.resource.bitmap.Rotate
import com.bumptech.glide.request.RequestOptions

class ImageViewActivity : AppCompatActivity() {
    private var imageUrl: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_view) // 이 레이아웃 파일이 필요합니다.

        imageUrl = intent.getStringExtra(ARG_IMAGE_URL)

        val imageView: ImageView = findViewById(R.id.fullScreenImageView)
        Glide.with(this)
            .load(imageUrl)
            .apply(RequestOptions.bitmapTransform(Rotate(90)))
            .into(imageView)
    }

    companion object {
        const val ARG_IMAGE_URL = "imageUrl"
    }
}
