# -*- coding: utf-8 -*-

from openerp import models, fields, api

class vacaciones(models.Model):
    _name = 'vacaciones.vacaciones'
    partner_id = fields.Many2one('res.partner')
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    dias_laborables = fields.Integer()
    tipo_vacaciones = fields.Selection([('verano ','verano '),('invierno','invierno'),('asuntos propios','asuntos propios')],required=True)
