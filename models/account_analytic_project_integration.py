# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import date
import logging

_logger = logging.getLogger(__name__)

today = date.today().strftime('%Y-%m-%d')

class account_analytic_project(models.Model):
    _inherit = 'account.analytic.account'

    type = fields.Selection([('view', 'Analytic view'), ('normal', 'Analytic account'), ('contract', 'Contract or Project'), ('template', 'Contract template')], default="contract", string='Account type',
                            help='Select the appropriate type for this analytical account.', required=True)
    manager_id = fields.Many2one('hr.employee', string='Contract manager', help='The manager responsible for this contract.', required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env['res.company']._company_default_get('account.analytic.account'), required=True)
    date_start = fields.Date(string="Start date", help='Start date of the project.', default=today)
    date_stop = fields.Date(string="Stop date", help='Project completion date.')
    notes = fields.Text(string="Notes", help='Space for a short note, description, project tasks.')
    project_id = fields.Many2one('project.project')
    parent_id = fields.Many2one('account.analytic.account', default=40840,)
    state = fields.Selection([
        ('template', 'Template'),
        ('draft', 'New'),
        ('open', 'In Progress'),
        ('pending', 'To Renew'),
        ('close', 'Closed'),
        ('cancelled', 'Cancelled')], 'Status', default="draft", required=True, track_visibility='onchange', copy=False)

    @api.constrains("name", "partner_id", "date_start", "date_stop")
    def _add_project(self):
        for rec in self:
            if not rec.project_id and (rec.type == 'contract'):
                self.project_id = self.env["project.project"].create({
                    'name': rec.name,
                    'user_id': self.env['res.users'].search([('name', '=', rec.manager_id['name'])]).id,
                    'date_start': rec.date_start,
                    'date': rec.date_stop,
                    'analytic_account_id': rec.id,
                    'partner_id': rec.partner_id.id,
                })

            elif rec.name or rec.partner_id or rec.manager_id or rec.date_start or rec.date_stop:
                self.project_id.write({
                    'name': rec.name,
                    'user_id': self.env['res.users'].search([('name', '=', rec.manager_id['name'])]).id,
                    'date_start': rec.date_start,
                    'date': rec.date_stop,
                    'partner_id': rec.partner_id.id,
                })

    @api.constrains('active')
    def _archive_project(self):
        for rec in self:
            if not rec.active:
                self.project_id.write({
                    'active': False,
                })
            if rec.active:
                self.project_id.write({
                    'active': True,
                })

    def action_template(self):
        if self.employees_ids and self.project_id and self.date_start:
            self.ensure_one()
            self.write({'state': 'template'})

    def action_draft(self):
        if self.employees_ids and self.project_id and self.date_start:
            self.ensure_one()
            self.write({'state': 'draft'})

    def action_open(self):
        if self.employees_ids and self.project_id and self.date_start:
            self.ensure_one()
            self.write({'state': 'open'})

    def action_pending(self):
        if self.employees_ids and self.project_id and self.date_start:
            self.ensure_one()
            self.write({'state': 'pending'})

    def action_close(self):
        if self.employees_ids and self.project_id and self.date_start:
            self.ensure_one()
            self.write({'state': 'close'})

    def action_cancelled(self):
        if self.employees_ids and self.project_id and self.date_start:
            self.ensure_one()
            self.write({'state': 'cancelled'})
