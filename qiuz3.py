import requests
import json
import sqlite3
conn = sqlite3.connect('NASAA.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS NASAA
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            copyright VARCHAR(20),
            media_type VARCHAR(20),
            date VARCHAR(20)
            )''')

c.execute('INSERT INTO NASAA (copyright, media_type, date) VALUES (?, ?, ?)', ("MaryBeth Kiczenski", "image", "2021-05-05"))
conn.commit()

key = 'c2DwBf9noyHSVAcsJsTj0YMWzFYFWwQecRBi0J8x'
payload = {'api_key': key, 'date': '2021-05-05'}
resp = requests.get(f'https://api.nasa.gov/planetary/apod', params=payload)
#print(resp)
print(resp.headers['content-type'])
print(resp.status_code)

#print(resp.text)


r = json.loads(resp.text)
with open('NASA.json', 'w') as F:
    json.dump(r, F, indent=5)
print(json.dumps(r, indent=5))

print('თარიღი --> ', r['date'], 'yy/mm/dd')
print('სათაური, დასახელება --> ', r['title'])
print('ლინკი --> ', r['url'])


