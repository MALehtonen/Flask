import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route( "/")
def listaa():    
    with sqlite3.connect( "Ruokalista.db") as con:
        cur = con.cursor()
        entries = []
       
        for row in cur.execute( "SELECT id, nimi, hinta FROM ruokalista"):
            rank = str( row[ 0]) + '.'
            article = row[ 1]
            price = '{:.2f}'.format( row[ 2]) + '€'
            entries.append( [rank, article, price])
       
        return render_template( "Ruokalista.html", entries = entries)
            
