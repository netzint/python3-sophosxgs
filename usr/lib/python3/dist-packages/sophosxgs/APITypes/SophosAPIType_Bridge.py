class SophosAPIType_Bridge():

    def __init__(self, name, hardware, bridgemembers, ip_assignment, ip, netmask, description="", routingonbridgepair=True) -> None:
        self.name: str = name
        self.hardware: str = hardware
        self.bridgemembers: list = bridgemembers
        self.ip_assignment: str = ip_assignment
        self.ip: str = ip
        self.netmask: str = netmask
        self.description: str = description
        self.routingonbridgepair: str = routingonbridgepair


    def getXML(self) -> str:
        xml =  f"""
            <Name>{self.name}</Name>
            <Hardware>{self.hardware}</Hardware>
            <Description>{self.description}</Description>
            <RoutingOnBridgePair>{self.__getValue(self.routingonbridgepair)}</RoutingOnBridgePair>"""
        
        xml += "<BridgeMembers>"

        for bridgemember in self.bridgemembers:
            xml += f"""
                <Member>
                    <Interface>{bridgemember["interface"]}</Interface>
                    <Zone>{bridgemember["zone"]}</Zone>
                </Member>"""
            
        xml += "</BridgeMembers>"

        xml += f"""
            <IPv4Configuration>Enable</IPv4Configuration>
            <IPv4Assignment>{self.ip_assignment}</IPv4Assignment>
            <IPAddress>{self.ip}</IPAddress>
            <Netmask>{self.netmask}</Netmask>
            <MTU>1500</MTU>
            <MSS>
                <Override>Disable</Override>
                <MSSValue>1460</MSSValue>
            </MSS>"""
     
        return xml
    
    def __getValue(self, service):
        if service:
            return "Enable"
        return "Disable"