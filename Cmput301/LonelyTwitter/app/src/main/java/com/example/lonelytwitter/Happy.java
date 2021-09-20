package com.example.lonelytwitter;

import java.util.Date;

public class Happy extends Mood{
    @Override
    public String returnMood() {
        return this.getMood();
    }

    Happy(Date date, String mood) {
        super(date, mood);
    }

    Happy(String mood) {
        super(mood);
    }
}
