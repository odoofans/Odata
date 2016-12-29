import time
import erppeek
import names

class Project(object):
    def __init__(self):
        """
            Wrapper
        """

    def generate_projects(self, client, show_generated_records_in_terminal, number_of_recs):
        start_time = time.time()
        model_proxy = client.model('project.project')
        values = ({
            'name': names.get_full_name()
        })

        model_proxy.create(values)
        if show_generated_records_in_terminal:
            print(str(values))

        elapsed_time = time.time() - start_time
        print('We\'ve imported ' + str(number_of_recs) + ' records in the model \'project.project\' in ' + str(elapsed_time) + ' seconds.')
