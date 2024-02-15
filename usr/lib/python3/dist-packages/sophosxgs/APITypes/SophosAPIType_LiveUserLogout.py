class SophosAPIType_LiveUserLogin():

    DEVICETYPE_IOS = "iOS"
    DEVICETYPE_ANDROID = "Android"

    def __init__(self, username, ip) -> None:
        self.username = username
        self.ip = ip

    def getXML(self) -> str:
        xml =  f"""
		<UserName>{self.username}</UserName>
		<IPAddress>{self.ip}</IPAddress>"""

        return xml