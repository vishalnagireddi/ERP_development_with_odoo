{
    'name': 'Project',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Customize labels in project task list view',
    'description': """
        This module customizes the list view of tasks in the Project app.
        - "Title" becomes "Task"
        - "Project" becomes "Project Name"
        - "Tags" becomes "Practice"
        - "Stage" becomes "Status"
    """,
    'author': 'Vishal',
    'depends': ['project'],
    'data': [
        'views/project_task_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
