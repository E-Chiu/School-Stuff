package com.example.echiu_medbook;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.ArrayAdapter;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    // declare variables
    RecyclerView medView;
    ArrayAdapter<Medicine> medAdapter;
    ArrayList<Medicine> medList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        medView = findViewById(R.id.med_View);
        Medicine []medicines ={}; // list of medicines
        medList = new ArrayAdapter<>(this, R.layout.content, medList);
        medView.setAdapter(medAdapter);
    }
}