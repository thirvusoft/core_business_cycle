from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
def delivery_note_customization():
    delivery_note_custom_field()
    delivery_note_property_setter()

def delivery_note_custom_field():
    custom_fields={
        "Delivery Note":[
          dict(
                    fieldname= "ts_landed_cost_voucher",
                    fieldtype= "Section Break",
                    insert_after= "pricing_rules",
                    label= "Landed Cost Voucher",
          ),
        #   dict(
        #             fieldname= "cost_center",
        #             fieldtype= "Link",
        #             insert_after= "ts_landed_cost_voucher",
        #             label= "Cost Center",
        #             options="Cost Center"
        #   ),
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

def delivery_note_property_setter():
    pass