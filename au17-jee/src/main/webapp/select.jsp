<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Au17 JavaEE Dynamic</title>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
<header>
    <h1>Politische Bildung</h1>
    <p>Auswahl</p>
    <form action="select" method="get">
        <select name="topic" title="topics">
            <c:forEach var="topic" items="${topics}">
                <option value="${topic}">${topic}</option>
            </c:forEach>
        </select>

        <input type="submit"/>
    </form>
</header>

<main>
    <c:set var="chosenTopic" value="<%= request.getParameter("topic")%>"/>
    <!-- Alle Hauptstädte -->
    <c:if test='${chosenTopic == "Alle Hauptstädte"}'>
        <h2>Alle Hauptstädte</h2>
        <ul>
            <c:forEach var="state" items="${states}">
                <li>${state.getCapital()}</li>
            </c:forEach>
        </ul>
    </c:if>
    <!-- Alle Bundesländer -->
    <c:if test='${chosenTopic == "Alle Bundesländer"}'>
        <h2>Alle Hauptstädte</h2>
        <ul>
            <c:forEach var="state" items="${states}">
                <li>${state.getName()}</li>
            </c:forEach>
        </ul>
    </c:if>
</main>
</body>
</html>
