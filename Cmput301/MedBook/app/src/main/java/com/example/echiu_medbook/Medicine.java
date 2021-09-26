package com.example.echiu_medbook;

import android.os.Parcel;
import android.os.Parcelable;

import java.util.Date;

public class Medicine implements Parcelable {
    private String date;
    private String name;
    private String doseAmount;
    private String doseUnit;
    private String freq;

    Medicine() {}

    Medicine(String date, String name, String doseAmount, String doseUnit, String freq) {
        this.date = date;
        this.name = name;
        this.doseAmount = doseAmount;
        this.doseUnit = doseUnit;
        this.freq = freq;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDoseAmount() {
        return doseAmount;
    }

    public void setDoseAmount(String doseAmount) {
        this.doseAmount = doseAmount;
    }

    public String getDoseUnit() {
        return doseUnit;
    }

    public void setDoseUnit(String doseUnit) {
        this.doseUnit = doseUnit;
    }

    public String getFreq() {
        return freq;
    }

    public void setFreq(String freq) {
        this.freq = freq;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(this.date);
        dest.writeString(this.name);
        dest.writeString(this.doseAmount);
        dest.writeString(this.doseUnit);
        dest.writeString(this.freq);
    }

    public void readFromParcel(Parcel source) {
        this.date = source.readString();
        this.name = source.readString();
        this.doseAmount = source.readString();
        this.doseUnit = source.readString();
        this.freq = source.readString();
    }

    protected Medicine(Parcel in) {
        this.date = in.readString();
        this.name = in.readString();
        this.doseAmount = in.readString();
        this.doseUnit = in.readString();
        this.freq = in.readString();
    }

    public static final Creator<Medicine> CREATOR = new Creator<Medicine>() {
        @Override
        public Medicine createFromParcel(Parcel source) {
            return new Medicine(source);
        }

        @Override
        public Medicine[] newArray(int size) {
            return new Medicine[size];
        }
    };
}
