from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    repo = fields.Char()
    branch = fields.Char()
    pull_request = fields.Char()
