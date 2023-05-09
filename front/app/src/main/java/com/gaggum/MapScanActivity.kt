package com.gaggum;

// Import 추가
import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide

class MapScanActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map_scan)

        // ImageView 참조
        val gifImageView: ImageView = findViewById(R.id.gifImageView)

        // Glide로 GIF 로드 및 ImageView에 적용
        Glide.with(this)
            .asGif()
            .load(R.drawable.plans_blueprint) // 여기에 실제 GIF 파일 이름을 넣어주세요
            .into(gifImageView)
    }
}
