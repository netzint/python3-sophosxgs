class SophosAPIType_UserStatus():

    USERSTATUS_ACTIVATE="ActivateUser"
    USERSTATUS_DEACTIVATE="DeactivateUser"

    def __init__(self, userstatus:str, users:list) -> None:
        self.userstatus: str = userstatus
        self.users: list = users
        
    def getXML(self) -> str:
        xml = ""

        for user in self.users:
            xml += f"<{self.userstatus}>{user}</{self.userstatus}>"

        return xml