package com.gaggum

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import io.socket.client.IO
import io.socket.client.Socket

class MapScanActivity : AppCompatActivity() {

    private lateinit var mSocket: Socket

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map_scan)

        val gifImageView: ImageView = findViewById(R.id.gifImageView)

        Glide.with(this)
            .asGif()
            .load(R.drawable.plans_blueprint)
            .into(gifImageView)

        mSocket = IO.socket("https://j8b310.p.ssafy.io")
        mSocket.connect()
        mSocket.emit("run_mapping", 1)
        mSocket.on("run_mapping") { args ->
            val data = args[0] as Int
            if (data == -1) {
                runOnUiThread {
                    Toast.makeText(this, "스캔이 완료되었습니다.", Toast.LENGTH_LONG).show()
                }
                navigateToMainActivity()
            }
        }
    }

    override fun onBackPressed() {
        val dialogView = LayoutInflater.from(this).inflate(R.layout.map_scan_dialog, null)

        val dialogTitle = dialogView.findViewById<TextView>(R.id.dialog_title)
        val dialogMessage = dialogView.findViewById<TextView>(R.id.dialog_message)
        val positiveButton = dialogView.findViewById<Button>(R.id.dialog_positive_button)
        val negativeButton = dialogView.findViewById<Button>(R.id.dialog_negative_button)

        val alertDialog = AlertDialog.Builder(this)
            .setView(dialogView)
            .show()

        positiveButton.setOnClickListener {
            mSocket.emit("run_mapping", 0)
            navigateToMainActivity()
            alertDialog.dismiss()
        }

        negativeButton.setOnClickListener {
            alertDialog.dismiss()
        }
    }

    private fun navigateToMainActivity() {
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
        finish()
    }

    override fun onDestroy() {
        super.onDestroy()
        mSocket.disconnect()
    }
}
