package org.example.zadanie3.controller

import org.example.zadanie3.service.AuthService
import org.example.zadanie3.dto.User
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/auth")
class AuthController @Autowired constructor(private val authService: AuthService) {

    @PostMapping("/login")
    fun authenticate(@RequestBody request: User): ResponseEntity<Map<String, Any>> {
        val isAuthenticated = authService.authenticate(request.username, request.password)
        val response = mapOf(
            "username" to request.username,
            "authenticated" to isAuthenticated
        )
        return if (isAuthenticated) {
            ResponseEntity.ok(response)
        } else {
            ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(response)
        }
    }

    @GetMapping("/data")
    fun getData(): Map<String, String> {
        return mapOf(
            "Data 1" to "Demo", "Data 2" to "Demo", "Data 3" to "Demo"
        )
    }
}
