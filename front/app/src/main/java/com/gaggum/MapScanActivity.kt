package com.gaggum

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.util.Log
import android.view.LayoutInflater
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import com.bumptech.glide.Glide
import io.socket.client.IO
import io.socket.client.Socket
import org.json.JSONObject

class MapScanActivity : AppCompatActivity() {
    override fun onUserLeaveHint() {
        super.onUserLeaveHint()

        val serviceIntent = Intent(this, MyForegroundService::class.java)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(serviceIntent)
        } else {
            startService(serviceIntent)
        }
    }

    private lateinit var mSocket: Socket
    private val channelId = "channel_id"
    private lateinit var context: Context

    override fun onCreate(savedInstanceState: Bundle?) {




        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map_scan)

        context = this

        val gifImageView: ImageView = findViewById(R.id.gifImageView)

        Glide.with(this)
            .asGif()
            .load(R.drawable.plans_blueprint)
            .into(gifImageView)

        createNotificationChannel()

        mSocket = IO.socket("https://k8b101.p.ssafy.io")
        mSocket.connect()
//        val jsonObject = JSONObject()
//        jsonObject.put("mode", "motor")
//        jsonObject.put("motor_status", 2)
        mSocket.emit("run_walltracking", 1)
        mSocket.on("run_walltracking") { args ->
            val data = args[0] as Int
            if (data == -1) {
                runOnUiThread {
                    val notificationId = 1
                    val notificationBuilder = NotificationCompat.Builder(context, channelId)
                        .setSmallIcon(R.drawable.maskable_icon_x192_logo)
                        .setContentTitle("스캔 완료")
                        .setContentText("집 스캔이 종료되었습니다")
                        .setPriority(NotificationCompat.PRIORITY_DEFAULT)

                    val notificationManager = NotificationManagerCompat.from(context)
                    try {
                        notificationManager.notify(notificationId, notificationBuilder.build())
                    } catch (e: SecurityException) {
                        // Handle the exception appropriately.
                    }

                    Log.e("스캔완료", data.toString())
                    navigateToMainActivity()
                }
            }
        }


    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = getString(R.string.channel_name)
            val descriptionText = getString(R.string.channel_description)
            val importance = NotificationManager.IMPORTANCE_DEFAULT
            val channel = NotificationChannel(channelId, name, importance).apply {
                description = descriptionText
            }
            val notificationManager: NotificationManager =
                getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
            notificationManager.createNotificationChannel(channel)
        }
    }

    override fun onBackPressed() {
        val dialogView = LayoutInflater.from(this).inflate(R.layout.map_scan_cancel_dialog, null)


        val positiveButton = dialogView.findViewById<Button>(R.id.dialog_positive_button)
        val negativeButton = dialogView.findViewById<Button>(R.id.dialog_negative_button)

        val alertDialog = AlertDialog.Builder(this)
            .setView(dialogView)
            .show()

            positiveButton.setOnClickListener {
                mSocket.emit("run_mapping", 0)
                finish()
//                navigateToMainActivity()
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
