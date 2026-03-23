from odoo import models

class ProjectTask(models.Model):
    _inherit = 'project.task'
    # No changes here since we're just changing label in the view
