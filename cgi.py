import cgi, cgitb

form = cgi.FieldStorage()

f_name = form.getvalue("f_name")
l_name = form.getvalue("l_name")

print("CONTENT-TYPE=text/html")
print()
print("<html>")
print("<head>")
print("<title> My new cgi </title>")
print("<body>")
print("<h1>Hello  %s  %s" %(f_name, l_name))
print("</body>")
print("</html>")