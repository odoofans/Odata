# We'll add the path to the directory above this one so we can import the Models folder.
import sys
sys.path.append('..')
from Models.Contact import Contact
import erppeek

class contact_test(object):
    def test_contact_creation():
        # Order: client, model, show_generated_records_in_terminal, number_of_recs
        """
            Create client object to connect through XML-RPC:
            client = erppeek.Client('http://IP:OdooPortNumber', 'DatabaseName', 'DatabaseUsername', 'DatabasePassword')
            Create an object (instance):
            contact = Contact()
            Call the function to generate records. client is the above object, 'modelName', print output in terminal or not, amount of records) 
            contact.generate_res_partner_contacts(client, 'your.model', True, 1)
        """
        client = erppeek.Client('http://localhost:9999', 'example', 'admin', 'admin')
        contact = Contact()
        contact.generate_contacts(client, True, 1)

    test_contact_creation()

