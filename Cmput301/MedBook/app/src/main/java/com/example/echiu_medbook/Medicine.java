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
        this.date = "Date: " + date;
        this.name = "Name: " + name;
        this.doseAmount = "Dose: " + doseAmount;
        this.doseUnit = "Unit: "+ doseUnit;
        this.freq = "Freq: " + freq;
    }

    // getters and setters
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

    // Parcelable implementations, generated using the Parcelable addon

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
