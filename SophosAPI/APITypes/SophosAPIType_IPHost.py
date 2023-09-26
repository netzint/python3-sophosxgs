import ipaddress

class SophosAPIType_IPHost():

    IPFAMILY_IPV4 = "IPv4"
    IPFAMILY_IPV6 = "IPv6"

    HOSTTYPE_IP = "IP"
    HOSTTYPE_IPRange = "IPRange"
    HOSTTYPE_IPList = "IPList"
    HOSTTYPE_Network = "Network"

    def __init__(self, name, ipfamily, hosttype, ip=None, iprange=None, iplist=None, ipnetwork=None, hostgrouplist=None) -> None:
        """
        :param name: Name of the iphost
        :type name: str
        :param ipfamily: Currently only IPv4 and IPv6
        :type ipfamily: str
        :param hosttype: Currently only IP, IPRange, IPList and Network
        :type hosttype: str
        :param ip: IP-Address of object
        :type ip: str
        :param iprange: Range of IP-Address eg.: (1.1.1.1, 1.1.1.2)
        :type iprange: (str, str)
        :param iplist: List of IP-Addresses
        :type iplist: list[str]
        :param ipnetwork: IP-Network eg.: 1.1.1.1/32, 192.168.0.0/24
        :type ipnetwork: str
        :param hostgrouplist: List of groups the host if member of
        :type hostgrouplist: list[str]
        """
        self.name = name
        self.ipfamily = ipfamily
        self.hosttype = hosttype
        self.ip = ip
        self.iprange = iprange
        self.iplist = iplist
        self.ipnetwork = ipnetwork
        self.hostgrouplist = hostgrouplist

    def getXML(self):
        xml =  f"""<Name>{self.name}</Name>
            <IPFamily>{self.ipfamily}</IPFamily>
            <HostType>{self.hosttype}</HostType>"""
        
        if self.hosttype == self.HOSTTYPE_IP:
            xml += f"<IPAddress>{self.ip}</IPAddress>"
        elif self.hosttype == self.HOSTTYPE_IPRange:
            xml += f"""<StartIPAddress>{self.iprange[0]}</StartIPAddress>
		        <EndIPAddress>{self.iprange[1]}</EndIPAddress>"""
        elif self.hosttype == self.HOSTTYPE_IPList:
            str = ""
            for ip in self.iplist:
                str += ip + ","
            str = str[:-1]
            xml += f"<ListOfIPAddresses>{str}</ListOfIPAddresses>"
        elif self.hosttype == self.HOSTTYPE_Network:
            ip = ipaddress.IPv4Network(self.ipnetwork)
            xml += f"""<IPAddress>{ip.network_address}</IPAddress>
		        <Subnet>{ip.netmask}</Subnet>"""
        
        if self.hostgrouplist:
            xml += "<HostGroupList>"
            for hostgroup in self.hostgrouplist:
                xml += f"<HostGroup>{hostgroup}</HostGroup>"
            xml += "</HostGroupList>"
            
        return xml