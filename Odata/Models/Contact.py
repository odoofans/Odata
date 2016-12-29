import time
import erppeek
import random
import names

class Contact(object):
    def __init__(self):
        """
            Wrapper
        """

    def generate_contacts(self, client, show_generated_records_in_terminal, number_of_recs):
        start_time = time.time()
        model_proxy = client.model('res.partner')
        contact_types = ['person', 'company']
        domains = ["@aol.com", "@att.net", "@comcast.net", "@facebook.com", "@gmail.com", "@gmx.com", "@googlemail.com",
  "@google.com", "@hotmail.com", "@hotmail.co.uk", "@mac.com", "@me.com", "@mail.com", "@msn.com",
  "@live.com", "@sbcglobal.net", "@verizon.net", "@yahoo.com", "@yahoo.co.uk"]
        white_place_changer = ['.', '_', '-']
        company_contact = ['info', 'contact', 'sales', 'support']
        extension = ['.com', '.be', '.nl', '.fr', '.de', '.us']

        for index in range(0, number_of_recs):
            business_type = ['SA', 'NV', 'NGO', 'Ltd', 'VZW']
            company_type = random.choice(contact_types)
            if company_type == 'person':
                name = names.get_full_name()
                email = name.replace(' ',random.choice(white_place_changer)) + random.choice(domains)
            else:
                name = names.get_last_name() + ' ' + random.choice(business_type)
                email = random.choice(company_contact) + '@' + name.replace(' ', random.choice(white_place_changer)) + random.choice(extension)
            values = {
                'name': name,
                'company_type': company_type,
                # Generates a number with a length of 10 digits.
                'phone': random.randrange(100000000,999999999),
                'email': email
            }
            model_proxy.create(values)
            if show_generated_records_in_terminal:
                print(str(values))
        elapsed_time = time.time() - start_time
        print('We\'ve imported ' + str(number_of_recs) + ' records in the model \'res.partner\' in ' + str(elapsed_time) + ' seconds.')

