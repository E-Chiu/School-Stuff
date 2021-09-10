package com.example.lonelytwitter;

import java.util.Date;

public abstract class Tweet implements Tweetable {

    public abstract Boolean isImportant();

    private Date date;
    private String message;

    Tweet(Date date, String message) {
        this.date = date;
        this.message = message;
    }

    Tweet(String message) {
        this.date = new Date();
        this.message = message;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
