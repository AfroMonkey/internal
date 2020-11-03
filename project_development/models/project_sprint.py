from datetime import timedelta

from odoo import api, fields, models


class ProjectSprint(models.Model):
    _name = "project.sprint"

    name = fields.Char(
        compute="_compute_name",
        index=True,
    )
    start = fields.Date(required=True, default=fields.Date.today)
    end = fields.Date(
        required=True,
        default=lambda self: fields.Date.today() + timedelta(days=7),  # TODO config
    )
    task_ids = fields.One2many(
        comodel_name="project.task",
        inverse_name="sprint_id",
    )
    planned_hours = fields.Float(compute="_compute_planned_hours")

    @api.depends("start")
    def _compute_name(self):
        for sprint in self:
            sprint.name = f"S{sprint.start.year}W{sprint.start.isocalendar()[1]}"  # TODO name depends on periodicy, actually weekly

    @api.depends("task_ids")
    def _compute_planned_hours(self):
        for sprint in self:
            sprint.planned_hours = sum(sprint.task_ids.mapped("planned_hours"))
