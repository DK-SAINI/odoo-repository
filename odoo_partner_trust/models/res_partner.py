# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    trust_state = fields.Selection(
        [("trusted", "Trusted"), ("blacklisted", "BlackListed")],
        string="Trust Status",
        default="trusted",
    )
