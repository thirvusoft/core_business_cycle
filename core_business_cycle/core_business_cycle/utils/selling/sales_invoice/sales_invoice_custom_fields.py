import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def sales_invoice_customization():
    sales_invoice_custom_field()
    sales_invoice_property_setter()

def sales_invoice_custom_field():
    custom_fields={
        "Sales Invoice":[
          dict(
                    fieldname='ts_landed_cost_voucher',
                    label='Landed Cost Voucher',
                    fieldtype='Section Break', 
                    insert_after = "total_taxes_and_charges",
          ),
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
          ),
          dict(
                    fieldname= "ts_total_amount",
                    fieldtype= "Currency",
                    insert_after= "ts_distribute_charges_based_on",
                    label= "Total Amount",
          ),
          dict(
                    fieldname= "ts_duplicate",
                    fieldtype= "Check",
                    hidden= 1,
                    insert_after= "ts_total_amount",
                    label= "Duplicate",
                    read_only= 1,
          ),
        ]
    }
    create_custom_fields(custom_fields)

def sales_invoice_property_setter():
    pass