# This file is intented to organize the required calls and utilities in
# Python classes. These classes are imported into the app.py for cleaner
# code and better breakdown of the functionality    

# Bb-rest-helper imports.
from Bb_rest_helper import Bb_Utils
from Bb_rest_helper import Get_Config
from Bb_rest_helper import Auth_Helper
from Bb_rest_helper import Bb_Requests
# Other imports

class Helper:

    # This method initializes the Helper class, by default handles all that is needed
    # for authentication, logging, requests and utils. No arguments are needed.
    def __init__(self):

        self.utils = Bb_Utils()
        self.utils.set_logging()
        self.quick_auth_learn = self.utils.quick_auth(
            './credentials/config.json', 'Learn')
        self.learn_token = self.quick_auth_learn['token']
        self.learn_url = self.quick_auth_learn['url']
        self.reqs = Bb_Requests()

    # Other methods.
    def helper_method(self):
        pass
    
