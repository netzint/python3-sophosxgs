class SophosAPIType_DHCPServer():

    def __init__(self, name, interface, dhcp_start, dhcp_end, netmask, gateway, dns1) -> None:
        self.name: str = name
        self.interface: str = interface
        self.dhcp_start: str = dhcp_start
        self.dhcp_end: str = dhcp_end
        self.netmask: str = netmask
        self.gateway: str = gateway
        self.dns1: str = dns1

    def getXML(self) -> str:
        xml =  f"""
        <Name>{self.name}</Name>
        <Status>1</Status>
        <Interface>{self.interface}</Interface>
        <IPLease>
        <IP>{self.dhcp_start}-{self.dhcp_end}</IP>
        </IPLease>
        <ConflictDetection>Disable</ConflictDetection>
        <LeaseForRelay>Disable</LeaseForRelay>
        <SubnetMask>{self.netmask}</SubnetMask>
        <DomainName/>
        <DefaultLeaseTime>1440</DefaultLeaseTime>
        <MaxLeaseTime>2880</MaxLeaseTime>
        <UseApplianceDNSSettings>Disable</UseApplianceDNSSettings>
        <PrimaryDNSServer>{self.dns1}</PrimaryDNSServer>
        <SecondaryDNSServer/>
        <PrimaryWINSServer/>
        <SecondaryWINSServer/>
        <Gateway>{self.gateway}</Gateway>
        <UseInterfaceIPasGateway>UseInterfaceIPAsGateway</UseInterfaceIPasGateway>"""

        return xml