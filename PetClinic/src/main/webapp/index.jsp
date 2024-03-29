<%@ page language="java" import="java.util.ResourceBundle" %>
<%
    try {
        ResourceBundle resource = ResourceBundle.getBundle("petclinic");
        String title = resource.getString("title");
    } catch (Exception e) {
    }
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" href="styles/petclinic.css" type="text/css"/>
    <title>PetClinic :: a Spring Framework demonstration</title>
</head>

<body>

<div id="main">
    <img src="/petclinic/images/pets.png" align="right" style="position:relative;right:30px;">

    <p>&nbsp;</p>

    <p> -- {{TITLE}} -- </p>
    <ul>
        <li><a href="/petclinic/findOwners.jsp">Find owner</a></li>
        <li><a href="/petclinic/vets.jsp">Display all veterinarians</a></li>
        <li><a href="/petclinic/petclinic.html">Tutorial</a></li>
    </ul>
    <p>&nbsp;</p>

    <table class="footer">
        <tr>
            <td><a href="/petclinic/index.html">Home</a></td>
            <td align="right"><img src="/petclinic/images/springsource-logo.png"></td>
        </tr>
    </table>

</div>
</body>

</html>

