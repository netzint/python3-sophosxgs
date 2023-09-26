class SophosAPIType_IPHostGroup():

    IPFAMILY_IPV4 = "IPv4"
    IPFAMILY_IPV6 = "IPv6"

    def __init__(self, name, ipfamily, description=None, hostlist=None) -> None:
        """
        :param name: Name of the iphost
        :type name: str
        :param ipfamily: Currently only IPv4 and IPv6
        :type ipfamily: str
        :param description: Description of thi hostgroup
        :type description: str
        :param hostlist: List of host should be member of this group
        :type hostlist: list[str]
        """
        self.name = name
        self.ipfamily = ipfamily
        self.description = description
        self.hostlist = hostlist

    def getXML(self):
        xml =  f"""<Name>{self.name}</Name>
            <IPFamily>{self.ipfamily}</IPFamily>"""
        
        if self.description:
            xml += f"<Description>{self.description}</Description>"
        
        if self.hostlist:
            xml += "<HostList>"
            for host in self.hostlist:
                xml += f"<Host>{host}</Host>"
            xml += "</HostList>"
            
        return xml