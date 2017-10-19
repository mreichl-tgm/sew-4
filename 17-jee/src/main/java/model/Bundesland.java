/**
 * @author Markus Reichl
 * @version 29.05.2017
 */

package main.java.model;


import java.io.Serializable;

public class Bundesland implements Serializable {
    private String name;
    private String capital;

    public Bundesland(String name, String capital) {
        this.name = name;
        this.capital = capital;
    }

    public String getName() { return name; }
    public String getCapital() { return capital; }
}
