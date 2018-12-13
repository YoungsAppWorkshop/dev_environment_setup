## Linux(Ubuntu 16.04 LTS) Setup

### 1. Linux Settings Guide
* Resources:
  - [Initial Server Setup with Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)
  - [How to Secure Your Server](https://linode.com/docs/security/securing-your-server/)

### 2. Setting up locale (if necessary)
* Resources: [Setting locales correctly on Mac OSX Terminal application](https://blog.remibergsma.com/2012/07/10/setting-locales-correctly-on-mac-osx-terminal-application/)

### 3. Update/Upgrade Packages
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

### 4. Create a New User as a sudoer
```
sudo su
adduser USER_NAME
echo "USER_NAME ALL=(ALL:ALL) ALL" > /etc/sudoers.d/USER_NAME
exit
```

* Resources:
  - [Sudoers](https://help.ubuntu.com/community/Sudoers)
  - [Linux Tips: Password Usage in Sudo (PASSWD / NOPASSWD)](http://www.ducea.com/2006/06/18/linux-tips-password-usage-in-sudo-passwd-nopasswd/)

### 5. Secure SSH Connection

* Forcing Key based Authentication
  * On Local machine, generate key pairs with `ssh-keygen -t rsa -b 4096`
  * On Server in home directory (`/home/USER_NAME`):
```
mkdir .ssh
touch .ssh/authorized_keys
# Copy and Paste the Public Key in authorized_keys
vi .ssh/authorized_keys
chmod 700 .ssh
chmod 644 .ssh/authorized_keys
```

* Modify SSH Configuration file
  - `sudo vi /etc/ssh/sshd_config`
```
Port 2200
PermitRootLogin no
PasswordAuthentication no
AddressFamily inet
```

  - `sudo systemctl restart sshd`

* Resources: [SSH-Keygen](https://www.digitalocean.com/community/questions/setting-up-ubuntu?answer=34263)

### 6. Set Up Time Synchronization

* Set Time Zone
```
# Check Current Date/Time
date
# List all available Timezones
timedatectl list-timezones
# Set Timezone: Asia/Seoul
sudo timedatectl set-timezone Asia/Seoul
# Check if Time Synchronization is enabled
timedatectl
```

* Resources: [How To Set Up Time Synchronization on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-time-synchronization-on-ubuntu-16-04)

### 7. Set Up Firewall using ufw

* Using `ufw`
```
sudo ufw status verbose
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 123
sudo ufw allow 2200/tcp
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

* Resources
  - [How To Set Up a Firewall with UFW on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-14-04)
  - [UFW Essentials: Common Firewall Rules and Commands](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)

### 8. Set Up Automatic Security Update

* Install and activate `unattended-upgrades` package
```
sudo apt-get install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
# To verify it's properly set
sudo vi /etc/apt/apt.conf.d/20auto-upgrades
sudo vi /etc/apt/apt.conf.d/50unattended-upgrades
```

* Resources: [Automatic Security Updates](https://help.ubuntu.com/community/AutomaticSecurityUpdates)

### 9. Set Up Mail System using Postfix
* Resources: [How To Install and Configure Postfix on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-16-04)

### 10. Set Up Fail2Ban

* Install: `sudo apt-get install fail2ban`

* Modify Configuration:
  - `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`
  - `sudo vi /etc/fail2ban/jail.local`
```
# Whitelist YOUR_PUBLIC_IP_ADDRESS
ignoreip = 127.0.0.1/8 YOUR_PUBLIC_IP_ADDRESS
# Ban the IP permanently
bantime  = -1
# Set Email Notification
destemail = RECEIVER@EMAIL.COM
sender = SENDER@EMAIL.COM
# Ban and send an email with a WhoIs report
action = %(action_mw)s
```

* Resources: [Use Fail2ban to Secure Your Server](https://linode.com/docs/security/using-fail2ban-for-security/)

### 11. Set Up Monitoring System

* Resources:
  - [How To Install Nagios 4 and Monitor Your Servers on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-nagios-4-and-monitor-your-servers-on-ubuntu-14-04)
  - [How To Install the Munin Monitoring Tool on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-munin-monitoring-tool-on-ubuntu-14-04)
