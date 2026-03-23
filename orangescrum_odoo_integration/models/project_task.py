from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'


    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    spent_time=fields.Float(string="Spent Time")
    internal_verification_on = fields.Date(string="Internal Verification On")
    verified_by = fields.Char(string="Verified By")
    customer_verification_on = fields.Date(string="Customer Verification On")
    confirmed_by = fields.Char(string="Confirmed By")


    priority_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Priority Level")

    review_required = fields.Boolean(string="Requires Review")
