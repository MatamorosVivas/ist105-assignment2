import cgi
import math

form = cgi.FieldStorage()

a = float(form.getvalue("a"))
b = float(form.getvalue("b"))
c = float(form.getvalue("c"))

cCubed = c ** 3
squareRoot = math.sqrt(cCubed)
division = squareRoot / a
multiplication = division * 10
result = b + multiplication

print("Content-Type: text/html\n")
print("""
<html>
<head>
<title>Assignment 2 Result</title>
</head>
<body>
<span>Assignment #2</span>
Carlos_MatamorosVivas

<div>
Step 1: c = {:.1f} , c³ = {:.1f}
Step 2: √(c³) = {:.1f}
Step 3: {:.1f} / {:.1f} = {:.1f}
Step 4: {:.1f} * 10 = {:.1f}
Step 5: {:.1f} + {:.1f} = {:.1f}
</div>
      
Result: {:.1f}
      
</body>
</html>
""".format(result, c, cCubed, squareRoot, squareRoot, a, division, division, multiplication, multiplication, b, result))
