package com.gaggum

import android.app.AlertDialog
import android.app.Dialog
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.gaggum.databinding.ActivityImagePreviewBinding
import kotlinx.coroutines.launch
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.asRequestBody
import java.io.File
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.util.Base64
import android.util.Log
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.view.WindowManager
import android.widget.*
import androidx.core.content.ContentProviderCompat.requireContext
import androidx.recyclerview.widget.RecyclerView
import org.json.JSONObject
import java.io.ByteArrayOutputStream
import com.bumptech.glide.Glide
import com.bumptech.glide.load.engine.DiskCacheStrategy
import com.bumptech.glide.request.RequestOptions
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class ImagePreviewActivity : AppCompatActivity() {

    private lateinit var binding: ActivityImagePreviewBinding
    private lateinit var imageFile: File
    private lateinit var allPlantsList : ArrayList<allPlants>
    private lateinit var myPlantRVAdapter: MyPlantRVAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityImagePreviewBinding.inflate(layoutInflater)
        setContentView(binding.root)
        getAllPlants()

        val imageUri = intent.getStringExtra("image_uri")
        if (imageUri == null) {
            finish()
            return
        }

        val requestOptions = RequestOptions().diskCacheStrategy(DiskCacheStrategy.NONE).skipMemoryCache(true)
        Glide.with(this)
            .load(imageUri)
            .apply(requestOptions)
            .into(binding.ivCapturedImage)

        imageFile = File(Uri.parse(imageUri).path!!)

//        binding.btnUpload.setOnClickListener {
//            uploadImage()
//        }

    }

    private fun imageToBase64(imageFile: File): String {
        val originalBitmap = BitmapFactory.decodeFile(imageFile.absolutePath)

        val targetWidth = 400
        val scaleFactor = targetWidth.toFloat() / originalBitmap.width.toFloat()
        val targetHeight = (originalBitmap.height * scaleFactor).toInt()

        val resizedBitmap = Bitmap.createScaledBitmap(originalBitmap, targetWidth, targetHeight, true)

        val byteArrayOutputStream = ByteArrayOutputStream()
        resizedBitmap.compress(Bitmap.CompressFormat.JPEG, 25, byteArrayOutputStream)
        val byteArray = byteArrayOutputStream.toByteArray()
        return Base64.encodeToString(byteArray, Base64.DEFAULT)
    }

    fun getAllPlants() {
        val service = RetrofitObject.service
        service
            .getAllPlantsData(1)
            .enqueue(object : Callback<GetAllPlantsResponseBody> {
                override fun onResponse(
                    call: Call<GetAllPlantsResponseBody>,
                    response: Response<GetAllPlantsResponseBody>
                ) {
                    if (response.isSuccessful) {
//                        Log.e("이미지뷰 성공", response.body()!!.toString())
                        allPlantsList = response.body()!!.data
                        setupButtons()
//                        myPlantRVAdapter.plants = allPlantsList
//                        Log.e("식물리스트", allPlantsList.toString())
//                        myPlantRVAdapter.notifyDataSetChanged()
                    }
                }

                override fun onFailure(call: Call<GetAllPlantsResponseBody>, t: Throwable) {
                    Log.e("실패", t.toString())
                }

            })
    }


    fun setupButtons() {
        val titleButton = binding.titleButton
        val memoEditText = binding.memoEditText // 메모 작성 EditText 참조

        val plantNames = allPlantsList.map { it.plantName }

        titleButton.setOnClickListener {
            val items = listOf("전체보기") + plantNames
            showPlantNameBottomDialog("이름 선택", items) { selectedItem ->
                titleButton.text = selectedItem
            }
        }

        binding.btnUpload.setOnClickListener {
            val selectedItem = titleButton.text.toString()
            val selectedPlant = allPlantsList.firstOrNull { it.plantName == selectedItem }
            val plantId = selectedPlant?.plantId
            val plantName = selectedPlant?.plantName

            if (plantId != null && plantName != null) {
                val memoContent = memoEditText.text.toString() // 메모 내용 가져오기
                val base64Image = imageToBase64(imageFile) // 이미지를 base64로 인코딩
                sendPlantDataToApi(plantId, plantName, memoContent, base64Image)
            } else {
                Toast.makeText(this@ImagePreviewActivity, "식물 이름을 선택해 주세요.", Toast.LENGTH_SHORT).show()
            }
        }
    }




    private fun showPlantNameBottomDialog(title: String, plantItems: List<String>, onPlantItemSelected: (String) -> Unit) {
        val dialog = Dialog(this, R.style.BottomDialogAnimation)
        val dialogView = LayoutInflater.from(this).inflate(R.layout.dialog_bottom, null)

        val titleTextView = dialogView.findViewById<TextView>(R.id.dialogTitle)
        titleTextView.text = title

        val listView = dialogView.findViewById<ListView>(R.id.listView)
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, plantItems)
        listView.adapter = adapter

        listView.setOnItemClickListener { _, _, position, _ ->
            onPlantItemSelected(plantItems[position])
            dialog.dismiss()
        }

        dialog.setContentView(dialogView)
        dialog.window?.setGravity(Gravity.BOTTOM)

        // 모달의 배경을 어둡게 처리
        dialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
        val layoutParams = WindowManager.LayoutParams().apply {
            copyFrom(dialog.window?.attributes)
            width = WindowManager.LayoutParams.MATCH_PARENT
            height = WindowManager.LayoutParams.WRAP_CONTENT
            gravity = Gravity.BOTTOM
            dimAmount = 0.5f
            flags = flags or WindowManager.LayoutParams.FLAG_DIM_BEHIND
        }
        dialog.window?.attributes = layoutParams

        // 배경을 클릭하면 모달이 닫히도록 설정
        dialogView.setOnClickListener {
            dialog.dismiss()
        }

        // 리스트뷰의 배경을 투명하게 설정하여 배경 클릭이 가능하게 함
        listView.setBackgroundColor(Color.TRANSPARENT)

        dialog.setOnCancelListener {
            dialog.dismiss()
        }

        // 추가: 배경을 클릭하면 모달이 닫히도록 설정
        dialog.setCanceledOnTouchOutside(true)

        dialog.show()
    }


    private fun sendPlantDataToApi(plantId: Int, plantName: String, memoContent: String, base64Image: String) {
        val service = RetrofitObject.service


        service.createDiary(createDiaryRequestBody(plantId, plantName, memoContent, base64Image)).enqueue(object : Callback<createDiaryResponseBody> {
            override fun onResponse(
                call: Call<createDiaryResponseBody>,
                response: Response<createDiaryResponseBody>
            ) {
//                Toast.makeText(this@ImagePreviewActivity, "생성 완료", Toast.LENGTH_SHORT).show()
                Log.e("base64", base64Image)
                Log.e("plantId", plantId.toString())
                Log.e("plantName", plantName)
                Log.e("memoContent", memoContent)
                Log.e("결과", response.toString())
                val msg = response.body()?.data
                Log.e("메세지", msg.toString())

                if (response.isSuccessful) {
                    Toast.makeText(this@ImagePreviewActivity, "생성 완료2", Toast.LENGTH_SHORT).show()
                    val intent = Intent(this@ImagePreviewActivity, MainActivity::class.java)
                    startActivity(intent)
                } else {
                    Toast.makeText(this@ImagePreviewActivity, "생성에 실패했습니다.", Toast.LENGTH_SHORT).show()
                }
            }

            override fun onFailure(call: Call<createDiaryResponseBody>, t: Throwable) {
                Toast.makeText(this@ImagePreviewActivity, "생성에 실패했습니다2.", Toast.LENGTH_SHORT).show()
            }
        })
    }
}