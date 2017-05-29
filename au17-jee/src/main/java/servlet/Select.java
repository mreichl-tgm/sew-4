package main.java.servlet;

import main.java.model.Bundesland;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.ArrayList;

public class Select extends HttpServlet {
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        ArrayList<String> topics = new ArrayList<>();
        topics.add("Alle Hauptstädte");
        topics.add("Alle Bundesländer");
        topics.add("Ein Bundesland");
        topics.add("Eine Hauptstadt");

        ArrayList<Bundesland> states = new ArrayList<>();
        states.add(new Bundesland("Oberösterreich", "Linz"));
        states.add(new Bundesland("Wien", "Wien"));
        states.add(new Bundesland("Niederösterreich", "St. Pölten"));
        states.add(new Bundesland("Steiermark", "Graz"));
        states.add(new Bundesland("Vorarlberg", "Bregenz"));
        states.add(new Bundesland("Salzburg", "Salzburg"));
        states.add(new Bundesland("Kärnten", "Klagenfurt"));
        states.add(new Bundesland("Tirol", "Innsbruck"));
        states.add(new Bundesland("Burgenland", "Eisenstadt"));

        request.setAttribute("topics", topics);
        request.setAttribute("states", states);
        request.getRequestDispatcher("/select.jsp").forward(request, response);
    }
}
