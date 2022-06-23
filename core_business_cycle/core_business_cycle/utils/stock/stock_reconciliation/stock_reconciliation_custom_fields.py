from requests import options
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def stock_reconciliation_customization():
    stock_reconciliation_custom_field()
    stock_reconciliation_property_setter()

def stock_reconciliation_custom_field():
    custom_fields={
        "Stock Reconciliation":[
          dict(
                    fieldname= "ts_stock_entry_no",
                    fieldtype= "Link",
                    insert_after= "cost_center",
                    label= "Stock Entry No.",
                    options="Stock Entry"
          ),
        ]
    }
    create_custom_fields(custom_fields)

def stock_reconciliation_property_setter():
    pass