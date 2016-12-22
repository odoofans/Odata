# -*- coding: utf-8 -*-
from Models import contact
import erppeek

class contact_test(object):
    partner = contact()
    port = "10000"
    database_name = "DataImport"
    username = "admin"
    password = "admin"
    model = 'res.partner'
    client = erppeek.Client('http://localhost:' + port, database_name, username, password)
    recs = partner.generate_res_partner_contacts(client, model, True)
