import odoorpc

odoo = odoorpc.ODOO('localhost', port=8069)
print(odoo.db.list())

odoo.login('odoo', 'ljhub1566@gmail.com', 'odoo')

user = odoo.env.user
print("Username is: " + user.name)
print("Company is: " + user.company_id.name)

if 'ir.model' in odoo.env:
    print('hi')