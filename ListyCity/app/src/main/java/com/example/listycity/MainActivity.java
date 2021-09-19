package com.example.listycity;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {
//variables
    ListView cityView;
    ArrayAdapter<String> cityAdapter;
    ArrayList<String> dataList;
    public static int toDel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cityView = findViewById(R.id.list_view);

        cityView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long l) {
                toDel = position;
            }
        });

        //create a string array
        String []cities ={"Edmonton", "Calgary", "Berlin", "Tokyo", "Beijing", "Toronto", "Montreal"};
        dataList= new ArrayList<>();
        dataList.addAll(Arrays.asList(cities));

        cityAdapter= new ArrayAdapter<>(this, R.layout.content, dataList);
        cityView.setAdapter(cityAdapter);
    }

    // add city to list
    public void addCity(View view) {
        EditText editText = (EditText) findViewById(R.id.add_City);
        String toAdd = editText.getText().toString();
        dataList.add(toAdd);
        cityAdapter.notifyDataSetChanged();
    }

    public void removeCity(View view) {
        ListView listView = (ListView) findViewById(R.id.list_view);
        dataList.remove(toDel);
        cityAdapter.notifyDataSetChanged();
    }
}