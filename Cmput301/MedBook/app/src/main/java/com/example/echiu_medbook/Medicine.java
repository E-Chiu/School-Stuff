package com.example.echiu_medbook;

import java.util.Date;

public class Medicine {
    private Date date;
    private String name;
    private int doseAmount;
    private String doseUnit;
    private int freq;

    Medicine() {}

    Medicine(Date date, String name, int doseAmount, String doseUnit, int freq) {
        this.date = date;
        this.name = name;
        this.doseAmount = doseAmount;
        this.doseUnit = doseUnit;
        this.freq = freq;
    }
}
