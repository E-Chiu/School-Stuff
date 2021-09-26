package com.example.echiu_medbook;

import androidx.annotation.Nullable;
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
        medView = (ListView) findViewById(R.id.med_view);
        medList = new ArrayList<>();
        medAdapter = new CustomList(this, medList);
        medView.setAdapter(medAdapter);

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode == RESULT_OK) { // if data was sent over make a new class with it
            Medicine newMedicine = (Medicine) data.getParcelableExtra("newMed");
            medAdapter.add(newMedicine);
        }
    }

    // function to add medicine, called by button press
    public void addMedicine(View view) {
        Intent intent = new Intent(this, AddMedicineActivity.class);
        startActivityForResult(intent,1);
    }
}