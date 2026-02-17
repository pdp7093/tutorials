from odoo import models,fields, Command



class InheritedModel(models.Model):
    _inherit = "estate.property"

    invoice_count = fields.Integer(
        string="Invouce Count",
        compute = "_compute_invoice_count"
    )

    def _compute_invoice_count(self):
        for record in self:
            record.invoice_count = self.env["account.move"].search([
                ("move_type","=","out_invoice"),
                ("invoice_origin","=",record.name)
            ])
    def action_sold(self):
        res = super().action_sold()

        for record in self:
            commission = record.selling_price * 0.06
            self.env["account.move"].create({
                "move_type":"out_invoice",
                "partner_id":record.buyer_id.id ,
                "invoice_date":fields.Date.today(),
                "invoice_origin":record.name,
                "invoice_line_ids":[
                    Command.create({
                        "name":record.name,
                        "quantity":1,
                        "price_unit":record.selling_price,
                    }),
                    Command.create({
                        "name":"Adminstrative Fees",
                        "quantity":1,
                        "price_unit":100.0,
                    }),
                    Command.create({
                        "name":"Agency Commission (6%)",
                        "quantity":1,
                        "price_unit":commission,
                    }),
                ],

            })
        return res

    def action_view_invoices(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Invoices",
            "view_mode": "list,form",
            "res_model": "account.move",
            "domain": [
                ("move_type", "=", "out_invoice"),
                ("invoice_origin", "=", self.name),
            ],
            "context": {"default_move_type": "out_invoice"},
        }
