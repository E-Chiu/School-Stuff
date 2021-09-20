package com.example.lonelytwitter;

import java.util.Date;

public class Sad extends Mood {
    @Override
    public String returnMood() {
        return this.getMood();
    }

    Sad(Date date, String mood) {
        super(date, mood);
    }

    Sad(String mood) {
        super(mood);
    }
}
