class SophosAPIType_GatewayHost():

    IPFAMILY_IPV4 = "IPv4"
    IPFAMILY_IPV6 = "IPv6"

    def __init__(self, name: str, gatewayip: str, interface: str, ipfamily: str = IPFAMILY_IPV4) -> None:
        self.name: str = name
        self.ipfamily: str = ipfamily
        self.gatewayip: str = gatewayip
        self.interface: str = interface


    def getXML(self) -> str:
        xml =  f"""<Name>{self.name}</Name>
        <IPFamily>{self.ipfamily}</IPFamily>
        <GatewayIP>{self.gatewayip}</GatewayIP>
        <Interface>{self.interface}</Interface>
        <NetworkZone/>
        <Healthcheck>ON</Healthcheck>
        <MailNotification>OFF</MailNotification>
        <Interval>60</Interval>
        <FailureRetries>3</FailureRetries>
        <Timeout>2</Timeout>
        <MonitoringCondition>
        <Rule>
            <Protocol>PING</Protocol>
            <Port>*</Port>
            <IPAddress>{self.gatewayip}</IPAddress>
            <Condition/>
        </Rule>
        </MonitoringCondition>"""

        return xml