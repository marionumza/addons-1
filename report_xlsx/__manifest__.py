# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Base report xlsx",

    'summary': "Base module to create xlsx report",
    'author': 'ACSONE SA/NV,'
              'Creu Blanca,'
              'Odoo Community Association (OCA)',
    'website': "http://github.com/oca/reporting-engine",
    'category': 'Reporting',
    'version': '11.0.1.0.2',
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': [
            'xlutils',
            'xlrd',
        ],
    },
    'depends': [
        'base', 'web',
    ],
    'data': [
        'views/webclient_templates.xml',
        'views/report.xml',
    ],
     
    'installable': True,
}
