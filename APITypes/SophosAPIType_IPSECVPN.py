class SophosAPIType_IPSECVPN():

    CONNECTIONTYPE_RemoteAccess = "RemoteAccess"
    CONNECTIONTYPE_SiteToSite = "SiteToSite"
    CONNECTIONTYPE_HostToHost = "HostToHost"
    CONNECTIONTYPE_TunnelInterface = "TunnelInterface"

    ActionOnVPNRestart_Disable = "Disable"
    ActionOnVPNRestart_RespondOnly = "RespondOnly"
    ActionOnVPNRestart_Initiate = "Initiate"

    AuthenticationType_PresharedKey = "PresharedKey"
    AuthenticationType_DigitalCertificate = "DigitalCertificate"
    AuthenticationType_RSAKey = "RSAKey"

    def __init__(self, name:str, description:str="", connectiontype:str=CONNECTIONTYPE_TunnelInterface, policy:str="IKEv2",
                 actiononvpnrestart:str = ActionOnVPNRestart_Disable, authenticationtype:str = AuthenticationType_PresharedKey,
                 presharedkey: str|None = None,  localcertificate: str|None = None,  remotecertificate: str|None = None,  remotersakey: str|None = None,) -> None:
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
        self.description: str = description
        self.connectiontype: str = connectiontype
        self.policy: str = policy
        self.actiononvpnrestart: str = actiononvpnrestart
        self.authenticationtype: str = authenticationtype
        self.presharedkey: str = presharedkey
        self.localcertificate: str = localcertificate
        self.remotecertificate: str = remotecertificate
        self.remotersakey: str = remotersakey


    def getXML(self) -> str:
        xml =  f"""<Configuration>
        <Name>{self.name}</Name>
        <Description>{self.description}</Description>
        <ConnectionType>{self.connectiontype}</ConnectionType>
        <Policy>{self.policy}</Policy>
        <ActionOnVPNRestart>{self.actiononvpnrestart}</ActionOnVPNRestart>
        <AuthenticationType>{self.authenticationtype}</AuthenticationType>"""

        if self.authenticationtype == SophosAPIType_IPSECVPN.AuthenticationType_PresharedKey:
            xml += """<PresharedKey>key</PresharedKey>"""

        if self.authenticationtype == SophosAPIType_IPSECVPN.AuthenticationType_DigitalCertificate:
            xml += """<LocalCertificate>ApplianceCertificate</LocalCertificate>
                <RemoteCertificate>ExternalCertificate</RemoteCertificate>"""

        if self.authenticationtype == SophosAPIType_IPSECVPN.AuthenticationType_RSAKey:
            xml += """<RemoteRSAKey>Text</RemoteRSAKey>"""

        """<!-- For Certificate -->


			<!-- For Network Detail IP Family -->
			<SubnetFamily>IPv4/IPv6</SubnetFamily>

			<!-- For Endpoint Detail IP Family -->
			<EndpointFamily>IPv4/IPv6</EndpointFamily>

			<!-- For RSA Key -->
			
			<LocalWANPort>PortB</LocalWANPort>
			<!-- For alias wan port -->
			<AliasLocalWANPort>PortB:0</AliasLocalWANPort>
			<RemoteHost>Host</RemoteHost>
			<LocalSubnet>Host</LocalSubnet>

			<!-- only for site-to-site -->
			<NATedLAN>Host</NATedLAN>
			<LocalIDType>DNS/IP Address/Email/DER ASN1 DN (X.509)</LocalIDType>
			<LocalID>localid</LocalID>

			<!-- only for RemoteAccess & Host-to-Host -->
			<AllowNATTraversal>Enable/Disable</AllowNATTraversal>
			<RemoteNetwork>
				<Network>Network</Network>
			</RemoteNetwork>
			<RemoteIDType>DNS/IP Address/Email/DER ASN1 DN (X.509)</RemoteIDType>
			<RemoteID>remoteid</RemoteID>
			<UserAuthenticationMode>Disable/AsServer/AsClient</UserAuthenticationMode>

			<!-- for AsClient -->
			<Username>username</Username>
			<Password>password</Password>

			<!-- for AsServer -->
			<AllowedUser>
				<User>username</User>
				:
			</AllowedUser>
			<Protocol>ALL/UDP/TCP/ICMP</Protocol>
			<LocalPort>Number</LocalPort>
			<RemotePort>Number</RemotePort>
			<DisconnectOnIdleInterval>600</DisconnectOnIdleInterval>
			<Status>Active/Deactive</Status>
		</Configuration>"""

        return xml