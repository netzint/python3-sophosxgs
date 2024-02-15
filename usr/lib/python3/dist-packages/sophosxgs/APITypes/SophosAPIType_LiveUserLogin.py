class SophosAPIType_LiveUserLogin():

    DEVICETYPE_IOS = "iOS"
    DEVICETYPE_ANDROID = "Android"

    def __init__(self, username, ip, mac="", groupname="", devicetype="") -> None:
        self.username = username
        self.ip = ip
        self.mac = mac
        self.groupname = groupname
        self.devicetype = devicetype

    def getXML(self) -> str:
        xml =  f"""
		<UserName>{self.username}</UserName>
		<IPAddress>{self.ip}</IPAddress>"""

        if self.mac != "":
		    xml += f"<MacAddress>{self.mac}</MacAddress>"

        if self.groupname != "":
		    xml += f"<GroupName>{self.groupname}</GroupName>"

        if self.devicetype != "":
		    xml += f"<DeviceType>{self.devicetype}</DeviceType>"

        return xml