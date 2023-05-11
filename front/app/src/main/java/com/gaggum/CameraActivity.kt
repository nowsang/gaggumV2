package com.gaggum

import android.Manifest
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.util.DisplayMetrics
import android.util.Log
import android.view.Surface
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageCapture
import androidx.camera.core.ImageCaptureException
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.core.content.ContextCompat
import com.gaggum.databinding.ActivityCameraBinding
import java.io.File
import java.text.SimpleDateFormat
import java.util.*
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors
import android.view.Display
import android.view.WindowManager
import java.io.IOException

class CameraActivity : AppCompatActivity() {
    private lateinit var imageCapture: ImageCapture
    private lateinit var cameraExecutor: ExecutorService
    private lateinit var binding: ActivityCameraBinding

    private val requestPermissionLauncher = registerForActivityResult(ActivityResultContracts.RequestPermission()) { isGranted: Boolean ->
        if (isGranted) {
            startCamera()
        } else {
            Log.e("CameraActivity", "Camera permission not granted")
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCameraBinding.inflate(layoutInflater)
        setContentView(binding.root)

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
            startCamera()
        } else {
            requestPermissionLauncher.launch(Manifest.permission.CAMERA)
        }

        cameraExecutor = Executors.newSingleThreadExecutor()

        binding.btnTakePhoto.setOnClickListener {
            takePhoto()
        }
    }

    private fun startCamera() {
        val cameraProviderFuture = ProcessCameraProvider.getInstance(this)

        cameraProviderFuture.addListener({
            val cameraProvider = cameraProviderFuture.get()

            val preview = androidx.camera.core.Preview.Builder()
                .build()
                .also { it.setSurfaceProvider(binding.previewView.surfaceProvider) }

            val windowManager = getSystemService(Context.WINDOW_SERVICE) as WindowManager
            val rotation = windowManager.defaultDisplay.rotation

            imageCapture = ImageCapture.Builder()
                .setTargetRotation(rotation)
                .build()

            val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA

            cameraProvider.unbindAll()
            cameraProvider.bindToLifecycle(this, cameraSelector, preview, imageCapture)
        }, ContextCompat.getMainExecutor(this))
    }


    private fun takePhoto() {
        val imageCapture = imageCapture ?: return

        val timeStamp: String = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(Date())
        val storageDir: File? = getExternalFilesDir(null)
        val photoFile = File.createTempFile("JPEG_${timeStamp}_", ".jpg", storageDir)

        val outputOptions = ImageCapture.OutputFileOptions.Builder(photoFile).build()

        val windowManager = getSystemService(Context.WINDOW_SERVICE) as WindowManager
        val rotation = windowManager.defaultDisplay.rotation

        // Update target rotation
        imageCapture.targetRotation = rotation

        imageCapture.takePicture(
            outputOptions, ContextCompat.getMainExecutor(this), object : ImageCapture.OnImageSavedCallback {
                override fun onImageSaved(outputFileResults: ImageCapture.OutputFileResults) {
                    val savedUri = Uri.fromFile(photoFile)
                    Log.d("CameraActivity", "Photo capture succeeded: $savedUri")

                    showCapturedImage(savedUri)
                }

                override fun onError(exception: ImageCaptureException) {
                    Log.e("CameraActivity", "Photo capture failed: ${exception.message}", exception)
                }
            })
    }










    private fun showCapturedImage(uri: Uri) {
        val intent = Intent(this, ImagePreviewActivity::class.java).apply {
            putExtra("image_uri", uri.toString())
        }
        startActivity(intent)
    }

    private fun getRotation(): Int {
        val display = binding.previewView.display
        val displayMetrics = DisplayMetrics()
        display.getMetrics(displayMetrics)

        return when (display.rotation) {
            Surface.ROTATION_0 -> 0
            Surface.ROTATION_90 -> 90
            Surface.ROTATION_180 -> 180
            Surface.ROTATION_270 -> 270
            else -> 0
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        cameraExecutor.shutdown()
    }
}