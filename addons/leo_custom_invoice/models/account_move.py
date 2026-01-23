from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    appointment_id = fields.Many2one(
        'leo.appointment',
        string='Appointment',
    )

    appointment_price = fields.Float(
        related="appointment_id.totalfee",
        store=True,
        string='Appointment Price'
    )