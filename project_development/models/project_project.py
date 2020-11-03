from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    odoo_version = fields.Char()
    master_repo = fields.Char()
    domain = fields.Char()
