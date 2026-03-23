from odoo import models, fields, api

class CRMStage(models.Model):
    _inherit = 'crm.stage'

    required_fields = fields.Char(compute='_compute_required_fields', store=True)

    FIELD_DISPLAY_NAMES = {
        'name': 'Name',
        'partner_id': 'Customer',
        'phone': 'Phone',
        'email_from': 'Email',
        'user_id': 'Salesperson',
        'planned_revenue': 'Expected Revenue',
        'source_id': 'Source',
        'contact_name': 'Contact Name',
        'function': 'Job Position',
        'campaign_id': 'Campaign',
        'medium_id': 'Medium',
        'referred': 'Referred By',
        'website': 'Website',
        'team_id': 'Sales Team',
        'street': 'Street',
        'city': 'City',
        'state_id': 'State',
        'zip': 'ZIP',
        'country_id': 'Country',
        'description': 'Description',
        'lost_reason': 'Lost Reason',
        'partner_name': 'Company Name',
        'date_deadline': 'Expected Closing'
    }

    def get_required_fields(self):
        stage_name = self.name.lower() if self.name else ''

        if 'suspect' in stage_name:
            return ['name', 'partner_id', 'phone', 'partner_name']
        elif 'prospect' in stage_name:
            return ['name', 'partner_id', 'phone', 'email_from']
        elif 'qualified' in stage_name:
            return ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id','date-deadline']
        elif 'demo' in stage_name:
            return ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                    'contact_name', 'function', 'campaign_id', 'medium_id', 'referred']
        elif 'proposal' in stage_name:
            return ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                    'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                    'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id']
        elif 'negotiation' in stage_name:
            return ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                    'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                    'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                    'description']
        elif 'won' in stage_name:
            return ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                    'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                    'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                    'description']
        return []

    @api.depends('name')
    def _compute_required_fields(self):
        for stage in self:
            tech_fields = stage.get_required_fields()
            display_names = [self.FIELD_DISPLAY_NAMES.get(field, field) for field in tech_fields]