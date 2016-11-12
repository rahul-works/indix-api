Requirement: 
1. Python3
2. Bottle 
3. virtualenv
4. pip

Install commands
1. virtualenv develop
2. source develop/bin/activate
3. pip install -U bottle
4. python multipleCSV_inFile.py
or
4. python multipleCSV_inHtml.py

CSV files should be in folder path: "../Datasets/API-Dataset/"

End points:
GET /upc/<input upc>
GET /pid/<input pid>
GET /category/<input category>
GET /search?q=<search tokens>&minPrice=<lower limit>&maxPrice=<upper limit> (example /search?q=iphone%206s&minPrice=500&maxPrice=950)

Tested End points:
http://localhost:8080/upc/00631620109196
http://localhost:8080/pid/ad6830d1e0721d693a932e7673866fe1
http://localhost:8080/category/25171
http://localhost:8080/search?q=Toffee&minPrice=2.99&maxPrice=100