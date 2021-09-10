package com.example.lonelytwitter;

import java.util.Date;

public class ImportantTweet extends Tweet{
    @Override
    public Boolean isImportant() {
        return true;
    }

    ImportantTweet(Date date, String message) {
        super(date, message);
    }

    ImportantTweet(String message) {
        super(message);
    }
}
