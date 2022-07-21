import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def journal_entry_custom_fields():
          custom_fields = {
          "Journal Entry":[
                    dict(
                              fieldname='against_document', 
                              label='Against Document',
                              fieldtype='Data', 
                              insert_after='voucher_type',
                              read_only =1,
                    ),
                    dict(
                              fieldname='against_document_number', 
                              label='Against Document Number',
                              fieldtype='Data', 
                              insert_after='against_document',
                              read_only =1,
                    ),
               ],
          }
          create_custom_fields(custom_fields)