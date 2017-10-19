package main.java.model;

import java.io.Serializable;

/**
 * @author Markus Reichl
 * @version 31.05.2017
 *
 * Model class for the temperature converter holding units and conversions.
 */

public class ConverterModel implements Serializable {
    private double convert;
    private double converted;
    private boolean initial;
    private String unit;

    public double getConvert() { return convert; }

    public void setConvert(double convert) { this.convert = convert; }

    public double getConverted() { return converted; }

    public boolean getInitial() { return initial; }

    public String getUnit() { return unit; }

    private void init(){
        initial = true;
        converted = 0;
        convert = 0;
        unit="";
    }

    /**
     * Calls init() method and returns "reset"
     * @return "reset"
     */
    public String reset() {
        init();
        return "reset";
    }

    public void celsiusToFahrenheit() {
        this.initial = false;
        this.unit="Fahrenheit";
        this.converted = (convert * 1.8) + 32;
    }

    public void celsiusToKelvin() {
        this.initial = false;
        this.unit="Kelvin";
        this.converted = convert + 273.15;
    }

    public void kelvinToCelsius() {
        this.initial = false;
        this.unit="Celsius";
        this.converted = convert - 273.15;
    }

    public void kelvinToFahrenheit() {
        this.initial = false;
        this.unit="Fahrenheit";
        this.converted = (convert * 1.8) - 459.67;
    }

    public void fahrenheitToKelvin() {
        this.initial = false;
        this.unit="Kelvin";
        this.converted = (convert + 459.67) / 1.8;
    }

    public void fahrenheitToCelsius() {
        this.initial = false;
        this.unit="Celsius";
        this.converted = (convert - 32)/ 1.8;
    }
}