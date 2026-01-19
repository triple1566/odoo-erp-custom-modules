from odoo import fields, models

class realestate_clients(models.Model):
    _name = "real_estate_clients"
    _description = "real estate clients"

    name=fields.Char(required=True)
    age=fields.Integer()
    isvip=fields.Boolean()
    profit=fields.Float()
    region=fields.Selection(string='Region',
        selection=[('canada','Canada'), ('america','America'), ('uk','UK'), ('austrailia','Austrailia')],
        help="Region the client resides in")