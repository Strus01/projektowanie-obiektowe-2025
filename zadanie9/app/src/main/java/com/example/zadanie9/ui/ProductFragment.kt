package com.example.zadanie9.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.zadanie9.viewmodel.MainViewModel


class ProductFragment : Fragment() {

    private lateinit var viewModel: MainViewModel

    companion object {
        fun newInstance(categoryId: Int): ProductFragment {
            val fragment = ProductFragment()
            val bundle = Bundle()
            bundle.putInt("category_id", categoryId)
            fragment.arguments = bundle
            return fragment
        }
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        val categoryId = arguments?.getInt("category_id") ?: 0
        val recyclerView = RecyclerView(requireContext())
        recyclerView.layoutManager = LinearLayoutManager(requireContext())

        viewModel = ViewModelProvider(requireActivity())[MainViewModel::class.java]
        val filtered = viewModel.getProductsByCategory(categoryId)

        recyclerView.adapter = ProductAdapter(filtered)

        return recyclerView
    }
}