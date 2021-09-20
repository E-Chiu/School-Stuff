package com.example.lonelytwitter;

import java.util.Date;

public abstract class Mood {

    public abstract String returnMood();

    private Date date;
    private String mood;

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
        this.mood = mood;
    }

    Mood(Date date, String mood) {
        this.date = date;
        this.mood = mood;
    }

    public String getMood() {
        return mood;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }

    Mood(String mood) {
        this.date = new Date();
        this.mood = mood;
    }

}
