#### Cloud Server Setup: Docker, Nginx \& Web Deployment







##### 1\. Launch Instance \& SSH Access

Commands Used



Check connection:



ssh -i my-key.pem ubuntu@<your-instance-ip>



Verified connection:

Successfully logged into Ubuntu cloud server.



Checked OS:

uname -a

cat /etc/os-release



##### 2\. Install Docker \& Nginx

Update System



sudo apt update \&\& sudo apt upgrade -y



Install Docker



sudo apt install docker.io -y

sudo systemctl start docker

sudo systemctl enable docker



Verify:



docker --version

sudo systemctl status docker



Install Nginx



sudo apt install nginx -y

sudo systemctl start nginx

sudo systemctl enable nginx



Verify:



systemctl status nginx



##### 3\. Security Group Configuration



Opened inbound rule:



Type: HTTP

Port: 80

Source: 0.0.0.0/0



After allowing port 80:



Visited in browser:



http://<your-instance-ip>



Result:

Nginx Welcome Page successfully loaded.





##### 4\. Extract Nginx Logs

View Logs



sudo tail -n 20 /var/log/nginx/access.log

sudo tail -n 20 /var/log/nginx/error.log



Save Logs to File



sudo cp /var/log/nginx/access.log ~/nginx-logs.txt



Verify:



cat nginx-logs.txt



Download to Local Machine



scp -i my-key.pem ubuntu@<your-instance-ip>:~/nginx-logs.txt .



Log file downloaded successfully.

