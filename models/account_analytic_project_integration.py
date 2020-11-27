# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class account_analytic_project(models.Model):
    _inherit = 'account.analytic.account'

    account_type = fields.Selection([('view', 'Analytic view'), ('normal', 'Analytic account'), ('contract', 'Contract or Project'), ('template', 'Contract template')])
