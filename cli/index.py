import sys, sqlite3

script, database = sys.argv

query = """
select *
FROM teachers 
where teachers.FirstName like Brion;
"""
try:
 dbconnectie = sqlite3.connect(database)
 mijn_cursor = dbconnectie.cursor()
except:
 print("Geen connectie met database mogelijk.")
 sys.exit(-1)

antwoord = []

try:
	mijn_cursor.execute(query)
	antwoord = mijn_cursor.fetchall()
except Exception as e:
	print("query uitvoeren niet gelukt!", e)
