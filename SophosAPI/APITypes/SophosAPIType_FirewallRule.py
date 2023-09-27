class SophosAPIType_FirewallRule():

    IPFAMILY_IPV4 = "IPv4"
    IPFAMILY_IPV6 = "IPv6"

    POLICYTYPE_NETWORK = "Network"
    POLICYTYPE_USER = "User"
    POLICYTYPE_HTTPBASED = "HTTPBased"

    ACTION_ACCEPT = "Accept"
    ACTION_REJECT = "Reject"
    ACTION_DROP = "Drop"

    POSITION_TOP = "top"
    POSITION_BOTTOM = "bottom"
    POSITION_AFTER = "after"
    POSITION_BEFORE = "before"

    USERPOLICYDATAACCOUNTING_INCLUDE = "Include"
    USERPOLICYDATAACCOUNTING_EXCLUDE = "Exclude"

    def __init__(self, name:str, description:str="", status:bool=True, ipfamily:str=IPFAMILY_IPV4, position:str=POSITION_BOTTOM, policytype:str=None, 
                 action:str=None, logtraffic:bool=False, sourcezonelist:list=["Any"], sourcenetworklist:list=["Any"], servicelist:list=["Any"], 
                 schedule:str="All the time", destinationzonelist:list=["Any"], destinationnetworklist:list=["Any"], exclustionsourcezonelist:list=None, 
                 exclustionsourcenetworklist:list=None, exclustionservicelist:list=None, exclustiondestinationzonelist:list=None, 
                 exclustiondestinationnetworklist:list=None, userpolicymatchidentity:bool=False, userpolicyshowcaptiveportal:bool=None, 
                 userpolicyidentitylist:list=None, userpolicydataaccounting:str=None) -> None:
        """
        :param name: Name of the zone
        :type name: str
        :param description: Description of this zone
        :type description: str
        :param status: 
        :type status: 
        :param ipfamily: 
        :type ipfamily: 
        :param position: 
        :type position: 
        :param policytype: 
        :type policytype: 
        :param action: 
        :type action: 
        :param logtraffic: 
        :type logtraffic: 
        :param sourcezonelist: 
        :type sourcezonelist: 
        :param sourcenetworklist: 
        :type sourcenetworklist: 
        :param servicelist: 
        :type servicelist: 
        :param schedule: 
        :type schedule: 
        :param destinationzonelist: 
        :type destinationzonelist: 
        :param destinationnetworklist: 
        :type destinationnetworklist: 
        :param exclustionsourcezonelist: 
        :type exclustionsourcezonelist: 
        :param exclustionsourcenetworklist: 
        :type exclustionsourcenetworklist: 
        :param exclustionservicelist: 
        :type exclustionservicelist: 
        :param exclustiondestinationzonelist: 
        :type exclustiondestinationzonelist: 
        :param exclustiondestinationnetworklist: 
        :type exclustiondestinationnetworklist: 
        :param userpolicymatchidentity: 
        :type userpolicymatchidentity: 
        :param userpolicyshowcaptiveportal: 
        :type userpolicyshowcaptiveportal: 
        :param userpolicyidentitylist: 
        :type userpolicyidentitylist: 
        :param userpolicydataaccounting: 
        :type userpolicydataaccounting: 
        """
        self.name = name
        self.description = description
        self.status = status
        self.ipfamily = ipfamily
        self.position = position
        self.policytype = policytype
        self.action = action
        self.logtraffic = logtraffic
        self.sourcezonelist = sourcezonelist
        self.sourcenetworklist = sourcenetworklist
        self.servicelist = servicelist
        self.schedule = schedule
        self.destinationzonelist = destinationzonelist
        self.destinationnetworklist = destinationnetworklist
        self.exclustionsourcezonelist = exclustionsourcezonelist
        self.exclustionsourcenetworklist = exclustionsourcenetworklist
        self.exclustionservicelist = exclustionservicelist
        self.exclustiondestinationzonelist = exclustiondestinationzonelist
        self.exclustiondestinationnetworklist = exclustiondestinationnetworklist
        self.userpolicymatchidentity = userpolicymatchidentity
        self.userpolicyshowcaptiveportal = userpolicyshowcaptiveportal
        self.userpolicyidentitylist = userpolicyidentitylist
        self.userpolicydataaccounting = userpolicydataaccounting

    def __getValue(self, service):
        if service:
            return "Enable"
        return "Disable"

    def getXML(self) -> str:
        xml =  f"""<Name>{self.name}</Name>
            <Description>{self.description}</Description>
            <Status>{self.__getValue(self.action)}</Status>
            <IPFamily>{self.ipfamily}</IPFamily>
            <Position>{self.position}</Position>
            <Policytype>{self.policytype}</Policytype>"""
        
        # Add here the positioning options:
        # <Position>top/bottom/after/before</Position>
        # <!-- After and Before Tag Apply only for Set Request -->
        # <After>
        #     <Name>Policy name after which Policy Inserted </Name>
        # </After>
        # <Before>
        #     <Name>Policy name before which Policy Inserted </Name>
        # </Before>
        
        if self.policytype == self.POLICYTYPE_USER:
            xml += "<UserPolicy>"
        elif self.policytype == self.POLICYTYPE_NETWORK:
            xml += "<NetworkPolicy>"
        elif self.policytype == self.POLICYTYPE_HTTPBASED:
            xml += "<HTTPBasedPolicy>"

        xml += f"""<Action>{self.action}</Action>
            <LogTraffic>{self.__getValue(self.logtraffic)}</LogTraffic>
            <Schedule>{self.schedule}</Schedule>"""
		
        xml += "<SourceZones>"
        for sourcezone in self.sourcezonelist:
            xml += f"<Zone>{sourcezone}</Zone>"
        xml += "</SourceZones>"
		
        xml += "<SourceNetworks>"
        for sourcenetwork in self.sourcenetworklist:
            xml += f"<Network>{sourcenetwork}</Network>"
        xml += "</SourceNetworks>"

        xml += "<Services>"
        for service in self.servicelist:
            xml += f"<Service>{service}</Service>"
        xml += "</Services>"

        xml += "<DestinationZones>"
        for destinationzone in self.destinationzonelist:
            xml += f"<Zone>{destinationzone}</Zone>"
        xml += "</DestinationZones>"
		
        xml += "<DestinationNetworks>"
        for destinationnetwork in self.destinationnetworklist:
            xml += f"<Network>{destinationnetwork}</Network>"
        xml += "</DestinationNetworks>"
		
        if self.exclustiondestinationnetworklist and self.exclustiondestinationzonelist and self.exclustionservicelist and self.exclustionsourcenetworklist and self.exclustionsourcezonelist:
            xml += "<Exclusions>"
            xml += "<SourceZones>"
            for exclustionsourcezone in self.exclustionsourcezonelist:
                xml += f"<Zone>{exclustionsourcezone}</Zone>"
            xml += "</SourceZones>"
            
            xml += "<SourceNetworks>"
            for exclustionsourcenetwork in self.exclustionsourcenetworklist:
                xml += f"<Network>{exclustionsourcenetwork}</Network>"
            xml += "</SourceNetworks>"

            xml += "<Services>"
            for exclustionservice in self.exclustionservicelist:
                xml += f"<Service>{exclustionservice}</Service>"
            xml += "</Services>"

            xml += "<DestinationZones>"
            for exclustiondestinationzone in self.exclustiondestinationzonelist:
                xml += f"<Zone>{exclustiondestinationzone}</Zone>"
            xml += "</DestinationZones>"
            
            xml += "<DestinationNetworks>"
            for exclustiondestinationnetwork in self.exclustiondestinationnetworklist:
                xml += f"<Network>{exclustiondestinationnetwork}</Network>"
            xml += "</DestinationNetworks>"
            xml += "</Exclusions>"
        
        # add her webfiltering and the other stuff

