package com.example.echiu_medbook;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    // declare variables
    ListView medView;
    ArrayAdapter<Medicine> medAdapter;
    ArrayList<Medicine> medList; //list of medicines

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // initialize listview of medicines
        medView = findViewById(R.id.med_view);
        /*
        medList = new ArrayList<>();
        medAdapter = new ArrayAdapter<>(this, R.layout.content, medList);
        medView.setAdapter(medAdapter);
        */
    }

    // function to add medicine, called by button press
    public void addMedicine(View view) {
        Intent intent = new Intent(this, AddMedicineActivity.class);
        startActivity(intent);
    }
}