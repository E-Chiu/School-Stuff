package com.example.lab6;


import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

public class TestCityList {
    private CityList cityList = new CityList();
    private City city = new City("Edmonton", "Alberta");
    private City tempCity = new City("Edmonton", "Ontario");

    @BeforeEach
    void mockCityList() {
        cityList.addCity(city);
    }

    @Tag("fast")
    @Test
    @DisplayName("Test to check Add city function")
    void testAddCity() {
        assertThrows(IllegalArgumentException.class,
                ()->{cityList.addCity(city);});
    }

    @Test
    void testGetCities() {
            assertAll("Mock Checkup",
                    ()->assertNotEquals(2, cityList.getCities().size()),
                    ()->assertEquals(1, cityList.getCities().size()),
                    ()->assertEquals("Edmonton", cityList.getCities().get(0).getCityName())
            );
    }

    @Test
    void testHasCity() {
        assertAll("Mock Checkup",
                ()->assertEquals(true, cityList.hasCity(city)),
                ()->assertEquals(false, cityList.hasCity(tempCity))
                );
    }

    @Test
    void testDelete() {
        assertThrows(IllegalArgumentException.class,
                ()->{cityList.delete(tempCity);});
    }

    @Test
    void testCountCities() {
        assertEquals(1, cityList.countCities());
    }

    @AfterEach
    void runAfterTestCase() {

    }
}