# 						<!-- WebFiltering -->
# 			<WebFilter>Allow All</WebFilter>
# 			<WebCategoryBaseQoSPolicy>Apply/Revoke</WebCategoryBaseQoSPolicy><!-- this tag is only appliacable only when any WebFilter is selected. -->
# 			<BlockQuickQuic>Enable/Disable</BlockQuickQuic>
# 			<ScanVirus>Enable/Disable</ScanVirus>
# 			<Sandstorm>Enable/Disable</Sandstorm>
# 			<ScanFTP>Enable/Disable</ScanFTP>
# 			<ProxyMode>Enable/Disable</ProxyMode>
# 			<DecryptHTTPS>Enable/Disable</DecryptHTTPS>
# 						<!-- Synchronized Security -->
# 			<SourceSecurityHeartbeat>Enable/Disable</SourceSecurityHeartbeat>
# 			<MinimumSourceHBPermitted />
# 			<DestSecurityHeartbeat>Enable/Disable</DestSecurityHeartbeat>
# 			<MinimumDestinationHBPermitted />
# 						<!-- Security Features -->
# 			<ApplicationControl>Allow All</ApplicationControl>
# 			<ApplicationBaseQoSPolicy>Apply/Revoke</ApplicationBaseQoSPolicy><!-- this tag is only appliacable only when any ApplicationFilter is selected. -->
# 			<IntrusionPrevention>None</IntrusionPrevention>
# 			<TrafficShapingPolicy>None</TrafficShapingPolicy>
# 			<DSCPMarking>0-Best Effort/1/2/3/4/5/6/7/8-Class 1(CS1)/9/10-Class 1,Gold(AF11)/11/12-Class1,Silver(AF12)/13/14-Class 1,Bronze(AF13)/15/16-Class 2(CS2)/17/18-Class 2,Gold(AF21)/19/20-Class 2,Silver(AF22)/21/22-Class 2,Bronze(AF23)/23/24-Class 3(CS3)/25/26-Class 3,Gold(AF31)/27/28-Class 3,Silver(AF32)/29/30-Class 3,Bronze(AF33)/31/32-Class 4(CS4)/33/34-Class 4,Gold(AF41)/35/36-Class 4,Silver(AF42)/37/38-Class 4,Bronze(AF43)/39/40-Class 5(CS5)/41/42/43/44/45/46-Expedited Forwarding(EF)/47/48-Control(CS6)/49/50/51/52/53/54/55/56-Control(CS7)/57/58/59/60/61/62/63</DSCPMarking>
# 			<!-- Email Scanning -->
# 			<ScanSMTP>Enable/Disable</ScanSMTP>
# 			<ScanSMTPS>Enable/Disable</ScanSMTPS>
# 			<ScanIMAP>Enable/Disable</ScanIMAP>
# 			<ScanIMAPS>Enable/Disable</ScanIMAPS>
# 			<ScanPOP3>Enable/Disable</ScanPOP3>
# 			<ScanPOP3S>Enable/Disable</ScanPOP3S>

        if self.policytype == self.POLICYTYPE_USER:
            xml += f"""<MatchIdentity>{self.__getValue(self.userpolicymatchidentity)}</MatchIdentity>
                <ShowCaptivePortal>{self.__getValue(self.userpolicyshowcaptiveportal)}</ShowCaptivePortal>
                <Identity>"""
            for userpolicyidentity in self.userpolicyidentitylist:
                xml += f"<Member>{userpolicyidentity}</Member>"
            xml += f"""</Identity>
                <DataAccounting>{self.userpolicydataaccounting}</DataAccounting>"""
            xml += "</UserPolicy>"
        elif self.policytype == self.POLICYTYPE_NETWORK:
            xml += "</NetworkPolicy>"
        elif self.policytype == self.POLICYTYPE_HTTPBASED:
            xml += "</HTTPBasedPolicy>"
            
        return xml
