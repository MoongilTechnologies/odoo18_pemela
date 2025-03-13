{
    'name': "Repair Order IMEI Extension",
    'version': '1.0',
    'depends': ['helpdesk_repair', 'mrp_repair', 'repair'],
    'author': "Your Name",
    'category': 'Manufacturing',
    'summary': "Adds an IMEI field to repair orders",
    'data': [
        'views/repair_views.xml',
    ],
    'installable': True,
    'application': False,
}
