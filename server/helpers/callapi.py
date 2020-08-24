# v1.0
#   - init
#   - list_calls
#   - start.employee_call
import requests
import json


class Callapi:
    _url = "https://callapi.uiscom.ru/v4.0"
    is_auth = False
    session = None
    expire_at = None
    last_request = None

    def __init__(self, token=None, user=None, password=None):
        self.access_token = token
        self.user = user
        self.password = password
        self.session = requests.Session()

    async def release_call(self, call_id, token=None):
        if token is not None:
            self.access_token = token
        if self.access_token is not None:
            json_request = {
                "jsonrpc": "2.0",
                "id": "req1",
                "method": "release.call",
                "params": {
                    "access_token": self.access_token,
                    "call_session_id": int(call_id)
                }
            }
            response = self.session.post(self._url, json=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        else:
            return None

    async def list_calls(self, token=None, direction=None, virtual_phone_number=None):
        if token is not None:
            self.access_token = token
        if self.access_token is not None:
            json_request = {
                "jsonrpc": "2.0",
                "id": "req1",
                "method": "list.calls",
                "params": {
                    "access_token": self.access_token
                }
            }
            if direction is not None:
                json_request['params']['direction'] = direction
            if virtual_phone_number is not None:
                json_request['params']['virtual_phone_number'] = virtual_phone_number
            response = self.session.post(self._url, json=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        else:
            return None

    async def start_employee_call(
            self,
            id_user,
            call_num,
            v_num,
            token=None,
            log=None):
        if token is not None:
            self.access_token = token
        if self.access_token is not None:
            json_request = {
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "start.employee_call",
                            "params": {
                                "access_token": self.access_token,
                                "first_call": "employee",
                                "virtual_phone_number": v_num,
                                "direction": "out",
                                "show_virtual_phone_number": False,
                                "contact": call_num,
                                "employee": {
                                    "id": id_user
                                }
                                }
                            }
            response = self.session.post(self._url, json=json_request)
            if log is not None:
                await log(
                    callapi_response=response.content,
                    callapi_request=json_request)
            if response.status_code == 200:
                return json.loads(response.content)
        else:
            return None