# 		<!-- WAF Policy Start -->
# 		<HTTPBasedPolicy>
# 		<!--HTTP base policy is only applicable for IPv4-->
# 			<HostedAddress>Address</HostedAddress>
# 			<HTTPS>Enable/Disable</HTTPS>
# 			<RedirectHTTP>Enable/Disable</RedirectHTTP>
# 			<ListenPort>80</ListenPort>
# 			<Domains>
# 				<Domain />
# 				<Domain />
# 				:
# 			</Domains>
# 			<!--Use Either Authentication,AllowFrom,BlockFrom or AccessPaths -->
# 			<SourceNetworks>
# 				<Network />
# 				<Network />
# 				:
# 			</SourceNetworks>
# 			<ExceptionNetworks>
# 				<Network />
# 				<Network />
# 				:
# 			</ExceptionNetworks>
# 			<AccessPaths>
# 				<AccessPath><!--  At present AccessPath Attributes are name as it is in database and values of enable/disable is mapped as 1/0. -->
# 					<path>/access</path>
# 					<backend />
# 					<backend />
# 					<auth_profile />
# 					<allowed_networks />
# 					<allowed_networks />
# 					:
# 					<denied_networks />
# 					<denied_networks />
# 					:
# 					<stickysession_status>1/0</stickysession_status>
# 					<hot_standby>1/0</hot_standby>
# 					<websocket_passthrough>1/0</websocket_passthrough>
# 				</AccessPath>
# 				<AccessPath>
# 					<Path>/useraccess</Path>
# 					<backend />
# 					<backend />
# 					<auth_profile />
# 					<allowed_networks />
# 					<allowed_networks />
# 					:
# 					<denied_networks />
# 					<denied_networks />
# 					:
# 					<stickysession_status>1/0</stickysession_status>
# 					<hot_standby>1/0</hot_standby>
# 					<websocket_passthrough>1/0</websocket_passthrough>
# 				</AccessPath>
# 				:
# 			</AccessPaths>
# 			<Exceptions>
# 				<Exception> <!--  At present Exception Attributes are name as it is in database and values of enable/disable is mapped as 1/0. -->
# 					<path>psql</path>
# 					<path>abcd</path>
# 					<op>and/or</op>
# 					<source />
# 					<source />
# 					<skip_threats_filter_categories>application_attacks</skip_threats_filter_categories>
# 					<skip_threats_filter_categories>sql_injection_attacks</skip_threats_filter_categories>
# 					<skip_threats_filter_categories>xss_attacks</skip_threats_filter_categories>
# 					<skip_threats_filter_categories>protocol_enforcement</skip_threats_filter_categories>
# 					<skip_threats_filter_categories>scanner_detection</skip_threats_filter_categories>
# 					<skip_threats_filter_categories>data_leakages</skip_threats_filter_categories>
# 					<skipav>1</skipav>
# 					<skipbadclients>0</skipbadclients>
# 					<skipcookie>1</skipcookie>
# 					<skipform>0</skipform>
# 					<skipurl>1</skipurl>
# 					</Exception>
# 				<Exception>
# 					:
# 					:
# 				</Exception>
# 				:
# 			</Exceptions>
# 			<ProtocolSecurity />
# 			<CompressionSupport>Disable/Enable</CompressionSupport>
# 			<RewriteHTML>Enable/Disable</RewriteHTML>
# 			<RewriteCookies>Enable/Disable</RewriteCookies>
# 			<PassHostHeader>Enable/Disable</PassHostHeader>
# 			<IntrusionPrevention>None</IntrusionPrevention>
# 			<TrafficShapingPolicy>None</TrafficShapingPolicy>
# 		</HTTPBasedPolicy>
# 		<!-- WAF Policy End -->