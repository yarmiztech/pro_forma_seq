from odoo import fields, models, api



class ProFormaInvoice(models.Model):
    _inherit = 'pro.forma.invoice'

    @api.model
    def create(self, vals):
        if vals.get('name', 'Draft') == 'Draft':
            vals['name'] = self.env['ir.sequence'].next_by_code('pro.forma.no') or '/'
        res = super(ProFormaInvoice, self).create(vals)
        return res

    name = fields.Char(string='Pro-Forma Invoice',default="Draft",copy=False,required=True)



