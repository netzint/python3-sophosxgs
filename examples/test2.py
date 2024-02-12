from SophosAPI.SophosAPI import *

def getCertificatesFromSophos(certificates) -> list:
   certsToWorkOn = []
   if type(certificates["Response"]["Certificate"]) == list:
      # whe have more then one certificate, so we have to loop throug all
      for certificate in certificates["Response"]["Certificate"]:
         if "-LE" in certificate["Name"]:
            tmp = {
               "commonName":  certificate["CommonName"],
               "email": certificate["EmailAddress"]
            }
            if type(certificate["DNSSubjectAltNames"]["DNSName"]) != list:
               tmp["dnsNames"] = [ certificate["DNSSubjectAltNames"]["DNSName"] ]
            else:
               tmp["dnsNames"] = certificate["DNSSubjectAltNames"]["DNSName"]
            certsToWorkOn.append(tmp)
   else:
      # we have only one certificate
      certificate = certificates["Response"]["Certificate"]
      if "-LE" in certificate["Name"]:
         tmp = {
            "commonName":  certificate["CommonName"],
            "email": certificate["EmailAddress"]
         }
         if type(certificate["DNSSubjectAltNames"]["DNSName"]) != list:
            tmp["dnsNames"] = [ certificate["DNSSubjectAltNames"]["DNSName"] ]
         else:
            tmp["dnsNames"] = certificate["DNSSubjectAltNames"]["DNSName"]
         certsToWorkOn.append(tmp)

   return certsToWorkOn

def registerDehydrated():
   command = "./dehydrated --register --accept-terms"

def generateLECertificates(certificates) -> list:
   for certificate in certificates:
      command = "./dehydrated -f -c /tmp/tmp.config"

      for domain in certificate["dnsNames"]:
         command += " -d " + domain

      with open("/tmp/tmp.config", "w") as f:
         f.write("CHALLENGETYPE='http-01'\nBASEDIR=/opt\nWELLKNOWN='/var/www/dehydrated'\nCONTACT_EMAIL=" + certificate["email"])
      
      print(command)


api = SophosAPI("10.0.0.254", 4444, "apiuser", "ApIuSeR#123")
result = api.get(SophosAPIType.CERTIFICATE)
certificates = getCertificatesFromSophos(result.get())

generateLECertificates(certificates)