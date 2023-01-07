import sqlite3
con = sqlite3.connect( "Ruokalista.db")
cur = con.cursor()

for row in cur.execute( "SELECT id, nimi, hinta FROM ruokalista"):
    rank = str( row[ 0]) + '.'
    article = row[ 1]
    price = '{:.2f}'.format( row[ 2]) + '€'
    print( rank + ' ' + article + ' ' + price)
