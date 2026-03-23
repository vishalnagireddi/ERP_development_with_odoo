from odoo import models, fields, api

from odoo.exceptions import ValidationError,UserError
from odoo import _

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    FIELD_DISPLAY_NAMES = {
        'name': 'Name',
        'partner_id': 'Customer',
        'phone': 'Phone',
        'email_from': 'Email',
        'expected_revenue': 'Expected Revenue',
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
        'partner_name': 'Company Name',
        'date_deadline': 'Expected Closing'
    }

    def check_required_fields(self):
        """Check if all required fields are filled for the current stage"""
        stage = self.stage_id
        if not stage:
            stage = self.env['crm.stage'].get_default_stage()
            if not stage:
                return

        stage_name = stage.name.lower() if stage.name else ''
        required_fields = []

        if 'suspect' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'partner_name']  # Added partner_name
        elif 'prospect' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from']
        elif 'qualified' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'date_deadline']
        elif 'demo' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred']
        elif 'proposal' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                               'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id']
        elif 'negotiation' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                               'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                               'description']
        elif 'won' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                               'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                               'description']

        missing_fields = []
        for field in required_fields:
            if not self[field]:
                missing_fields.append(field)

        if missing_fields:
            display_names = [self.FIELD_DISPLAY_NAMES.get(field, field) for field in missing_fields]
            raise ValidationError(
                f"The following fields are required at {stage.name} stage: {', '.join(display_names)}"
            )

    @api.model
    def create(self, vals):
        """Override create to check required fields"""
        # If no stage is provided, get the default stage
        if not vals.get('stage_id'):
            # Use direct search instead of get_default_stage()
            default_stage = self.env['crm.stage'].search([('name', 'ilike', 'suspect')], limit=1)
            if default_stage:
                vals['stage_id'] = default_stage.id

        # Create the lead first
        lead = super(CRMLead, self).create(vals)

        # Get stage for validation
        stage = lead.stage_id
        if not stage:
            # Use direct search again for validation
            stage = self.env['crm.stage'].search([('name', 'ilike', 'suspect')], limit=1)
            if not stage:
                return lead

        stage_name = stage.name.lower() if stage.name else ''
        required_fields = []

        if 'suspect' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'partner_name']
        elif 'prospect' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from']
        elif 'qualified' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'date_deadline']
        elif 'demo' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred']
        elif 'proposal' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                               'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id']
        elif 'negotiation' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                               'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                               'description']
        elif 'won' in stage_name:
            required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                               'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                               'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                               'description']

        missing_fields = []
        for field in required_fields:
            if not lead[field]:
                missing_fields.append(field)

        if missing_fields:
            lead.unlink()
            display_names = [self.FIELD_DISPLAY_NAMES.get(field, field) for field in missing_fields]
            raise ValidationError(
                f"The following fields are required at {stage.name} stage: {', '.join(display_names)}"
            )

        return lead

    def write(self, vals):
        """Override write to check required fields"""
        if 'stage_id' in vals:
            stage = self.env['crm.stage'].browse(vals['stage_id'])
            if not stage:
                # Get the first stage of the current team
                stage = self.env['crm.stage'].search([], limit=1)
                if not stage:
                    raise UserError(_('No CRM stage found in the system!'))

            stage_name = stage.name.lower() if stage.name else ''
            required_fields = []

            if 'suspect' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'partner_name']  # Added partner_name
            elif 'prospect' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'email_from']
            elif 'qualified' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                                   'date_deadline']
            elif 'demo' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                                   'contact_name', 'function', 'campaign_id', 'medium_id', 'referred']
            elif 'proposal' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                                   'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                                   'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id']
            elif 'negotiation' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                                   'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                                   'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                                   'description']
            elif 'won' in stage_name:
                required_fields = ['name', 'partner_id', 'phone', 'email_from', 'expected_revenue', 'source_id',
                                   'contact_name', 'function', 'campaign_id', 'medium_id', 'referred',
                                   'website', 'phone', 'team_id', 'street', 'city', 'state_id', 'zip', 'country_id',
                                   'description']

            missing_fields = []
            for field in required_fields:
                if field in vals:
                    if not vals[field]:
                        missing_fields.append(field)
                else:
                    if not self[field]:
                        missing_fields.append(field)

            if missing_fields:
                display_names = [self.FIELD_DISPLAY_NAMES.get(field, field) for field in missing_fields]
                raise ValidationError(
                    f"The following fields are required to move to {stage.name} stage: {', '.join(display_names)}"
                )

        res = super(CRMLead, self).write(vals)
        return res