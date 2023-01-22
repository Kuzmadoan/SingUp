import sqlite3
import json
from aiohttp import web

routes = web.RouteTableDef()

json_file = open(r"C:\Users\kuzma\New folder\sain up\JSON\template.json")
json_data = json.load(json_file)

print(json_data)

def getPassword(email):
    
     conn = sqlite3.connect("SQL/database.db")
     cur = conn.cursor()

     emails = cur.execute("SELECT email FROM account").fetchall()
     # [('admin@gmail.com',)]
     for i in range(len(emails)):
        emails[i] = emails[i][0]

     if email in emails:
         return cur.execute(f"SELECT password FROM account WHERE email= '{email}'").fetchone()[0]

@routes.get('/')
async def webpage(request):
    html = open(r"C:\Users\kuzma\New folder\sain up\HTML\index.html")
    return web.Response(
        text = html.read(),
        content_type = 'text/html'
    )

@routes.get('/done')
async def webpage(request):
    html = open(r"C:\Users\kuzma\New folder\sain up\HTML\log-in.html")
    return web.Response(
        text = html.read(),
        content_type = 'text/html'
    )

# getPassword("admin@gmail.com")
app = web.Application()
app.add_routes(routes)
web.run_app(app)
