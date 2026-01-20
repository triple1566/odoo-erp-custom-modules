{
    'name':'Leo Invoicing',
    'version':'1.0',
    'summary': 'Leos Custom Invoicing Module',
    'category':'tools',
    'depends':['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/leo_invoice_appointment_views.xml',
        'views/account_move.xml',
        'views/leo_invoice_menu.xml'
    ],
    'application':True
}