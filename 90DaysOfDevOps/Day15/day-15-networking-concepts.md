#### Networking Concepts: DNS, IP, Subnets \& Ports



##### 

##### 1\. DNS – How Names Become IPs





What happens when you type google.com in a browser?



Browser checks local DNS cache.



If not found, it queries a DNS resolver.



Resolver asks root → TLD (.com) → authoritative DNS server.



DNS returns IP address (A/AAAA record).



Browser connects to that IP using TCP (usually port 443).



DNS Record Types



A → Maps domain name to IPv4 address



AAAA → Maps domain to IPv6 address



CNAME → Alias of another domain



MX → Mail server record



NS → Name server for the domain



dig Output



Command:



dig google.com



From output:



A record → (example) 142.250.x.x



TTL → (example) 300 seconds



TTL tells how long DNS response is cached.



##### 2\. IP Addressing



What is IPv4?



An IPv4 address is a 32-bit number written in dotted decimal format.



Example:

192.168.1.10



Structure:

4 octets (0–255 each).



Public vs Private IP



Public IP → Accessible from internet (example: 8.8.8.8)



Private IP → Used inside local networks (example: 192.168.1.5)



Private IP Ranges



10.0.0.0 – 10.255.255.255



172.16.0.0 – 172.31.255.255



192.168.0.0 – 192.168.255.255



Check My IP



Command:



ip addr show



Observation:

My system IP (example: 192.168.x.x) falls under private range.



##### 3\. CIDR \& Subnetting

What does /24 mean?



In 192.168.1.0/24:



24 bits for network



8 bits for hosts



Subnet mask:

255.255.255.0



Usable Hosts



Formula:

2^(host bits) - 2



CIDR	Subnet Mask	Total IPs	Usable Hosts

/24	   255.255.255.0	 256	254

/16	  255.255.0.0	    65536	65534

/28	 255.255.255.240	  16	14

Why Do We Subnet?



Better IP management



Improve security



Reduce broadcast traffic



Separate environments (prod/dev/test)



##### 4\. Ports – The Doors to Services





What is a Port?



A port identifies a specific service on a machine.



IP = house address

Port = specific door



Common Ports

Port	Service

22	SSH

80	HTTP

443	HTTPS

53	DNS

3306	MySQL

6379	Redis

27017	MongoDB

Check Listening Ports



Command:



ss -tulpn



Example:



22 → sshd



5432 → postgres (if installed)



Matched services with ports.



##### 5\. Putting It Together



curl http://myapp.com:8080



Concepts involved:



DNS resolves myapp.com



IP routing connects to server



TCP connects to port 8080



HTTP runs at application layer



##### App Can't Reach DB at 10.0.1.50:3306



First checks:



Is 10.0.1.50 reachable? (ping)



Is port 3306 open? (nc -zv 10.0.1.50 3306)



Is database service running? (systemctl status mysql)



Firewall/security group rules



What I Learned



DNS translates names to IP before any connection happens



CIDR controls how many devices can exist in a network



Ports define which service you're talking to



Networking issues can exist at DNS, IP, port, or application layer

