## SSL/TLS Encryption (Apache / Let's Encrypt )



### 1. Install Certbot
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-apache
```



### 2. Get Certificates
```
sudo certbot --apache certonly -d example.com -d www.example.com
```



### 3. Configure Apache Server
* Create `.conf` files


* Enable HTTPS VirtualHost: `sudo a2ensite example-le-ssl.conf`


* Reload Apache Server: `sudo service apache2 reload`


### 4. Automate renewal
```
sudo certbot renew --dry-run
```
