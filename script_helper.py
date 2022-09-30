# This file is intented to organize the required calls and utilities in
# Python classes. These classes are imported into the app.py for cleaner
# code and better breakdown of the functionality    

# Bb-rest-helper imports.
from Bb_rest_helper import Bb_Utils
from Bb_rest_helper import Get_Config
from Bb_rest_helper import Auth_Helper
from Bb_rest_helper import Bb_Requests
# Other imports
import os
import requests
from requests import HTTPError
import json
import logging
import time
import datetime
import csv

class Helper:

    # This method initializes the Donwloader class, by default handles all that is needed
    # for authentication logging and utils. No arguments are needed.
    def __init__(self):
        # remove logging for pruduction
        #self.utils = Bb_Utils()
        #self.utils.set_logging()
        self.conf = Get_Config('./credentials/learn_config.json')
        self.learn_url = self.conf.get_url()
        self.learn_token = None
        self.reqs = Bb_Requests()

    # Method that returns True when the token expires.
    def token_is_expired(self, expiration_datetime):
        time_left = (expiration_datetime -
                     datetime.datetime.now()).total_seconds()
        if time_left < 1:
            time.sleep(1)
            return True
        else:
            return False

    # Using this method instead of default for Bb-rest-helper auth to better handle
    # token expiration, this will be updated in the library so this method is not needed.
    def authenticate(self):
        self.endpoint = "/learn/api/public/v1/oauth2/token"
        self.params = {"grant_type": "client_credentials"}
        self.headers = {
            'Content-Type': "application/x-www-form-urlencoded"}

        try:
            if self.learn_token == None:
                
                r = requests.request(
                    "POST",
                    self.learn_url +
                    self.endpoint,
                    headers=self.headers,
                    params=self.params,
                    auth=(
                        self.conf.get_key(),
                        self.conf.get_secret()))
                r.raise_for_status()
                self.data = json.loads(r.text)
                self.learn_token = self.data["access_token"]
                self.expires = self.data["expires_in"]
                m, s = divmod(self.expires, 60)
                self.now = datetime.datetime.now()
                self.expires_at = self.now + \
                    datetime.timedelta(seconds=s, minutes=m)
                logging.info("Learn Authentication successful")
                logging.info("Token expires at: " + str(self.expires_at))
                # return self.learn_token

            elif self.token_is_expired(self.expires_at):
                r = requests.request(
                    "POST",
                    self.learn_url +
                    self.endpoint,
                    headers=self.headers,
                    params=self.params,
                    auth=(
                        self.conf.get_key(),
                        self.conf.get_secret()))
                r.raise_for_status()
                self.data = json.loads(r.text)
                self.learn_token = self.data["access_token"]
                self.expires = self.data["expires_in"]
                m, s = divmod(self.expires, 60)
                self.now = datetime.datetime.now()
                self.expires_at = self.now + \
                    datetime.timedelta(seconds=s, minutes=m)
                logging.info("Learn Authentication successful")
                logging.info("Token expires at: " + str(self.expires_at))

        except requests.exceptions.HTTPError as e:
            data = json.loads(r.text)
            logging.error(data["error_description"])

    # This method returns a list with all the Ultra courses in the target system, due to pagination this method
    # can take time to run. No arguments are needed.
    def get_courses_ultra(self):
        self.endpoint = '/learn/api/public/v3/courses'
        self.params = {
            'fields': 'id,externalId,name,ultraStatus',
            'organization': False
        }
        self.data = self.reqs.Bb_GET(
            self.learn_url,
            self.endpoint,
            self.learn_token,
            self.params)
        self.ultra_course_list = []
        self.original_course_list = []
        for self.d in (self.data):
            if self.d['ultraStatus'] == "Ultra":
                self.ultra_course_list.append(self.d)
        return self.ultra_course_list

    def get_LTI_content_ultra(self, course_id: str):
        self.endpoint = f'/learn/api/public/v1/courses/{course_id}/contents'
        self.params = {
            'contentHandler': 'resource/x-bb-blti-link',
            'fields':'title,created,modified,availability.available'
            }
        self.data = self.reqs.Bb_GET(
            self.learn_url,
            self.endpoint,
            self.learn_token,
            self.params)
        return self.data

        