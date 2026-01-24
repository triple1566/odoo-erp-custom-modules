import odoorpc

def odooLogin(host: str, port: int, admin:str, db:str, db_pw:str):
    odoo = odoorpc.ODOO(host,port=port)
    odoo.login(db, admin, db_pw)
    return odoo

