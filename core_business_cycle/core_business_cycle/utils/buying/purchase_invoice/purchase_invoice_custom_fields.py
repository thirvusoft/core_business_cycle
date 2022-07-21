from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def purchase_invoice_customization():
    purchase_invoice_custom_field()
    purchase_invoice_property_setter()

def purchase_invoice_custom_field():
    custom_fields={
        "Purchase Invoice":[
          dict(
                    fieldname= "ts_landed_cost_voucher",
                    fieldtype= "Section Break",
                    insert_after= "taxes",
                    label= "Landed Cost Voucher",
          ),
         dict(fieldname='type', label='Type',
				fieldtype='Select', options='\nInclusive\nExclusive',
                insert_after='ts_landed_cost_voucher'),

          dict(
                    fieldname= "ts_landed_cost_voucher_table",
                    fieldtype= "Table",
                    insert_after= "ts_landed_cost_voucher",
                    options= "TS Landed Cost Voucher",
          ),

          dict(
                    fieldname= "ts_distribute_charges_based_on",
                    fieldtype= "Select",
                    insert_after= "ts_landed_cost_voucher_table",
                    label= "Distribute Charges Based On",
                    options= "Qty\nAmount",
                    depends_on='eval:doc.ts_landed_cost_voucher_table',
                  
          ),
          dict(
                    fieldname= "ts_total_amount",
                    fieldtype= "Currency",
                    insert_after= "ts_distribute_charges_based_on",
                    label= "Total Amount",
                    depends_on='eval:doc.ts_landed_cost_voucher_table',
                    read_only=1,
          ),
        ]
    }
    create_custom_fields(custom_fields)

def purchase_invoice_property_setter():
    pass