from odoo import models,fields, Command



class InheritedModel(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        res = super().action_sold()

        for record in self:
            commission = record.selling_price * 0.06
            self.env["account.move"].create({
                "move_type":"out_invoice",
                "partner_id":record.buyer_id.id ,
                "invoice_date":fields.Date.today(),
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
