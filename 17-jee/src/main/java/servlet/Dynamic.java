/**
 * @author Markus Reichl
 * @version 29.05.2017
 */

package main.java.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Dynamic extends HttpServlet {
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {
        Calendar cal = Calendar.getInstance();
        SimpleDateFormat timeFormat = new SimpleDateFormat("hh:mm");
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd.MM.yy");

        request.setAttribute("time", timeFormat.format(cal.getTime()));
        request.setAttribute("date", dateFormat.format(cal.getTime()));
        request.getRequestDispatcher("/dynamic.jsp").forward(request, response);
    }
}
