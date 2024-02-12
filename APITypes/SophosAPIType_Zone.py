class SophosAPIType_Zone():

    TYPE_LAN = "LAN"
    TYPE_DMZ = "DMZ"

    def __init__(self, name, type, description="", applianceaccess=None) -> None:
        """
        :param name: Name of the zone
        :type name: str
        :param type: Currently only LAN and DMZ
        :type type: str
        :param description: Description of this zone
        :type description: str
        :param applianceaccess: Sophos API Applicationaccess
        :type applianceaccess: SophosAPIType_Zone_ApplianceAccess
        """
        self.name: str = name
        self.type = type
        self.description = description
        self.applianceaccess = applianceaccess

    def getXML(self) -> str:
        xml =  f"""<Name>{self.name}</Name>
            <Type>{self.type}</Type>
            <Description>{self.description}</Description>"""

        if not self.applianceaccess:
            self.applianceaccess = SophosAPIType_Zone_ApplianceAccess()
        xml += self.applianceaccess.getXML()       
            
        return xml
    
class SophosAPIType_Zone_ApplianceAccess:

    def __init__(self, adminservice_http=False, adminservice_https=False, adminservice_telnet=False, adminservice_ssh=False,
                 auth_client=False, auth_captiveportal=False, auth_ntlm=False, auth_radiussso=False,
                 network_dns=False, network_ping=False,
                 other_webproxy=False, other_sslvpn=False, other_userportal=False, other_dynamicrouting=False, other_smtprelay=False, other_snmp=False) -> None:
        
        self.adminservice_http = adminservice_http
        self.adminservice_https = adminservice_https
        self.adminservice_telnet = adminservice_telnet
        self.adminservice_ssh = adminservice_ssh
        self.auth_client = auth_client
        self.auth_captiveportal = auth_captiveportal
        self.auth_ntlm = auth_ntlm
        self.auth_radiussso = auth_radiussso
        self.network_dns = network_dns
        self.network_ping = network_ping
        self.other_webproxy = other_webproxy
        self.other_sslvpn = other_sslvpn
        self.other_userportal = other_userportal
        self.other_dynamicrouting = other_dynamicrouting
        self.other_smtprelay = other_smtprelay
        self.other_snmp = other_snmp

    def __getValue(self, service):
        if service:
            return "Enable"
        return "Disable"

    def getXML(self) -> str:
        xml = f"""
            <ApplianceAccess>
                <AdminServices>
                    <HTTP>{self.__getValue(self.adminservice_http)}</HTTP>
                    <HTTPS>{self.__getValue(self.adminservice_https)}</HTTPS>
                    <Telnet>{self.__getValue(self.adminservice_telnet)}</Telnet>
                    <SSH>{self.__getValue(self.adminservice_ssh)}</SSH>
                </AdminServices>
                <AuthenticationServices>
                    <ClientAuthentication>{self.__getValue(self.auth_client)}</ClientAuthentication>
                    <CaptivePortal>{self.__getValue(self.auth_captiveportal)}</CaptivePortal>
                    <NTLM>{self.__getValue(self.auth_ntlm)}</NTLM>
                    <RadiusSSO>{self.__getValue(self.auth_radiussso)}</RadiusSSO>
                </AuthenticationServices>
                <NetworkServices>
                    <DNS>{self.__getValue(self.network_dns)}</DNS>
                    <Ping>{self.__getValue(self.network_ping)}</Ping>
                </NetworkServices>
                <OtherServices>
                    <WebProxy>{self.__getValue(self.other_webproxy)}</WebProxy>
                    <SSLVPN>{self.__getValue(self.other_sslvpn)}</SSLVPN>
                    <UserPortal>{self.__getValue(self.other_userportal)}</UserPortal>
                    <DynamicRouting>{self.__getValue(self.other_dynamicrouting)}</DynamicRouting>
                    <SMTPRelay>{self.__getValue(self.other_smtprelay)}</SMTPRelay>
                    <SNMP>{self.__getValue(self.other_snmp)}</SNMP>
                </OtherServices>
            </ApplianceAccess>
            """
        return xml
        