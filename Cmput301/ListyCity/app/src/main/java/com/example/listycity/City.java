package com.example.listycity;

public class City {
    private String city;
    private String province;

    public String getCityName() {
        return city;
    }

    public String getProvinceName() {
        return province;
    }

    City(String city, String province) {
        this.city = city;
        this.province = province;
    }
}
