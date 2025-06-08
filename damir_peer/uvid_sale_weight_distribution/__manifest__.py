{
    'name': 'Sale Weight Distribution',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Weight Distribution',
    'description': """
        Adds weight balancing on sale orders
    """,
    'depends': [
        'sale_management',
    ],
    'data': [
       'views/sale_order_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3'
}
