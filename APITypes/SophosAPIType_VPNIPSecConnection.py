class SophosAPIType_VPNIPSecConnection():

    CONNECTION_TYPE_REMOTE_ACCESS = "RemoteAccess"
    CONNECTION_TYPE_SITE_TO_SITE = "SiteToSite"
    CONNECTION_TYPE_HOST_TO_HOST = "HostToHost"
    CONNECTION_TYPE_TUNNEL_INTERFACE = "TunnelInterface"

    POLICY_IKEv2 = "IKEv2"

    ACTION_ON_VPN_RESTART_DISABLE = "Disable"
    ACTION_ON_VPN_RESTART_RESPOND_ONLY = "RespondOnly"
    ACTION_ON_VPN_RESTART_INITIATE = "Initiate"

    AUTHENTICATION_TYPE_PRESHARED_KEY = "PresharedKey"
    AUTHENTICATION_TYPE_DIGITAL_CERTIFICATE = "DigitalCertificate"
    AUTHENTICATION_TYPE_RSA_KEY = "RSAKey"

    SUBNET_FAMILY_IPv4 = "IPv4"
    SUBNET_FAMILY_IPv6 = "IPv6"
    SUBNET_FAMILY_DUAL= "Dual"

    ENDPOINT_FAMILY_IPv4 = "IPv4"
    ENDPOINT_FAMILY_IPv6 = "IPv6"

    LOCAL_ID_TYPE_DNS = "DNS"
    LOCAL_ID_TYPE_IP = "IP Address"
    LOCAL_ID_TYPE_EMAIL = "Email"

    USER_AUTHENTICATION_MODE_DISABLE = "Disable"
    USER_AUTHENTICATION_MODE_ASSERVER = "AsServer"
    USER_AUTHENTICATION_MODE_ASCLIENT = "AsClient"

    def __init__(self, name: str, description: str, connection_type: str, policy: str, action_on_vpn_restart: str,
                authentication_type: str, preshared_key: str = None, local_certificate: str = None,
                remote_certificate: str = None, subnet_family: str = SUBNET_FAMILY_IPv4, endpoint_family: str = ENDPOINT_FAMILY_IPv4,
                remote_rsa_key: str = None, local_wan_port: str = None, alias_local_wan_port: str = None,
                remote_host: str = None, local_subnet: str = None, nated_lan: str = None, local_id_type: str = None,
                local_id: str = None, allow_nat_traversal: str = None, remote_network: str = None,
                remote_id_type: str = None, remote_id: str = None, user_authentication_mode: str = USER_AUTHENTICATION_MODE_DISABLE,
                username: str = None, password: str = None, allowed_users: list[str] = None):
        """
        Initializes a VPNIPSecConnection object.

        :param name: Name of the VPN connection.
        :param description: Description of the VPN connection.
        :param connection_type: Type of the VPN connection (RemoteAccess, SiteToSite, HostToHost).
        :param policy: VPN policy for the connection.
        :param action_on_vpn_restart: Action to take on VPN restart (Disable, RespondOnly, Initiate).
        :param authentication_type: Type of authentication (PresharedKey, DigitalCertificate, RSAKey).
        :param preshared_key: Preshared key for authentication (optional).
        :param local_certificate: Local certificate for authentication (optional).
        :param remote_certificate: Remote certificate for authentication (optional).
        :param subnet_family: IP family for subnets (IPv4, IPv6).
        :param endpoint_family: IP family for endpoints (IPv4, IPv6).
        :param remote_rsa_key: RSA key for authentication (optional).
        :param local_wan_port: Local WAN port for the connection (optional).
        :param alias_local_wan_port: Alias for local WAN port (optional).
        :param remote_host: Remote host for the connection (optional).
        :param local_subnet: Local subnet for the connection (optional).
        :param nated_lan: NATed LAN address (optional, for SiteToSite connections).
        :param local_id_type: Local ID type (optional, for SiteToSite connections).
        :param local_id: Local ID for authentication (optional, for SiteToSite connections).
        :param allow_nat_traversal: Allow NAT traversal (optional, for RemoteAccess and HostToHost connections).
        :param remote_network: Remote network for the connection (optional, for RemoteAccess and HostToHost connections).
        :param remote_id_type: Remote ID type (optional, for RemoteAccess and HostToHost connections).
        :param remote_id: Remote ID for authentication (optional, for RemoteAccess and HostToHost connections).
        :param user_authentication_mode: User authentication mode (optional, for RemoteAccess and HostToHost connections).
        :param username: Username for user authentication (optional, for AsClient mode).
        :param password: Password for user authentication (optional, for AsClient mode).
        :param allowed_users: List of allowed users (optional, for AsServer mode).

        Example usage:
        connection = SophosAPIType_VPNIPSecConnection(name="MyConnection", description="My VPN Connection",
                                                    connection_type="RemoteAccess", policy="DefaultPolicy",
                                                    action_on_vpn_restart="Initiate", authentication_type="PresharedKey",
                                                    preshared_key="mysecretkey", subnet_family="IPv4")
        """
        self.name = name
        self.description = description
        self.connection_type = connection_type
        self.policy = policy
        self.action_on_vpn_restart = action_on_vpn_restart
        self.authentication_type = authentication_type
        self.preshared_key = preshared_key
        #self.local_certificate = local_certificate
        #self.remote_certificate = remote_certificate
        self.subnet_family = subnet_family
        self.endpoint_family = endpoint_family
        #self.remote_rsa_key = remote_rsa_key
        self.local_wan_port = local_wan_port
        self.alias_local_wan_port = alias_local_wan_port
        self.remote_host = remote_host
        #self.local_subnet = local_subnet
        self.nated_lan = nated_lan
        self.local_id_type = local_id_type
        self.local_id = local_id
        #self.allow_nat_traversal = allow_nat_traversal
        #self.remote_network = remote_network
        self.remote_id_type = remote_id_type
        self.remote_id = remote_id
        self.user_authentication_mode = user_authentication_mode
        self.username = username
        self.password = password
        self.allowed_users = allowed_users

    def getXML(self):
        xml = f"""<Configuration>
      <Name>{self.name}</Name>
      <Description>{self.description}</Description>
      <ConnectionType>{self.connection_type}</ConnectionType>
      <Policy>{self.policy}</Policy>
      <ActionOnVPNRestart>{self.action_on_vpn_restart}</ActionOnVPNRestart>
      <AuthenticationType>{self.authentication_type}</AuthenticationType>
      <SubnetFamily>{self.subnet_family}</SubnetFamily>
      <EndpointFamily>{self.endpoint_family}</EndpointFamily>
      <AliasLocalWANPort>{self.alias_local_wan_port}</AliasLocalWANPort>
      <RemoteHost>{self.remote_host}</RemoteHost>
      <NATedLAN/>
      <LocalIDType>{self.local_id_type}</LocalIDType>
      <LocalID>{self.local_id}</LocalID>
      <RemoteIDType>{self.remote_id_type}</RemoteIDType>
      <RemoteID>{self.remote_id}</RemoteID>
      <UserAuthenticationMode>{self.user_authentication_mode}</UserAuthenticationMode>
      <AllowedUser>
        <User/>
      </AllowedUser>
      <Protocol>ALL</Protocol>
      <LocalPort/>
      <RemotePort/>
      <LocalWANPort>{self.local_wan_port}</LocalWANPort>
      <DisconnectOnIdleInterval/>
      <Status>Active</Status>
      <PresharedKey>{self.preshared_key}</PresharedKey>
      <Username/>
      <Password/>
      <ActivateOnSave>y</ActivateOnSave>
    </Configuration>"""
        
        return xml
    
    def getActivationXML(self):
        xml = f"""
        <Configuration>
          <Name>{self.name}</Name>
        </Configuration>
        <Active><Name>{self.name}</Name></Active>
        """

        return xml
        




        # xml = f"""<Configuration><Name>{self.name}</Name>
        #     <Description>{self.description}</Description>
        #     <ConnectionType>{self.connection_type}</ConnectionType>
        #     <Policy>{self.policy}</Policy>
        #     <ActionOnVPNRestart>{self.action_on_vpn_restart}</ActionOnVPNRestart>
        #     <AuthenticationType>{self.authentication_type}</AuthenticationType>"""

        # if self.authentication_type == self.AUTHENTICATION_TYPE_PRESHARED_KEY:
        #     xml += f"<PresharedKey>{self.preshared_key}</PresharedKey>"
        # elif self.authentication_type == self.AUTHENTICATION_TYPE_DIGITAL_CERTIFICATE:
        #     xml += f"<LocalCertificate>{self.local_certificate}</LocalCertificate>"
        #     xml += f"<RemoteCertificate>{self.remote_certificate}</RemoteCertificate>"
        # elif self.authentication_type == self.AUTHENTICATION_TYPE_RSA_KEY:
        #     xml += f"<RemoteRSAKey>{self.remote_rsa_key}</RemoteRSAKey>"

        # xml += f"""<SubnetFamily>{self.subnet_family}</SubnetFamily>
        #     <EndpointFamily>{self.endpoint_family}</EndpointFamily>
        #     <LocalWANPort>{self.local_wan_port}</LocalWANPort>
        #     <AliasLocalWANPort>{self.alias_local_wan_port}</AliasLocalWANPort>
        #     <RemoteHost>{self.remote_host}</RemoteHost>
        #     <LocalSubnet>{self.local_subnet}</LocalSubnet>"""

        # if self.connection_type == self.CONNECTION_TYPE_SITE_TO_SITE:
        #     xml += f"<NATedLAN>{self.nated_lan}</NATedLAN>"

        # xml += f"""<LocalIDType>{self.local_id_type}</LocalIDType>
        #     <LocalID>{self.local_id}</LocalID>
        #     <RemoteIDType>{self.remote_id_type}</RemoteIDType>
        #     <RemoteID>{self.remote_id}</RemoteID>"""

        # if self.connection_type == self.CONNECTION_TYPE_HOST_TO_HOST or self.connection_type == self.CONNECTION_TYPE_REMOTE_ACCESS:
        #     xml += f"<AllowNATTraversal>{self.allow_nat_traversal}</AllowNATTraversal>"
        #     if self.remote_network:
        #         xml += "<RemoteNetwork>"
        #         xml += f"<Network>{self.remote_network}</Network>"
        #         xml += "</RemoteNetwork>"

        # xml += f"<UserAuthenticationMode>{self.user_authentication_mode}</UserAuthenticationMode>"
        # if self.user_authentication_mode == self.USER_AUTHENTICATION_MODE_ASSERVER:
        #     xml += f"<AllowedUser>"
        #     for user in self.allowed_users:
        #         xml += f"<User>{user}</User>"
        #     xml += "</AllowedUser>"

        # xml += "</Configuration>"
        # return xml