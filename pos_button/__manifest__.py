{
    'name': 'POS Custom Button',
    'version': '1.0',
    'category': 'POS',
    'summary': 'Adding a custom button',
    'author': 'Your Name',
    'depends': ['point_of_sale','base','repair'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_button/static/src/app/custom_button/custom_button.js',
            'pos_button/static/src/app/custom_button/custom_button.xml',
        ],
    },
    'installable': True,
    'application': False,
}
