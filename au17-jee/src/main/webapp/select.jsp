<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Au17 JavaEE Dynamic</title>
</head>
<body>
<form action="select.jsp" method="post">
    <select name="topic" title="topics">
        <c:forEach var="topic" items="${topics}">
            <option value="${topic}">${topic}</option>
        </c:forEach>
    </select>

    <input type="submit"/>
</form>
</body>
</html>
