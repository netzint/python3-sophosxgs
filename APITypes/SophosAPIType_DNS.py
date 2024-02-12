class SophosAPIType_DNS():

    def __init__(self, dns1, dns2="", dns3="") -> None:
        self.dns1: str = dns1
        self.dns2: str = dns2
        self.dns3: str = dns3

    def getXML(self) -> str:
        xml =  f"""
        <IPv4Settings>
        <ObtainDNSFrom>Static</ObtainDNSFrom>
        <DNSIPList>
            <DNS1>{self.dns1}</DNS1>
            <DNS2>{self.dns2}</DNS2>
            <DNS3>{self.dns3}</DNS3>
        </DNSIPList>
        </IPv4Settings>
        <IPv6Settings>
        <ObtainDNSFrom>Static</ObtainDNSFrom>
        <DNSIPList>
            <DNS1/>
            <DNS2/>
            <DNS3/>
        </DNSIPList>
        </IPv6Settings>
        <DNSQueryConfiguration>ChooseServerBasedOnIncomingRequestsRecordType</DNSQueryConfiguration>"""

        return xml