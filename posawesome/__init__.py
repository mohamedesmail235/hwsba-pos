# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = "15.0.1"


def console(*data):
    frappe.publish_realtime("toconsole", data, user=frappe.session.user)
