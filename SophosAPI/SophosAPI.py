import requests
import xmltodict

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

    def __requestAPI(self, request):
        print(request)
        data = {
            "reqxml": "<Request>" + self.loginXML + request + "</Request>"
        }
        request = requests.post(self.requestURL, data=data, verify=False)
        return SophosAPIRequest(request)

    def get(self, sophosapitype):
        request = "<Get><" + sophosapitype + "></" + sophosapitype + "></Get>"
        return self.__requestAPI(request)
    
    def add(self, sophosapitype, object):
        request = "<Set operation=\"add\"><" + sophosapitype + ">" + object.getXML() + "</" + sophosapitype + "></Set>"
        return self.__requestAPI(request)
    
    def update(self, sophosapitype, object):
        request = "<Set operation=\"update\"><" + sophosapitype + ">" + object.getXML() + "</" + sophosapitype + "></Set>"
        return self.__requestAPI(request)
    
    def remove(self, sophosapitype, name):
        request = "<Remove><" + sophosapitype + "><Name>" + name + "</Name></" + sophosapitype + "></Remove>"
        return self.__requestAPI(request)

class SophosAPIRequest():

    def __init__(self, requestsResponse) -> None:
        self.requestsResponse = requestsResponse
        self.xml = self.requestsResponse.text.split("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")[1].strip().replace("\x00", "")

    def __str__(self) -> str:
        return str(self.get())

    def getStatus(self) -> int:
        return self.requestsResponse.status_code

    def getXML(self) -> str:
        return self.xml

    def get(self) -> dict:
        return xmltodict.parse(self.xml)