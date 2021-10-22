package com.example.simpleparadox.listycity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class show_activity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.show_activity);
        Intent intent = getIntent();
        String cityName = intent.getStringExtra("name");

        TextView cityNameText = findViewById(R.id.city_name);
        cityNameText.setText(cityName);

        Button backbutton = findViewById(R.id.back_button);

        backbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(show_activity.this, MainActivity.class));
            }
        });
    }
}
