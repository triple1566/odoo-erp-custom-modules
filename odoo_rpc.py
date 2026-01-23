import odoorpc

#specify odoo instance
odoo = odoorpc.ODOO('localhost', port=8069)
print(odoo.db.list())

#loggin into odoo db
odoo.login('odoo', 'ljhub1566@gmail.com', 'odoo')

#accessing current user details
user = odoo.env.user
print("Username is: " + user.name)
print("Company is: " + user.company_id.name)

#Getting the recordset design pattern:
# 1. retrieve all record IDs (or some IDs) from the model
# 2. using the ID, browse the model to create proxy recordsets
# 3. The created recordsets can be used to access individual fields

#Check if model actually exists in db
if 'leo.appointment' in odoo.env:
    print('Appointment model is in place')

    #create an ID list of the records within our model
    appointments_list = odoo.env['leo.appointment'].search([])

    #for all record ID from the model, get the records corresponding to each ID
    for appointment in appointments_list:
        print('Record ID:'+str(appointment))
        app_record = odoo.env['leo.appointment'].browse(appointment)
        print((
            app_record.id,
            app_record.therapist,
            (app_record.date.year, app_record.date.month, app_record.date.day),
            app_record.totalfee
        ))