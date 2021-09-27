/*
    Copyright [2021] [Ethan Chiu]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
 */
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
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class EditMedicineActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    String[] doseTypes = new String[] {"mg", "mcg", "drop"};
    ArrayAdapter<String> units;
    String selectedDate;
    Intent intent;
    Medicine medicine;
    int position;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_medicine);

        intent = getIntent();
        medicine = intent.getParcelableExtra("selectedMed");
        position = intent.getIntExtra("position", 0);

        Spinner doseType = (Spinner) findViewById(R.id.dose_unit_dropdown);
        units = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, doseTypes);
        units.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        doseType.setAdapter(units);

        // set fields to be current attributes of the selected medicine
        // remove all attribute names
        EditText medName = (EditText) findViewById(R.id.set_name_box);
        medName.setText(medicine.getName().replace("Name: ", ""));
        EditText medDose = (EditText) findViewById(R.id.set_dose_box);
        medDose.setText(medicine.getDoseAmount().replace("Dose: ", ""));
        EditText medFreq = (EditText) findViewById(R.id.set_frequency_box);
        medFreq.setText(medicine.getFreq().replace("Freq: ", ""));

        CalendarView medDate = (CalendarView) findViewById(R.id.medDate);

        // set calendar view to current date
        String dateSplit[] = medicine.getDate().replace("Date: ", "").split("/");
        int day = Integer.parseInt(dateSplit[0]);
        int month = Integer.parseInt(dateSplit[1]);
        int year = Integer.parseInt(dateSplit[2]);
        Calendar calendar = Calendar.getInstance();
        calendar.set(calendar.YEAR, year);
        calendar.set(calendar.MONTH, month - 1);
        calendar.set(calendar.DAY_OF_MONTH, day);
        long milliTime = calendar.getTimeInMillis();
        medDate.setDate(milliTime, true, true);

        // set selected date
        selectedDate = medicine.getDate().replace("Date: ", "");
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        medDate.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDayChange(CalendarView view, int year, int month, int day) {
                String sDay = String.valueOf(day);
                String sMonth = String.valueOf(month + 1);
                String sYear = String.valueOf(year);
                selectedDate = sDay + "/" + sMonth + "/" + sYear; // concatenate into a dd/mm/yyyy format

            }
        });
    }

    public void onItemSelected(AdapterView<?> parent, View view, int pos, long id) {
        Spinner doseType = (Spinner) findViewById(R.id.dose_unit_dropdown); // if new unit is selected get that
        units.notifyDataSetChanged();
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }

    public void cancel(View view) { // finish activity without doing anything
        Intent fodder = new Intent();
        setResult(RESULT_CANCELED, fodder);
        super.finish();
    }

    public void delete(View view) { // say you wish to delete this activity
        Intent returnVals = new Intent();
        returnVals.putExtra("delete", "y"); // send message that they wish to delete this
        returnVals.putExtra("position", position);
        setResult(RESULT_CANCELED, returnVals);
        super.finish();
    }

    @Override
    public void onBackPressed() { // override device back button
        moveTaskToBack(true);
    }

    public void edit(@NonNull View view) {
        EditText medName = (EditText) findViewById(R.id.set_name_box);
        EditText medDose = (EditText) findViewById(R.id.set_dose_box);
        Spinner medUnit = (Spinner) findViewById(R.id.dose_unit_dropdown);
        EditText medFreq = (EditText) findViewById(R.id.set_frequency_box);
        // get all values
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
        // edit medicine class
        Medicine editMedicine = new Medicine(selectedDate, name, doseString, unit, freqString);
        Intent returnVals = new Intent(this, EditMedicineActivity.class);
        returnVals.putExtra("editMed", editMedicine); // return edited medicine
        returnVals.putExtra("position", position);
        setResult(RESULT_OK, returnVals);
        finish();
    }
}