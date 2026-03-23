{
    'name': 'OrangeScrum Odoo Integration',
    'version': '1.0',
    'summary': 'Add and remove fields in Project module, according to Orangescrum',
    'description': """
This module customizes the Task form in the Project app:
- Adds custom fields like Priority Level and Review Required.
- Optionally removes or replaces existing fields.
""",
    'author': 'Shivani Hirapara',
    'website': 'https://yourwebsite.com',
    'category': 'Project',
    'depends': ['project','sale'],
    'data': [
        'views/project_task_view.xml',
        'views/project_tree_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
