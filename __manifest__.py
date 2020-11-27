# -*- coding: utf-8 -*-

{
    'name': 'Analytic account integration with projects',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
    'summary': 'account, project',
    'sequence': 60,
    'complexity': 'normal',
    'description': """
Analytic account integration with projects
==================================
This is an add-on to account.analytic.account that extends the capabilities of the module. The main task of the add-on is to create a new project with an analytic account when certain conditions are met.

Please contact the author for more details:
email: daniel.demedziuk@gmail.com
""",
    'website': 'website',
    'category': 'Tool, Addon',
    'depends': ['account', 'project'],
    'data': [
        'views/account_analytic_project_integration_view.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
    },
}
