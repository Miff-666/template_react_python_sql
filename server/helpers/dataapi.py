# v1.0
#   - init
#   - login
#   - logout
#   - get_call_leg_report
#
# v1.1
#   - get_account
#   - get_sip_lines
import requests
import json


class Dataapi:
    _url = "https://dataapi.uiscom.ru/v2.0"
    is_auth = False
    session = None
    app_id = None
    expire_at = None
    last_request = None

    def __init__(self, token=None, user=None, password=None):
        self.access_token = token
        self.user = user
        self.password = password
        self.session = requests.Session()
        if (user is not None and password is not None):
            self.login()

    async def login(self, user=None, password=None, token=None):
        if (user is not None and password is not None):
            self.access_token = token
            self.user = user
        elif (self.user is None and self.password is None):
            self.is_auth = False
            return False
        else:
            json_request = {
                "jsonrpc": "2.0",
                "id": "req1",
                "method": "login.user",
                "params": {
                    "login": self.user,
                    "password": self.password
                }
            }
            response = self.session.post(self._url, json=json_request)
            if response.status_code == 200:
                response_json = json.loads(response.content)
                tkn = response_json['result']['data']['access_token']
                self.access_token = tkn
                self.app_id = response_json['result']['data']['app_id']
                self.expire_at = response_json['result']['data']['expire_at']
                self.is_auth = True
                return True
            else:
                return False
            pass

    async def logout(self):
        if self.is_auth is not None:
            json_request = {
                "jsonrpc": "2.0",
                "id": "req1",
                "method": "logout.user",
                "params": {
                    "access_token": self.access_token
                }
            }
            response = self.session.post(self._url, json=json_request)
            if response.status_code == 200:
                self.token = self.app_id = self.expire_at = None
                self.is_auth = False
                return True

    async def get_call_leg_report(self, session_id, start_time, finish_time):
        try:
            json_request = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "get.call_legs_report",
                "params":
                {
                    "filter": {
                        "field": "call_session_id",
                        "operator": "=",
                        "value": session_id
                    },
                    "fields": [
                        "id",
                        "called_phone_number",
                        "calling_phone_number",
                        "virtual_phone_number",
                        "employee_id",
                        "employee_full_name",
                        "is_operator",
                        "call_records",
                        "duration",
                        "total_duration",
                        "direction",
                        "is_transfered",
                        "is_talked"
                    ],
                    "access_token": self.access_token,
                    "date_from": start_time,
                    "date_till": finish_time
                }
            }
            self.last_request = json_request
            response = self.session.post(self._url, json=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        except Exception:
            return None

    async def get_account(self):
        try:
            json_request = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "get.account",
                "params":
                {
                    "access_token": self.access_token,
                }
            }
            self.last_request = json_request
            response = self.session.post(self._url, json=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        except Exception:
            return None

    async def get_employees_ext(self, ext, log=None):
        try:
            json_request = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "get.employees",
                "params":
                {
                    "access_token": self.access_token,
                    "filter": {
                        "field": "extension",
                        "operator": "jsquery",
                        "value": "extension_phone_number=\"" + ext + "\""
                    },
                    "fields": [
                        "id"
                    ]
                }
            }
            self.last_request = json_request
            response = self.session.post(self._url, json=json_request)
            if log is not None:
                await log(
                    dataapi_response=response.content,
                    dataapi_request=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        except Exception:
            return None
    
    async def get_employees_id(self, id_user, log=None):
        try:
            json_request = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "get.employees",
                "params":
                {
                    "access_token": self.access_token,
                    "filter": {
                        "field": "id",
                        "operator": "=",
                        "value": id_user
                    },
                    "fields": [
                        "extension"
                    ]
                }
            }
            response = self.session.post(self._url, json=json_request)
            if log is not None:
                await log(
                    dataapi_response=response.content,
                    dataapi_request=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        except Exception:
            return None

    async def get_sip_lines_employee_id(self, employee_id, log=None):
        try:
            json_request = {
                "jsonrpc": "2.0",
                "id": "number",
                "method": "get.sip_lines",
                "params": {
                    "access_token": self.access_token,
                    "filter": {
                        "field": "employee_id",
                        "operator": "=",
                        "value": employee_id
                    },
                    "fields": [
                        "physical_state",
                        "virtual_phone_number",
                        "type",
                        "virtual_phone_number"
                    ]
                }
            }
            self.last_request = json_request
            response = self.session.post(self._url, json=json_request)
            if log is not None:
                await log(
                    dataapi_response=response.content,
                    dataapi_request=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        except Exception:
            return None
