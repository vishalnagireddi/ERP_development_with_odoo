from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    # Dropdown to select the project type
    project_type = fields.Selection([
        ('aio', 'Application Implementation (AIO)'),
        ('ams', 'Application Maintenance Services (AMS)')
    ], string='Project Type', default='aio')

    # Common fields
    project_id = fields.Char(string="Project ID")
    location = fields.Char(string="Location")
    project_manager = fields.Many2one('res.users', string="Project Manager")
    assignee_ids = fields.Many2many(
        'res.users',  # Model to link (users)
        # 'project_project_user_rel',  # Relation table name (can be any name)
        # 'project_id',  # Column referring to the project
        # 'user_id',  # Column referring to the user
        string='Assignees'
    )
    priority = fields.Selection([
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High')
    ], string="Priority", default='2')
    practice = fields.Selection([
        ('sap', 'SAP'),
        ('infor', 'Infor'),
        ('odoo', 'Odoo'),
        ('bi', 'BI'),
        ('other', 'Other')
    ], string='Practice')
    description = fields.Text(string="Description")

    # AIO-specific fields
    scope = fields.Char(string="Scope")
    kick_off_date = fields.Date(string="Kick-off Date")
    go_live_date = fields.Date(string="Go Live Date")
    client_stakeholders = fields.Char(string="Client Stakeholders")
    internal_stakeholders = fields.Char(string="Internal Stakeholders")
    project_phase = fields.Selection([
        ('planning', 'Planning'),
        ('execution', 'Execution'),
        ('testing', 'Testing'),
        ('go_live', 'Go Live')
    ], string="Project Phase")

    # AMS-specific fields
    support_start_date = fields.Date(string="Support Start Date")
    support_end_date = fields.Date(string="Support End Date")
    monthly_hours_committed = fields.Float(string="Monthly Hours Committed")
    ticket_tool_used = fields.Char(string="Ticket Tool Used")
    account_manager = fields.Many2one('res.users', string="Account Manager")
    renewal_due = fields.Date(string="Renewal Due")
