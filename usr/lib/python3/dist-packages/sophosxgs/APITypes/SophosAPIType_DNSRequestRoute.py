class SophosAPIType_DNSRequestRoute():

    def __init__(self, domain, dnsserver) -> None:
        self.domain: str = domain
        self.dnsserver: str = dnsserver

    def getXML(self) -> str:
        xml =  f"""
        <DomainName>{self.domain}</DomainName>
		<TargetServers>
			<Host>{self.dnsserver}</Host>
		</TargetServers>"""

        return xml