package com.example.echiu_medbook;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class AddMedicineActivity extends AppCompatActivity {
    String[] doseType = {"mg", "mcg", "drop"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_medicine);

        Spinner doseType = (Spinner) findViewById(R.id.dose_unit_dropdown);
        ArrayAdapter<String> units = new ArrayAdapter(this, android.R.layout.simple_spinner_item, doseType);

    }

    public void cancel(View view) { // finish activity without doing anything
        super.finish();
    }

    public void add(View view) {
    // first ensure that all entries are correct

    }
}