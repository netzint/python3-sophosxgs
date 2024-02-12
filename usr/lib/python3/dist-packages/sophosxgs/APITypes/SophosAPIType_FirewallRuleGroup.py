class SophosAPIType_FirewallRuleGroup():

    POLICYTYPE_USERNETWORK = "User/network rule"
    POLICYTYPE_NETWORK = "Network rule"
    POLICYTYPE_USER = "User rule"
    POLICYTYPE_WAF = "WAF rule"
    POLICYTYPE_ANY = "Any"

    def __init__(self, name:str, description:str="", policytype:str=POLICYTYPE_ANY, securitypolicylist:list=None, sourcezonelist:list=None, destinationzonelist:list=None) -> None:
        """
        :param name: Name of the zone
        :type name: str
        :param description: Description of this zone
        :type description: str
        :param securitypolicylist: List of Name frtom firewallrules to add
        :type securitypolicylist: list[str]
        :param sourcezonelist: List of source zones
        :type sourcezonelist: list[str]
        :param destinationzonelist: List of destination zones
        :type destinationzonelist: list[str]
        """
        self.name = name
        self.description = description
        self.policytype = policytype
        self.securitypolicylist = securitypolicylist
        self.sourcezonelist = sourcezonelist
        self.destinationzonelist = destinationzonelist

    def getXML(self) -> str:
        xml =  f"""<Name>{self.name}</Name>
            <Description>{self.description}</Description>
            <Policytype>{self.policytype}</Policytype>"""
        
        if self.securitypolicylist:
            xml += "<SecurityPolicyList>"
            for securitypolicy in self.securitypolicylist:
                xml += f"<SecurityPolicy>{securitypolicy}</SecurityPolicy>"
            xml += "</SecurityPolicyList>"

        if self.sourcezonelist:
            xml += "<SourceZones>"
            for sourcezone in self.sourcezonelist:
                xml += f"<Zone>{sourcezone}</Zone>"
            xml += "</SourceZones>"

        if self.destinationzonelist:
            xml += "<DestinationZones>"
            for destinationzone in self.destinationzonelist:
                xml += f"<Zone>{destinationzone}</Zone>"
            xml += "</DestinationZones>"
            
        return xml