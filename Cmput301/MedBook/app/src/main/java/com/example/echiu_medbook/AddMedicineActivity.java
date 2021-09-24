package com.example.echiu_medbook;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class AddMedicineActivity extends AppCompatActivity {
    String[] doseTypes = new String[] {"mg", "mcg", "drop"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_medicine);

        Spinner doseType = (Spinner) findViewById(R.id.dose_unit_dropdown);
        ArrayAdapter units = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, doseTypes);
        units.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        doseType.setAdapter(units);
    }

    public void cancel(View view) { // finish activity without doing anything
        super.finish();
    }

    public void add(View view) {
    // first ensure that all entries are correct

    }
}