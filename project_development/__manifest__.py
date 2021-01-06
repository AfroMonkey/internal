{
    "name": "Project Development",
    "version": "13.0.0.1.0",
    "author": "HomebrewSoft, Odoo Community Association (OCA)",
    "website": "https://homebrewsoft.dev",
    "license": "LGPL-3",
    "depends": [
        "project",
    ],
    "data": [
        # security
        "security/ir.model.access.csv",  # TODO
        # data
        # reports
        # views
        "views/project_project.xml",
        "views/project_sprint.xml",
        "views/project_task.xml",
    ],
}
