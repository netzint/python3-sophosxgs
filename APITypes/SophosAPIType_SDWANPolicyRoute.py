class SophosAPIType_SDWANPolicyRoute():

    IPFAMILY_IPV4 = "IPv4"
    IPFAMILY_IPV6 = "IPv6"

    def __init__(self, name: str, description: str, interface: str, sourcenetwork: str, destinationnetwork: str, gateway: str, ipfamily: str = IPFAMILY_IPV4) -> None:
        self.name: str = name
        self.description: str = description
        self.interface: str = interface
        self.sourcenetwork: str = sourcenetwork
        self.destinationnetwork: str = destinationnetwork
        self.gateway: str = gateway
        self.ipfamily: str = ipfamily


    def getXML(self) -> str:
        xml =  f"""
        <Name>{self.name}</Name>
        <Description>{self.description}</Description>
        <IPFamily>{self.ipfamily}</IPFamily>
        <Interface>{self.interface}</Interface>
        <DSCPMarking>-1</DSCPMarking>
        <LinkSelection>SelectGateways</LinkSelection>
        <SourceNetworks>
        <Network>{self.sourcenetwork}</Network>
        </SourceNetworks>
        <DestinationNetworks>
        <Network>{self.destinationnetwork}</Network>
        </DestinationNetworks>
        <Healthcheck>OFF</Healthcheck>
        <Status>1</Status>
        <Gateway>{self.gateway}</Gateway>
        <BackupGateway/>
        """
        
        return xml