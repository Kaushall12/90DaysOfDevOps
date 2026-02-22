#### Networking Fundamentals \& Hands-on Checks





##### 1\. OSI vs TCP/IP 



OSI Model (7 Layers)



L1 Physical → cables, signals



L2 Data Link → MAC address, switching



L3 Network → IP addressing \& routing



L4 Transport → TCP/UDP (ports)



L5 Session → session management



L6 Presentation → encryption (SSL/TLS)



L7 Application → HTTP, DNS, FTP



TCP/IP Model (4 Layers)



Link → hardware + MAC



Internet → IP addressing



Transport → TCP/UDP



Application → HTTP, HTTPS, DNS



Simpler mapping:

OSI is conceptual. TCP/IP is practical.



##### 

##### 2\. Hands-on Networking Checks



Target used: google.com



Identity Check



hostname -I



Observation:

Displayed local machine IP address.



Alternative:

ip addr show



Reachability



ping google.com



Observation:

Low latency, 0% packet loss → internet working.



Path Check



traceroute google.com



Observation:

Multiple hops through ISP routers. No major timeouts.



Listening Ports



ss -tulpn



Observation:

SSH running on port 22.

Docker or other services visible (if running).



DNS Resolution



dig google.com



Observation:

Returned public IP address.

Confirms DNS resolution working.



HTTP Check



curl -I https://google.com



Observation:

HTTP/2 200 status.

Confirms application layer reachable.



Connections Snapshot



netstat -an | head



Observation:

Saw LISTEN and ESTABLISHED states.

Shows active connections.



##### 3\. Mini Task – Port Probe



Identified port 22 (SSH):



ss -tulpn | grep 22



Tested locally:



nc -zv localhost 22



Result:

Connection succeeded.



If failed:

Next check → systemctl status ssh

Then → sudo ufw status



##### 4\. Reflection





Fastest Signal When Something Breaks



ping and curl -I

They quickly show if network or application is failing.



If DNS Fails



Check:

dig domain

Inspect Application layer (DNS).



If HTTP 500 Appears



Check:



Application logs



systemctl status service



journalctl -u service



Two Real Incident Follow-Ups



Check firewall rules (ufw status or security groups)



Check service logs for errors

