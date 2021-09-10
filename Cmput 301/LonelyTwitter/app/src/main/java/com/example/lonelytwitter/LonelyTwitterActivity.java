package com.example.lonelytwitter;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class LonelyTwitterActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lonely_twitter);

        Tweet tweet  = new Tweet("This is a regular tweet!") {
            @Override
            public Boolean isImportant() {
                return true;
            }
        };
    }
}