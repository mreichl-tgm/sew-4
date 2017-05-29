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
    <c:set var="chosenState" value="<%= request.getParameter("singleState")%>"/>
    <c:set var="chosenCapital" value="<%= request.getParameter("singleCapital")%>"/>
    <!-- Alle Hauptstädte -->
    <c:if test='${chosenTopic == "Alle Hauptstädte"}'>
        <h2>Alle Hauptstädte</h2>
        <ul>
            <c:forEach var="state" items="${states.values()}">
                <li>${state.getCapital()}</li>
            </c:forEach>
        </ul>
    </c:if>
    <!-- Alle Bundesländer -->
    <c:if test='${chosenTopic == "Alle Bundesländer"}'>
        <h2>Alle Hauptstädte</h2>
        <ul>
            <c:forEach var="state" items="${states.values()}">
                <li>${state.getName()}</li>
            </c:forEach>
        </ul>
    </c:if>
    <!-- Ein Bundesland -->
    <c:if test='${chosenTopic == "Ein Bundesland" || chosenState != null}'>
        <h2>Ein Bundesland</h2>
        <form action="select" method="get">
            <select name="singleState" title="singleState">
                <c:forEach var="state" items="${states.entrySet()}">
                    <option value="${state.getKey()}">${state.getValue().getName()}</option>
                </c:forEach>
            </select>

            <input type="submit"/>
        </form>

        <c:if test='${chosenState != null}'>
            <p>${states.get(chosenState).getName()}'s capital is ${states.get(chosenState).getCapital()}</p>
        </c:if>
    </c:if>
    <!-- Eine Hauptstadt -->
    <c:if test='${chosenTopic == "Eine Hauptstadt" || chosenCapital != null}'>
        <h2>Eine Hauptstadt</h2>
        <form action="select" method="get">
            <select name="singleCapital" title="singleCapital">
                <c:forEach var="state" items="${states.entrySet()}">
                    <option value="${state.getKey()}">${state.getValue().getCapital()}</option>
                </c:forEach>
            </select>

            <input type="submit"/>
        </form>

        <c:if test='${chosenCapital != null}'>
            <p>${states.get(chosenCapital).getCapital()} is the capital of ${states.get(chosenCapital).getName()}</p>
        </c:if>
    </c:if>
</main>
</body>
</html>
