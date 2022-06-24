from . import __version__ as app_version

app_name = "core_business_cycle"
app_title = "Core Business Cycle"
app_publisher = "BC"
app_description = "BC"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bc@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/core_business_cycle/css/core_business_cycle.css"
# app_include_js = "/assets/core_business_cycle/js/core_business_cycle.js"

# include js, css files in header of web template
# web_include_css = "/assets/core_business_cycle/css/core_business_cycle.css"
# web_include_js = "/assets/core_business_cycle/js/core_business_cycle.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "core_business_cycle/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
doctype_js = {
	"Delivery Note":"core_business_cycle/utils/selling/delivery_note/delivery_note.js",
	"Sales Invoice":"core_business_cycle/utils/selling/sales_invoice/sales_invoice.js",
	"Purchase Receipt":"core_business_cycle/utils/buying/purchase_receipt/purchase_receipt.js",
	"Purchase Invoice":"core_business_cycle/utils/buying/purchase_invoice/purchase_invoice.js",
	"Stock Entry":"core_business_cycle/utils/stock/stock_entry/stock_entry.js"
	}


# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "core_business_cycle.install.before_install"
after_install = "core_business_cycle.core_business_cycle.utils.after_install.after_install"

# Uninstallation
# ------------

# before_uninstall = "core_business_cycle.uninstall.before_uninstall"
# after_uninstall = "core_business_cycle.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "core_business_cycle.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Stock Reconciliation": "core_business_cycle.core_business_cycle.utils.stock.stock_reconciliation.stock_reconciliation.StockReconciliation"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Purchase Receipt":{
		"on_submit":["core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.creating_journal_entry",
					 "core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.creating_landed_cost_voucher"],
		"on_cancel":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.removing_journal_entry",
		"validate":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.total_amount_calculator"
	},
	"Purchase Invoice":{
		"on_submit":["core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.creating_journal_entry",
					 "core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.creating_landed_cost_voucher"],
		"on_cancel":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.removing_journal_entry",
		"validate":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.total_amount_calculator"
	},
	"Stock Entry":{
		"on_submit":["core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.creating_journal_entry",
					 "core_business_cycle.core_business_cycle.utils.stock.stock_reconciliation.stock_reconciliation.creating_stock_reconciliation"],
		"on_cancel":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.removing_journal_entry",
		"validate":["core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.total_amount_calculator"]
	},
	"Delivery Note":{
		"on_submit":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.creating_journal_entry",
		"on_cancel":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.removing_journal_entry",
		"validate":"core_business_cycle.core_business_cycle.utils.stock.landed_cost_voucher.landed_cost_voucher.total_amount_calculator"
	},
	"Stock Reconciliation":{
		"validate":"core_business_cycle.core_business_cycle.utils.stock.stock_reconciliation.stock_reconciliation.calculating_difference_value"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"core_business_cycle.tasks.all"
# 	],
# 	"daily": [
# 		"core_business_cycle.tasks.daily"
# 	],
# 	"hourly": [
# 		"core_business_cycle.tasks.hourly"
# 	],
# 	"weekly": [
# 		"core_business_cycle.tasks.weekly"
# 	]
# 	"monthly": [
# 		"core_business_cycle.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "core_business_cycle.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "core_business_cycle.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "core_business_cycle.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"core_business_cycle.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
