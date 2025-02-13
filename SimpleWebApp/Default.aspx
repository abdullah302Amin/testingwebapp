<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="SimpleWebApp._Default" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Simple Web App</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="lblMessage" runat="server" Text="Welcome to ASP.NET 4.8!"></asp:Label>
            <br />
            <asp:Button ID="btnClickMe" runat="server" Text="Click Me!" OnClick="btnClickMe_Click" />
        </div>
    </form>
</body>
</html>
