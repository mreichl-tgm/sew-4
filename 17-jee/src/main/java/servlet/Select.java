/**
 * @author Markus Reichl
 * @version 29.05.2017
 */

package main.java.servlet;

import main.java.model.Bundesland;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Select extends HttpServlet {
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        ArrayList<String> topics = new ArrayList<>();
        topics.add("Alle Hauptstädte");
        topics.add("Alle Bundesländer");
        topics.add("Ein Bundesland");
        topics.add("Eine Hauptstadt");

        HashMap<String, Bundesland> states = new HashMap<>();
        states.put("O", new Bundesland("Oberösterreich", "Linz"));
        states.put("W", new Bundesland("Wien", "Wien"));
        states.put("N", new Bundesland("Niederösterreich", "St. Pölten"));
        states.put("ST", new Bundesland("Steiermark", "Graz"));
        states.put("V", new Bundesland("Vorarlberg", "Bregenz"));
        states.put("SA", new Bundesland("Salzburg", "Salzburg"));
        states.put("K", new Bundesland("Kärnten", "Klagenfurt"));
        states.put("T", new Bundesland("Tirol", "Innsbruck"));
        states.put("B", new Bundesland("Burgenland", "Eisenstadt"));

        for (Map.Entry state : states.entrySet()) {
            state.getKey();
        }

        request.setAttribute("topics", topics);
        request.setAttribute("states", states);
        request.getRequestDispatcher("select.jsp").forward(request, response);
    }
}
