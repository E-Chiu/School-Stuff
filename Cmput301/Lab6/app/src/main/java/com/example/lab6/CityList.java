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
     * This function adds a new city into the list
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

    /**
     * This function checks to see if a city is in the list
     * @param city
     * Takes input a new city of type {@link City}
     * @return
     * the return type is {@link boolean}
     */
    public boolean hasCity(City city) {
        if (cities.contains(city)) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * This function deletes a city from the list
     * @param city
     * Takes input a new city of type {@link City}
     * @throws IllegalArgumentException
     * This function can also throw Exception {@link IllegalArgumentException}
     */
    public void delete(City city) {
        if (hasCity(city)) {
            cities.remove(city);
        } else {
            throw new IllegalArgumentException();
        }
    }


    /**
     * This function returns the number of items in the list
     * @return
     * The retun type is {@link int}
     */
    public int countCities() {
        return cities.size();
    }
}
