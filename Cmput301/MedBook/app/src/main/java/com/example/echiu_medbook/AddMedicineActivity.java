package com.example.echiu_medbook;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.CalendarView;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class AddMedicineActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    String[] doseTypes = new String[] {"mg", "mcg", "drop"};
    ArrayAdapter<String> units;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_medicine);

        Spinner doseType = (Spinner) findViewById(R.id.dose_unit_dropdown);
        units = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, doseTypes);
        units.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        doseType.setAdapter(units);
    }

    public void onItemSelected(AdapterView<?> parent, View view, int pos, long id) {
        Spinner doseType = (Spinner) findViewById(R.id.dose_unit_dropdown);
        units.notifyDataSetChanged();
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }

    public void cancel(View view) { // finish activity without doing anything
        setResult(RESULT_CANCELED);
        super.finish();
    }

    public void add(@NonNull View view) {
        // get all values
        CalendarView medDate = (CalendarView) findViewById(R.id.medDate);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        String selectedDate = sdf.format(new Date(medDate.getDate()));
        EditText medName = (EditText) findViewById(R.id.set_name_box);
        EditText medDose = (EditText) findViewById(R.id.set_dose_box);
        Spinner medUnit = (Spinner) findViewById(R.id.dose_unit_dropdown);
        EditText medFreq = (EditText) findViewById(R.id.set_frequency_box);
        String name = medName.getText().toString();
        String doseString = medDose.getText().toString();
        String unit = medUnit.getItemAtPosition(medUnit.getSelectedItemPosition()).toString();
        String freqString = medFreq.getText().toString();
        // ensure that all entries are correct
        if (doseString.matches("") || freqString.matches("") || name.matches("")) {
            Toast.makeText(this, "You left some fields blank!", Toast.LENGTH_SHORT).show();
            return;
        } else if (!doseString.matches("\\d+") || !freqString.matches("\\d+")) {
            Toast.makeText(this, "Please enter digits where they are needed!", Toast.LENGTH_SHORT).show();
            return;
        }
        int dose = Integer.parseInt(doseString);
        int freq = Integer.parseInt(freqString);
        if (dose <= 0 || freq <= 0) {
            Toast.makeText(this, "Please enter a positive number!", Toast.LENGTH_SHORT).show();
            return;
        }
        // add to new medicine class
        Medicine newMedicine = new Medicine(selectedDate, name, doseString, unit, freqString);
        Intent returnVals = new Intent(this, AddMedicineActivity.class);
        returnVals.putExtra("newMed", newMedicine);
        setResult(RESULT_OK, returnVals);
        finish();
    }
}