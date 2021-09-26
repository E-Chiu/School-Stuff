package com.example.echiu_medbook;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.Nullable;

import java.util.ArrayList;

public class CustomList extends ArrayAdapter<Medicine> {
    private ArrayList<Medicine> medicines;
    private Context context;

    public CustomList (Context context, ArrayList<Medicine> medicines) {
        super(context, 0, medicines);
        this.medicines = medicines;
        this.context = context;
    }

    public View getView(int position, @Nullable View convertView, @Nullable ViewGroup parent) {
        View view = convertView;
        if(view == null) {
            view = LayoutInflater.from(context).inflate(R.layout.content, parent, false);
        }
        Medicine medicine = medicines.get(position);
        TextView medName = view.findViewById(R.id.name_text);
        TextView medDate = view.findViewById(R.id.date_text);
        TextView medDose = view.findViewById(R.id.dose_text);
        TextView medUnit = view.findViewById(R.id.unit_text);
        TextView medFreq = view.findViewById(R.id.freq_text);

        medName.setText(medicine.getName());
        medDate.setText(medicine.getDate());
        medDose.setText(medicine.getDoseAmount());
        medUnit.setText(medicine.getDoseUnit());
        medFreq.setText(medicine.getFreq());
        return view;
    }
}
