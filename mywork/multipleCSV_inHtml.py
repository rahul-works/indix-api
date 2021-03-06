import csv
import json
import glob

from bottle import route, run, get, request, response

path =r'../Datasets/API-Dataset/' 

@route('/')
@route('/upc/<name>')
def find(name):    
    
    allFiles = glob.glob(path + "/*.csv")
    jsonfile = open('upcM-'+name+'.json', 'w')
    fieldnames = ("pid","title","upcs","categoryld","storeld","seller","timestamp","price")
    
    for file_ in allFiles:
        print 'finding upc in '+file_  
        csvfile  = open(file_, 'r')
        
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
            if row['upcs']!="" and name in row['upcs']: 
                json.dump(row, jsonfile)
                jsonfile.write('\n')
                
    jsonfile = open('upcM-'+name+'.json', 'r')
    d = json.load(jsonfile)
    
    response.content_type = 'application/json'
    return d

@route('/pid/<name>')
def find2(name):
    allFiles = glob.glob(path + "/*.csv")
    jsonfile = open('pidM-'+name+'.json', 'w')
    fieldnames = ("pid","title","upcs","categoryld","storeld","seller","timestamp","price")
    
    for file_ in allFiles:
        print 'finding pid in '+file_  
        csvfile  = open(file_, 'r')
    
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
            if row['pid']!="" and name in row['pid']: 
                json.dump(row, jsonfile)
                jsonfile.write('\n')
    
    jsonfile = open('pidM-'+name+'.json', 'r')
    d = json.load(jsonfile)
    
    response.content_type = 'application/json'
    return d

@route('/category/<name>')
def find3(name):
    allFiles = glob.glob(path + "/*.csv")
    jsonfile = open('categoryM-'+name+'.json', 'w')
    fieldnames = ("pid","title","upcs","categoryld","storeld","seller","timestamp","price")
    
    for file_ in allFiles:
        print 'finding category in '+file_  
        csvfile  = open(file_, 'r')
    
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
            if row['categoryld']!="" and name in row['categoryld']: 
                json.dump(row, jsonfile)
                jsonfile.write('\n')
    
    jsonfile = open('categoryM-'+name+'.json', 'r')
    d = json.load(jsonfile)
    
    response.content_type = 'application/json'
    return d

@get('/search')
def find4():
    product = request.query['q']
    print product.strip()
    minPrice = request.query['minPrice']
    print minPrice
    maxPrice = request.query['maxPrice']
    print maxPrice
    
    allFiles = glob.glob(path + "/*.csv")
    jsonfile = open('searchM-'+product+'.json', 'w')
    fieldnames = ("pid","title","upcs","categoryld","storeld","seller","timestamp","price")
    
    for file_ in allFiles:
        print 'searching in '+file_  
        csvfile  = open(file_, 'r')
    
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
            if row['title']!="" and product in row['title'] and row['price']!="" and (float(minPrice)<=float(row['price']) and float(row['price'])<=float(maxPrice)):
                json.dump(row, jsonfile)
                jsonfile.write('\n')
    
    jsonfile = open('searchM-'+product+'.json', 'r')
    d = json.load(jsonfile)
    
    response.content_type = 'application/json'
    return d

run(host='localhost', port=8080, debug=True)


