import sys
sys.path.append("../..")

from module_sophosapi import SophosAPI, SophosAPIType, SophosAPIType_VPNIPSecConnection

api = SophosAPI("10.0.1.1", 4444, "admin", "Muster123!")

# res = api.get(SophosAPIType.IPSECVPN)
# print(res.getXML())

# xml = """<Set>
#     <VPNIPSecConnection>
#     <Configuration>
#       <Name>Test02</Name>
#       <Description/>
#       <ConnectionType>TunnelInterface</ConnectionType>
#       <Policy>IKEv2</Policy>
#       <ActionOnVPNRestart>RespondOnly</ActionOnVPNRestart>
#       <AuthenticationType>PresharedKey</AuthenticationType>
#       <SubnetFamily>Dual</SubnetFamily>
#       <EndpointFamily>IPv4</EndpointFamily>
#       <AliasLocalWANPort>Port2</AliasLocalWANPort>
#       <RemoteHost>1.1.1.1</RemoteHost>
#       <NATedLAN/>
#       <LocalIDType>DNS</LocalIDType>
#       <LocalID>firewall1</LocalID>
#       <RemoteIDType>DNS</RemoteIDType>
#       <RemoteID>firewall2</RemoteID>
#       <UserAuthenticationMode>Disable</UserAuthenticationMode>
#       <AllowedUser>
#         <User/>
#       </AllowedUser>
#       <Protocol>ALL</Protocol>
#       <LocalPort/>
#       <RemotePort/>
#       <LocalWANPort>Port2</LocalWANPort>
#       <DisconnectOnIdleInterval/>
#       <Status>Active</Status>
#       <PresharedKey>penis123penis456</PresharedKey>
#       <Username/>
#       <Password/>
#     </Configuration>
#     </VPNIPSecConnection>
#   </Set>"""

# res = api.rawRequest(xml)
# print(res)

res = api.add(SophosAPIType.IPSECVPN, SophosAPIType_VPNIPSecConnection("Test_Con_2", "This is a test connection", SophosAPIType_VPNIPSecConnection.CONNECTION_TYPE_TUNNEL_INTERFACE,
                                                                 SophosAPIType_VPNIPSecConnection.POLICY_IKEv2, SophosAPIType_VPNIPSecConnection.ACTION_ON_VPN_RESTART_RESPOND_ONLY,
                                                                 SophosAPIType_VPNIPSecConnection.AUTHENTICATION_TYPE_PRESHARED_KEY, "penis12345penis67890", local_wan_port="Port2",
                                                                 alias_local_wan_port="Port2", remote_host="1.1.1.1", local_id_type=SophosAPIType_VPNIPSecConnection.LOCAL_ID_TYPE_DNS,
                                                                 local_id="firewall1", remote_id_type=SophosAPIType_VPNIPSecConnection.LOCAL_ID_TYPE_DNS, remote_id="firewall2"))

print(res)