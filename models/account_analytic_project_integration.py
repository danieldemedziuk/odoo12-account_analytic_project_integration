# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class account_analytic_project(models.Model):
    _inherit = 'account.analytic.account'

    type = fields.Selection([('view', 'Analytic view'), ('normal', 'Analytic account'), ('contract', 'Contract or Project'), ('template', 'Contract template')], string='Account type', help='Select the appropriate type for this analytical account.')
    manager_id = fields.Many2one('hr.employee', string='Contract manager', help='The manager responsible for this contract.', required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env['res.company']._company_default_get('account.analytic.account'))
    date_start = fields.Date(string="Start date", help='Start date of the project.')
    date_stop = fields.Date(string="Stop date", help='Project completion date.')
    notes = fields.Text(string="Notes", help='Space for a short note, description, project tasks.')

    # @api.model
    # def create(self, vals):
    #     res = super(account_analytic_project, self).create(vals)
    #     values_dict = {}
    #     self.env['project.project'].create(values_dict)
    #
    #     return res
    #
    # @api.multi
    # def write(self, vals):
    #     res = super(account_analytic_project, self).write(vals)
    #     values_dict = {}
    #
    #     return res
