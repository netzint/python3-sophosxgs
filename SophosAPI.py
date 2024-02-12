import requests
import xmltodict
import json

import xml.etree.ElementTree as ET

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class SophosAPI():

    def __init__(self, url, port, username, password) -> None:
        self.url = url
        self.port = str(port)
        self.username = username
        self.password = password

        self.requestURL = "https://" + self.url + ":" + self.port + "/webconsole/APIController"
        self.loginXML = "<Login><Username>" + self.username + "</Username><Password>" + self.password + "</Password></Login>"

    def __requestAPI(self, request, sophosapitype=None):
        data = {
            "reqxml": "<Request>" + self.loginXML + request + "</Request>"
        }
        request = requests.post(self.requestURL, data=data, verify=False)
        return SophosAPIRequest(request, sophosapitype)
    
    def rawRequest(self, request):
        return self.__requestAPI(request)

    def get(self, sophosapitype):
        request = "<Get><" + sophosapitype + "></" + sophosapitype + "></Get>"
        return self.__requestAPI(request, sophosapitype)
    
    def add(self, sophosapitype, object):
        request = "<Set operation=\"add\"><" + sophosapitype + ">" + object.getXML() + "</" + sophosapitype + "></Set>"
        return self.__requestAPI(request, sophosapitype)
    
    def update(self, sophosapitype, object):
        request = "<Set operation=\"update\"><" + sophosapitype + ">" + object.getXML() + "</" + sophosapitype + "></Set>"
        return self.__requestAPI(request, sophosapitype)
    
    def set(self, sophosapitype, object):
        request = "<Set><" + sophosapitype + ">" + object.getXML() + "</" + sophosapitype + "></Set>"
        return self.__requestAPI(request, sophosapitype)
    
    def remove(self, sophosapitype, name):
        request = "<Remove><" + sophosapitype + "><Name>" + name + "</Name></" + sophosapitype + "></Remove>"
        return self.__requestAPI(request, sophosapitype)
    
    def activate(self, sophosapitype, object):
        request = "<Set operation=\"update\"><" + sophosapitype + ">" + object.getActivationXML() + "</" + sophosapitype + "></Set>"
        return self.__requestAPI(request, sophosapitype)
    
    def test(self):
        request = "<Get><IPHost></IPHost></Get>"
        return self.__requestAPI(request).getLogin()

class SophosAPIRequest():

    def __init__(self, requestsResponse, sophosapitype=None) -> None:
        self.requestsResponse = requestsResponse
        self.xml = self.requestsResponse.text.split("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")[1].strip().replace("\x00", "")
        self.data = xmltodict.parse(self.xml)
        self.sophosapitype = sophosapitype

    def __str__(self) -> str:
        return str(self.get())

    def getHTTPStatus(self) -> int:
        return self.requestsResponse.status_code
    
    def getStatusCode(self) -> int:
        if self.sophosapitype:
            return int(self.data["Response"][self.sophosapitype]["Status"]["@code"])
        return 0
    
    def getStatus(self) -> bool:
        if self.sophosapitype:
            if int(self.data["Response"][self.sophosapitype]["Status"]["@code"]) < 300:
                return True
        return False
    
    def getErrorText(self) -> bool:
        if self.sophosapitype:
            return self.data["Response"][self.sophosapitype]["Status"]["#text"]
        return False

    def getLogin(self) -> bool:
        if "Login" in self.data["Response"]:
            if "Authentication Successful" in self.data["Response"]["Login"]['status']:
                return True
        return False

    def getXML(self) -> str:
        return self.xml
    
    def getJSONString(self) -> str:
        return json.dumps(self.get())

    def get(self) -> dict:
        if self.sophosapitype:
            return self.data["Response"][self.sophosapitype]
        return self.data