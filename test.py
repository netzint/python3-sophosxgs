from SophosAPI import SophosAPI, SophosAPIType, SophosAPIType_FirewallRule
api = SophosAPI("10.0.1.1", 4444, "admin", "Muster123!")

# newhost = SophosAPIType_IPHost("test1", SophosAPIType_IPHost.IPFAMILY_IPV4, SophosAPIType_IPHost.HOSTTYPE_IP, ip="1.1.1.1")
# result = api.add(SophosAPIType.IPHOST, newhost)
# print(result)

# newhost = SophosAPIType_IPHost("test2", SophosAPIType_IPHost.IPFAMILY_IPV4, SophosAPIType_IPHost.HOSTTYPE_IPList, iplist=["1.1.1.1", "2.2.2.2", "3.3.3.3"])
# result = api.add(SophosAPIType.IPHOST, newhost)
# print(result)

# newhost = SophosAPIType_IPHost("test3", SophosAPIType_IPHost.IPFAMILY_IPV4, SophosAPIType_IPHost.HOSTTYPE_IPRange, iprange=("192.168.1.10", "192.168.1.20"))
# result = api.add(SophosAPIType.IPHOST, newhost)
# print(result)

# newhost = SophosAPIType_IPHost("test4", SophosAPIType_IPHost.IPFAMILY_IPV4, SophosAPIType_IPHost.HOSTTYPE_Network, ipnetwork="192.168.0.0/24")
# result = api.add(SophosAPIType.IPHOST, newhost)
# print(result)

# result = api.get(SophosAPIType.IPHOST)
# print(result)

# newgroup = SophosAPIType_IPHostGroup("test2", SophosAPIType_IPHostGroup.IPFAMILY_IPV4, "TEst123")
# result = api.add(SophosAPIType.IPHOSTGROUP, newgroup)
# print(result)

# newzone = SophosAPIType_Zone("Test", SophosAPIType_Zone.TYPE_LAN, applianceaccess=SophosAPIType_Zone_ApplianceAccess(network_dns=True, network_ping=True, adminservice_https=True))
# result = api.add(SophosAPIType.ZONE, newzone)
# print(result)

# new = SophosAPIType_FirewallRuleGroup("YELLOW", "All firewallrules from green network", SophosAPIType_FirewallRuleGroup.POLICYTYPE_ANY, sourcezonelist=["LAN", "DMZ"])
# result = api.add(SophosAPIType.FIREWALLRULEGROUP, new)
# print(result)

new = SophosAPIType_FirewallRule("Test1",
                                 policytype=SophosAPIType_FirewallRule.POLICYTYPE_NETWORK, sourcezonelist=["LAN"], destinationzonelist=["WAN"],
                                 action=SophosAPIType_FirewallRule.ACTION_ACCEPT)
result = api.add(SophosAPIType.FIREWALLRULE, new)
print(result)