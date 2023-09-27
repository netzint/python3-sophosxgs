class SophosAPIType_VLAN():

    IPV4ASSIGNMENT_STATIC = "Static"
    #IPV4ASSIGNMENT_PPPOE = "PPPoE" ## not implementet jet
    IPV4ASSIGNMENT_DHCP = "DHCP"

    def __init__(self, name:str, interface:str, zone:str, vlanid:int, ipv4configuration:bool, ipv4assignment:str, ipaddress:str=None, netmask:str=None, gatewayname:str=None, gatewayaddress:str=None) -> None:
        """
        :param name: Name of the VLAN
        :type name: str
        :param interface: Name of Port-Interface eg.: Port1-8, PortA1-4, PortF1-4 or PortMGMT
        :type interface: str
        :param zone: Name of the zone
        :type zone: str
        :param vlanid: VLAN ID
        :type vlanid: int
        :param ipv4configuration: Interface should have an ipv4 configuration
        :type ipv4configuration: bool
        :param ipv4assignment: IP assignment type. Currently only Static and DHCP. PPPoE work in process
        :type ipv4assignment: str
        :param ipaddress: IP address of this interface (optional)
        :type ipaddress: str
        :param netmask: Netmask of this interface (optional)
        :type netmask: str
        :param gatewayname: Name of the gateway if is WAN(optional)
        :type gatewayname: str
        :param gatewayaddress: IP of the gateway if is WAN (optional)
        :type gatewayaddress: str
        """
        self.name = name
        self.interface = interface
        self.zone = zone
        self.vlanid = vlanid
        self.ipv4configuration = ipv4configuration
        self.ipv4assignment = ipv4assignment
        self.ipaddress = ipaddress
        self.netmask = netmask
        self.gatewayname = gatewayname
        self.gatewayaddress = gatewayaddress

    def __getValue(self, service):
        if service:
            return "Enable"
        return "Disable"

    def getXML(self) -> str:
        xml =  f"""<Name>{self.name}</Name>
            <Hardware>{self.interface}.{self.vlanid}</Hardware>
            <Interface>{self.interface}</Interface>
            <Zone>{self.zone}</Zone>
            <VLANID>{str(self.vlanid)}</VLANID>
            <IPv4Configuration>{self.__getValue(self.ipv4configuration)}</IPv4Configuration>
            <IPv4Assignment>{self.ipv4assignment}</IPv4Assignment>
            <IPAddress>{self.ipaddress}</IPAddress>
            <Netmask>{self.netmask}</Netmask>"""
        
        if self.gatewayname and self.gatewayaddress:
            xml += f"""
                <GatewayName>{self.gatewayname}</GatewayName>
                <GatewayAddress>{self.gatewayaddress}</GatewayAddress>"""

        return xml