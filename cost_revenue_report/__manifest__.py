{
    'name': 'costrevenuereport',
    'summary': 'costrevenuereport',
    'description': """costrevenuereport""",
    #  'author': "My Company",
    'website': 'http://www.yourcompany.com',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.6',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cost_revenue_report_views.xml',
        #'views/task_report_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}