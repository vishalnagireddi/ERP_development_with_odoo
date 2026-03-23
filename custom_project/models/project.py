from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    sale_line_id = fields.Many2one('sale.order.line', string='Sales Order Item')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    status_color = fields.Html(string="Status Color", compute="_compute_status_color", sanitize=False)


    head_count = fields.Integer(
        string='Head Count',
        compute='_compute_head_count'
    )

    @api.depends('task_ids.user_ids')
    def _compute_head_count(self):
        for project in self:
            user_set = set()
            for task in project.task_ids:
                user_set.update(task.user_ids.ids)
            project.head_count = len(user_set)

    @api.depends('stage_id')
    def _compute_status_color(self):
        for project in self:
            color = "#FFD700"  # Default Yellow (To Do)
            label = "To Do"

            if project.stage_id:
                stage_name = project.stage_id.name.lower()
                if 'progress' in stage_name:
                    color = "#FFBF00"  # Amber
                    label = "In Progress"
                elif 'done' in stage_name:
                    color = "#28a745"  # Green
                    label = "Done"
                # You can add more conditions here if needed

            project.status_color = f"""
                    <span style='display:inline-block; width:12px; height:12px;
                                 background-color:{color}; border-radius:50%;
                                 margin-right:6px;'></span>{label}
                """