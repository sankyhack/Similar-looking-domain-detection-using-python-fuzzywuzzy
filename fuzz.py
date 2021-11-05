from fuzzywuzzy import fuzz

dns_data = open(r'/home/user/Desktop/BEC/your_domain.txt','r') # List of genuine domains owned by you
output = open(r'/home/user/Desktop/BEC/output.txt','w')		# Output file

for dns in dns_data:    
    domain = open(r'/home/user/Desktop/BEC/domain-names-data.txt','r') # domain data gathered from proxy/dns/mail logs
    for site in domain:
        if ( fuzz.ratio(site.rstrip(),dns.rstrip()) > 80 ):
            output.write( dns.rstrip() + "\t" + site.rstrip() + "\t" + str(fuzz.ratio(site.rstrip(),dns.rstrip())))
            output.write("\n")
