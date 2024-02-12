class SophosAPIType_User():

    def __init__(self, username, name, group) -> None:
        self.username: str = username
        self.name: str = name
        self.group: str = group

    def getXML(self) -> str:
        xml =  f"""
        <Username>{self.username}</Username>
        <Name>{self.name}</Name>
        <Group>{self.group}</Group>
        <LoginRestriction>UserGroupNode</LoginRestriction>
        """

        return xml