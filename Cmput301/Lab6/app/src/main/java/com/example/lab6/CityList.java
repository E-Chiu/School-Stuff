package com.example.lab6;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * This class contains list of cities belonging to class {@link City}
 */
public class CityList {
    private List<City> cities = new ArrayList<>();

    /**
     * This functions add a new city into the list
     * @param city
     * Takes input a new city of type {@link City}
     * @throws IllegalArgumentException
     * This function can also throw Exception {@link IllegalArgumentException}
     */
    public void addCity(City city) {
        if (cities.contains(city))
            throw new IllegalArgumentException();
        cities.add(city);
    }

    public List<City> getCities() {
        List<City> tmpList = cities;
        Collections.sort(tmpList);
        return tmpList;
    }
}
