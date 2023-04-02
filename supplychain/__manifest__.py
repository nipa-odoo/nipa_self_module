{
    'name': "supplychain",
    'version': '0.1.0',
    'author': "nipa",
    'category': 'Supply chain',
    'description': """

    """,
    # data files always loaded at installation
    'data': [
         'security/ir.model.access.csv',
         'views/supply_views.xml',
         'views/supply_products.xml',
         'views/supply_dealers.xml',
         'views/supply_wholesaler.xml',
         'views/supply_store.xml',
         'views/supply_menus.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
          'demo/demo_data.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}