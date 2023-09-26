class SophosAPIType_Services():

    TYPE_TCPorUDP = "TCPorUDP"

    def __init__(self, name, type, serviceportlist) -> None:
        """
        :param name: Name of the iphost
        :type name: str
        :param type: Currently only TCPorUDP
        :type type: str
        :param serviceportlist: List of Sophos API Service Port
        :type serviceportlist: list[SophosAPIType_Service_Port]
        """
        self.name = name
        self.type = type
        self.serviceportlist = serviceportlist

    def getXML(self):
        xml =  f"""<Name>{self.name}</Name>
            <Type>{self.type}</Type>
            <ServiceDetails>"""
        
        for serviceport in self.serviceportlist:
            xml += f"""<ServiceDetail>
            <Protocol>{serviceport.protocol}</Protocol>
            <SourcePort>{serviceport.sourceport}</SourcePort>
            <DestinationPort>{serviceport.destinationport}</DestinationPort>
            </ServiceDetail>
            """
        
        xml += "</ServiceDetails>"
            
        return xml
    
class SophosAPIType_Service_Port():

    PROTOCOL_TCP = "TCP"
    PROTOCOL_UDP = "UDP"

    def __init__(self, protocol, destinationport, sourceport="1:65535") -> None:
        """
        :param protocol: Currently only TCP, UDP
        :type protocol: str
        :param sourceport: Source port 
        :type sourceport: str
        :param destinationport: Destination port 
        :type destinationport: str
        """
        self.protocol = protocol
        self.sourceport = sourceport
        self.destinationport = destinationport