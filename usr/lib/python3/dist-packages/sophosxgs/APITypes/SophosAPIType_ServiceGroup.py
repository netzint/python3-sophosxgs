class SophosAPIType_ServiceGroup():

    def __init__(self, name, description=None, servicelist=None) -> None:
        """
        :param name: Name of the servicegroup
        :type name: str
        :param description: Description of this servicegroup
        :type description: str
        :param servicelist: List of services should be member of this group
        :type servicelist: list[str]
        """
        self.name = name
        self.description = description
        self.servicelist = servicelist

    def getXML(self):
        xml =  f"<Name>{self.name}</Name>"
        
        if self.description:
            xml += f"<Description>{self.description}</Description>"
        
        if self.servicelist:
            xml += "<ServiceList>"
            for service in self.servicelist:
                xml += f"<Service>{service}</Service>"
            xml += "</ServiceList>"
            
        return xml