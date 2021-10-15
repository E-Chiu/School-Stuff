package com.example.lab6;

/**
 * This class represents a city
 * @author Ethan
 * @version 1.0
 */

public class City implements Comparable<City>{
    /**
     * This variable contains te name of the city
     * This var is of type {@link String}
     */
    private String cityName;
    /**
     * This variable contains te name of the province for the city
     * This var is of type {@link String}
     */
    private String provinceName;

    /**
     *
     * @param cityName
     * Give name of the city, which should be of type {@link String}
     * @param provinceName
     * Give name of the province, which should be of type {@link String}
     */
    public City(String cityName, String provinceName) {
        this.cityName = cityName;
        this.provinceName = provinceName;
    }

    /**
     * This function returns {@link City#cityName}
     * @return
     * The return type is {@link String}
     */
    public String getCityName() {
        return cityName;
    }

    @Override
    public int compareTo(City city) {
        return cityName.compareTo(city.getCityName());
    }
}
