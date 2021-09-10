package com.example.lonelytwitter;

import java.util.Date;

public class NormalTweet extends Tweet{

    NormalTweet(Date date, String message) {
        super(date, message);
    }

    NormalTweet(String message) {
        super(message);
    }

    @Override
    public Boolean isImportant() {
        return false;
    }
}
