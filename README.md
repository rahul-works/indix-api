<b>Requirement:</b>  <br />
1. Python3 <br />
2. Bottle  <br />
3. virtualenv <br />
4. pip <br />

<b>Install commands</b> <br />
1. virtualenv develop<br />
2. source develop/bin/activate<br />
3. pip install -U bottle<br />
4. python multipleCSV_inFile.py<br />
or<br />
4. python multipleCSV_inHtml.py<br />
<br />
CSV files should be in folder path: "../Datasets/API-Dataset/"<br />
<br />
<b>End points:</b> <br />
GET /upc/<input upc><br />
GET /pid/<input pid><br />
GET /category/<input category><br />
GET /search?q=<search tokens>&minPrice=<lower limit>&maxPrice=<upper limit> (example /search?q=iphone%206s&minPrice=500&maxPrice=950)<br />

<b>Tested End points:</b> <br />
http://localhost:8080/upc/00631620109196<br />
http://localhost:8080/pid/ad6830d1e0721d693a932e7673866fe1<br />
http://localhost:8080/category/25171<br />
http://localhost:8080/search?q=Toffee&minPrice=2.99&maxPrice=100<br />
