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

/* Sources and References used
https://stackoverflow.com/questions/12121214/android-calendarview-how-do-i-get-the-date-in-correct-format/64871776
https://stackoverflow.com/questions/22461258/how-to-get-date-from-calendarview-oncreate-with-a-specific-format-e-g-dd-mm
https://stackoverflow.com/questions/12318791/getintextra-and-putextra/12318896
https://stackoverflow.com/questions/10295226/how-to-create-listview-onitemclicklistener
https://stackoverflow.com/questions/2139134/how-to-send-an-object-from-one-android-activity-to-another-using-intents
https://stackoverflow.com/questions/10407159/how-to-manage-startactivityforresult-on-android
https://stackoverflow.com/questions/7181526/how-can-i-make-my-custom-objects-parcelable
 */


package com.example.echiu_medbook;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    // declare variables
    ListView medView;
    ArrayAdapter<Medicine> medAdapter;
    ArrayList<Medicine> medList; //list of medicines
    TextView dailyDoseView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // initialize listview of medicines
        medView = (ListView) findViewById(R.id.med_view);
        medList = new ArrayList<>();
        medAdapter = new CustomList(this, medList);
        medView.setAdapter(medAdapter);

        // when medicine is selected start new activity to edit it
        medView.setOnItemClickListener(new android.widget.AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Medicine medicine = (Medicine) medView.getItemAtPosition(position); // get selected medicine
                Intent intent = new Intent(getApplicationContext(), EditMedicineActivity.class);
                intent.putExtra("selectedMed", medicine);
                intent.putExtra("position", position); //pass in position in case medicine is to be edited/deleted
                startActivityForResult(intent, 1); // start activity with selected medicine passed in
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        dailyDoseView = (TextView) findViewById(R.id.daily_doses_text);
        if (resultCode == RESULT_OK) { // if data was sent over make a new class with it
            Medicine newMedicine = (Medicine) data.getParcelableExtra("newMed");
            if (newMedicine != null) { // if new medicine was sent over add to list
                medAdapter.add(newMedicine);
            }
            Medicine editMedicine = (Medicine) data.getParcelableExtra("editMed");
            int position = (int) data.getIntExtra("position", 0);
            if (editMedicine != null) { // otherwise get edited medicine and replace
                medList.set(position, editMedicine); // insert edited medicine
                medAdapter.notifyDataSetChanged();
            }
        } else if (resultCode == RESULT_CANCELED) {// otherwise that means they cancelled or deleted
            String delete = (String) data.getStringExtra("delete");
            int position = (int) data.getIntExtra("position", 0);
            if (delete != null) { // if delete then delete
                medList.remove(position);
                medAdapter.notifyDataSetChanged();
            }
        } // otherwise it is a cancel
        // update dailydoses
        int doseInt = 0;
        for (int i = 0; i < medList.size(); i++) {
            doseInt = doseInt + Integer.parseInt(medList.get(i).getFreq().replace("Freq: ", ""));
        }
        String dailyDoses = String.valueOf(doseInt);
        dailyDoseView.setText("Total Daily Doses: " + dailyDoses);
    }

    @Override
    public void onBackPressed() { // override device back button
        moveTaskToBack(true);
    }

    // function to add medicine, called by button press
    public void addMedicine(View view) {
        Intent intent = new Intent(this, AddMedicineActivity.class); // pass medicine in
        startActivityForResult(intent,1);
    }
}