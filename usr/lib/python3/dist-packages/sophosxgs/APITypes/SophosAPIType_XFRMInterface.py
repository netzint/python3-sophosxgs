class SophosAPIType_XFRMInterface():

    def __init__(self, name:str, interface:str, tunnelname:str, ipv4configuration:bool, ipaddress:str=None, netmask:str=None) -> None:
        """
        :param name: Name of the VLAN
        :type name: str
        :param interface: Name of Port-Interface eg.: Port1-8, PortA1-4, PortF1-4 or PortMGMT
        :type interface: str
        :param tunnelname: Name of tunnel
        :type tunnelname: str
        :param ipv4configuration: Interface should have an ipv4 configuration
        :type ipv4configuration: bool
        :param ipaddress: IP address of this interface (optional)
        :type ipaddress: str
        :param netmask: Netmask of this interface (optional)
        :type netmask: str
        """
        self.name = name
        self.interface = interface
        self.tunnelname = tunnelname
        self.ipv4configuration = ipv4configuration
        self.ipaddress = ipaddress
        self.netmask = netmask

    def __getValue(self, service):
        if service:
            return "Enable"
        return "Disable"

    def getXML(self) -> str:
        xml =  f"""<Hardware>{self.interface}</Hardware>
            <Name>{self.name}</Name>
            <Connectionname>{self.tunnelname}</Connectionname>
            <IPv4Configuration>{self.__getValue(self.ipv4configuration)}</IPv4Configuration>
            <MTU>1400</MTU>
            <MSS>
                <OverrideMSS>Disable</OverrideMSS>
            <MSSValue>1360</MSSValue>
            </MSS>
            <IPv4Address>{self.ipaddress}</IPv4Address>
            <Netmask>{self.netmask}</Netmask>"""

        return xml