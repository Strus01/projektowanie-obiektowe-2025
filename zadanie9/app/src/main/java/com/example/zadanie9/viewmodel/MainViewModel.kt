package com.example.zadanie9.viewmodel

import androidx.lifecycle.ViewModel
import com.example.zadanie9.data.Category
import com.example.zadanie9.data.Product


class MainViewModel : ViewModel() {
    val categories = listOf(
        Category(1, "Category 1"),
        Category(2, "Category 2"),
        Category(3, "Category 3")
    )

    val products = listOf(
        Product(1, "Product 1", 1),
        Product(2, "Product 2", 1),
        Product(3, "Product 3", 1),
        Product(4, "Product 1", 2),
        Product(5, "Product 2", 2),
        Product(6, "Product 1", 3),
        Product(7, "Product 2", 3)
    )

    fun getProductsByCategory(categoryId: Int): List<Product> {
        return products.filter { it.categoryId == categoryId }
    }
}