package com.gaggum

import android.annotation.SuppressLint
import android.os.Bundle
import android.os.Handler
import android.view.LayoutInflater
import android.view.MotionEvent
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.gaggum.R
import io.socket.client.IO
import io.socket.client.Socket
import com.gaggum.databinding.FragmentRegisterBinding

class RegisterFragment : Fragment() {
    private lateinit var binding: FragmentRegisterBinding
    private lateinit var socket: Socket
    private val handler = Handler()

    private var upKeyDown = false
    private var downKeyDown = false
    private var leftKeyDown = false
    private var rightKeyDown = false

    private val repeatUpdateRunnable = object : Runnable {
        override fun run() {
            if (upKeyDown) logKeyDown("straight", 2)
            if (downKeyDown) logKeyDown("back", 3)
            if (leftKeyDown) logKeyDown("left", 1)
            if (rightKeyDown) logKeyDown("right", 4)

            handler.postDelayed(this, 100)
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentRegisterBinding.inflate(inflater, container, false)
        return binding.root
    }

    @SuppressLint("ClickableViewAccessibility")
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        connectSocketIO()

        val upArrow = binding.arrowUp
        val downArrow = binding.arrowDown
        val leftArrow = binding.arrowLeft
        val rightArrow = binding.arrowRight

        upArrow.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> upKeyDown = true
                MotionEvent.ACTION_UP -> upKeyDown = false
            }
            true
        }

        downArrow.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> downKeyDown = true
                MotionEvent.ACTION_UP -> downKeyDown = false
            }
            true
        }

        leftArrow.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> leftKeyDown = true
                MotionEvent.ACTION_UP -> leftKeyDown = false
            }
            true
        }

        rightArrow.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> rightKeyDown = true
                MotionEvent.ACTION_UP -> rightKeyDown = false
            }
            true
        }

        handler.post(repeatUpdateRunnable)
    }

    private fun connectSocketIO() {
        socket = IO.socket("http://192.168.1.72:3001")
        socket.connect()
    }

    private fun logKeyDown(direction: String, number: Int) {
        if (socket.connected()) {
//            socket.emit("go_$direction", mapOf("name" to "go $direction", "data" to number))
            socket.emit("connectReceive", mapOf("name" to "go $direction", "data" to number))

        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        handler.removeCallbacks(repeatUpdateRunnable)
        socket.disconnect()
    }
}
