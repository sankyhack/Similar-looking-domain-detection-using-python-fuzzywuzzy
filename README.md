# Similar-looking-domain-detection-using-python-fuzzywuzzy
Major cause of phishing and BEC incident is similar looking domain, if you detect it early, you can prevent incidents early, python fuzzywuzzy module let you do that and here is the process.

By statistics every day thousands of domains are registered, some are use for legit purpose and some are not.
BEC incidents incresing every day and cost millions to businesses, the core of BEC is spoofed email that looks similar to your business email.
Because of these similar looking domain we fall pray to BEC incidents.
Sometimes we end up submitting our credential when we received any email having link that looks like genuine website.
e.g. microsoft.com vs micr0soft.com.

How can we detect/prevent such incident?

In python you have module named "fuzzywuzzy" that looks for similarity in strings and gives score of how similar strings are, like 90% match, 66% match.
Use that to look for simiar domains
1) Gather data (SIEM) having domain related information e.g. Proxy logs, DNS logs, Mail logs.
2) Have list of domains related to your business ( your owned domain, list of vendor domains with whom you carry out business )
3) Now run fuzz module against this data and check ratio which is more than 50% ( e.g. given below )
4) Do the analysis of domains (check whois data) which looks similar to your domain, if genuine add to list gathered in Step 2
5) If domain is not genuine, start digging more on that domain, like any email received(mail logs), any user visited the domain(proxy logs)  
6) You can run such checks on hourly, daily basis.... thats it.

Here are coule of examples.

1) Basic example <br />  
	from fuzzywuzzy import fuzz<br />
	a = "microsoft.com" <br />
	b = "micros0ft.com" <br />
	print("Match ratio is ", str(fuzz.ratio(a, b)), "%")  // fuzz.ration(a,b) function gives you match score <br />

2) Working code <br />

	from fuzzywuzzy import fuzz <br />

	dns_data = open(r'/home/user/Desktop/BEC/your_domain.txt','r') # List of genuine domains owned by you <br />
	output = open(r'/home/user/Desktop/BEC/output.txt','w')		# Output file <br />

	for dns in dns_data:    <br />
	>domain = open(r'/home/user/Desktop/BEC/domain-names-data.txt','r') # domain data gathered from proxy/dns/mail logs <br />
	>for site in domain: <br />
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if ( fuzz.ratio(site.rstrip(),dns.rstrip()) > 80 ): <br />
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output.write("Match ratio is: \t" + dns.rstrip() + "\t" + site.rstrip() + "\t" + str(fuzz.ratio(site.rstrip(),dns.rstrip()))) <br />
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output.write("\n") <br />
			
		
If you have access to whois database then you can run this code against newly registered domain everyday and probably you can get the result early!!!

I have run this code against newly registered doamin on 3rd Nov. Legit domains considered are top 1000 domains.
Results are amazing as to how many similar looking domains are registered everyday and no wonder we receive lot of offerers from amzon apples :)
Check out Output.txt file

Feel free to share your thoughts!!!
