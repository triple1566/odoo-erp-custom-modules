from fastapi import FastAPI
import ML
from dotenv import load_dotenv
import os
from odoo_caller import odooLogin

load_dotenv()

host = str(os.getenv("HOST"))
port = str(os.getenv("PORT"))
db = str(os.getenv('DB'))
db_pw = str(os.getenv('DB_PW'))
admin = str(os.getenv('ADMIN'))

def connect_to_odoo():
    return odooLogin(host, int(port), admin, db, db_pw)

app = FastAPI(
    title="My API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"root called"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/checkodooconn")
def checkodooconn():
    try:
        odoo = connect_to_odoo()
    except:
        print("Odoo returned an error")
        return {"status": "odoo error"}
    print(
        "Available odoo db are: ",odoo.db.list(),
        "\n",
        "You are logged in as: ",odoo.env.user.name,
    )
    if odoo.env.user.name == "Administrator-Leo":
        return {"status": "ok"}
    
    else:
        return {"status","need login"}
    
#Lets check if the odoo proxy object remains after invoking /odooauth
@app.get("/odooops")
def odooops():
    try:
        odoo = connect_to_odoo()
    except:
        print("Odoo login request denied")
        return {"status":"login error"}
    
    try:
        invoice_records = odoo.env['account.move'].search([])
    except:
        print("error while fetching invoice record")
        return{"status":"error while fetching invoice record"}
    print("invoice record: ",invoice_records)
    recorddict = {}
    recorddictkey = 1
    for record in invoice_records:
        try:
            invoice_item = odoo.env['account.move'].browse(record)
            recorddict[recorddictkey] = invoice_item.name
            recorddictkey+=1
        except:
            pass
        print(invoice_item)

    return {
            "status":"ok",
            "records":recorddict
            }