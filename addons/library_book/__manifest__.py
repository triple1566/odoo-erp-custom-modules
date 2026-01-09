{
    'name':'Library Book',
    'version':'1.0',
    'summary': 'simple library book management',
    'category':'tools',
    'depends':['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/library_book_rules.xml',
        'views/book_views.xml',
    ],
    'application':True
}