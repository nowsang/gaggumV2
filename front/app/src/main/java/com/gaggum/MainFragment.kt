package com.gaggum

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class MainFragment : Fragment() {
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_main, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        /* 로그아웃 */
        val logoutBtn = view.findViewById<Button>(R.id.logoutBtn)
        logoutBtn.setOnClickListener {
            Firebase.auth.signOut()
            val intent = Intent(requireActivity(), SigninActivity::class.java)
            startActivity(intent)
        }

        /* 날씨 API */
        val OPEN_WEATHER_MAP_API_KEY = "be002738467412a6651e4278dd3f8c76"
        val OPEN_WEATHER_MAP_BASE_URL = "http://api.openweathermap.org/data/2.5/"
    }
}
