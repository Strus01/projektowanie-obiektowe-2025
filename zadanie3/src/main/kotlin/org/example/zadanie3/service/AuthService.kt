package org.example.zadanie3.service

import org.springframework.stereotype.Service


@Service
class AuthService {

    private val validDemoUsername = "username"
    private val validDemoPassword = "password"

    fun authenticate(username: String, password: String): Boolean {
        return username == validDemoUsername && password == validDemoPassword
    }
}