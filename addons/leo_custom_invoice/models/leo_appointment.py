from odoo import api, fields, models

class leo_appointment(models.Model):
    _name = 'leo.appointment'
    _description="leo's appointments"

    therapist = fields.Char(required=True)
    date = fields.Date(required=True)
    basefee = fields.Float(required=True)
    discount = fields.Float(required=True)
    totalfee = fields.Float(compute = "_compute_fee")

    def _compute_fee(self):
        for record in self:
            record.totalfee = record.basefee - record.discount
            if record.totalfee<0:
                record.totalfee=0