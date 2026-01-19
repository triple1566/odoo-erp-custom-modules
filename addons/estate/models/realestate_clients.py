from odoo import fields, models

class realestate_clients(models.Model):
    _name = "real_estate_clients"
    _description = "real estate clients"

    name=fields.Char(required=True)
    age=fields.Integer()
    isvip=fields.Boolean()

    profit=fields.Float(default=0)
    loss=fields.Float(default=0)
    networth=fields.Float(compute="_compute_networth")

    region=fields.Selection(string='Region',
        selection=[('canada','Canada'), ('america','America'), ('uk','UK'), ('austrailia','Austrailia')],
        help="Region the client resides in")
    alive=fields.Boolean(default=True)

    def neutralize_client(self):
        self.alive=False
        return

    def _compute_networth(self):
        for record in self:
            record.networth = record.profit-record.loss
            if record.networth<0:
                record.networth=0