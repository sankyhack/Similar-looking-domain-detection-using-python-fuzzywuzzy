from fuzzywuzzy import fuzz

dns_data = open(r'/home/user/Desktop/BEC/your_domains.txt','r') # List of genuine domains owned by you, add your vendor/partner domains as well (change path as per your directory structure)
output = open(r'/home/user/Desktop/BEC/output.txt','w')		# Output file (change path as per your directory structure)

for dns in dns_data:    
    domain = open(r'/home/user/Desktop/BEC/domain-names-data.txt','r') # domains related data gathered from proxy/dns/mail logs (SIEM will help you) (change path as per your directory structure)
    for site in domain:
        if ( fuzz.ratio(site.rstrip(),dns.rstrip()) > 80 ):
            output.write("Match ratio is: \t" + dns.rstrip() + "\t" + site.rstrip() + "\t" + str(fuzz.ratio(site.rstrip(),dns.rstrip())))
            output.write("\n")
