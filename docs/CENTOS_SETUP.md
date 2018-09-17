# CentOS 7 Initial Setup

### 1. Linux Settings Guide
* Resources:
  - Super User / SSH: [Initial Server Setup with CentOS 7](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-centos-7)
  - Time Synchronization: [Setup Timezone and NTP on CentOS 6](https://www.vultr.com/docs/setup-timezone-and-ntp-on-centos-6)

### 2. Update/Upgrade Packages
```
sudo yum update
```


### 3. Create a New User as a sudoer

### 4. Secure SSH Connection

### 5. Set Up Time Synchronization
* Set the Timezone
```bash
# Check the Current timezone
date
# Using the local timezone of the server's physical location is the best practice
sudo rm -rf /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime
# Check the timezone if it's been modified
date
```

* Write the system time info into the hardware clock
  - Modify the content of this file as below: `vi /etc/sysconfig/clock`
```bash
ZONE="Asia/Seoul"
UTC=false
ARC=false
```
  - Write the system time into the hardware clock.
```bash
hwclock --systohc --localtime
```
  - Input `hwclock` to see the result.

* Configure `ntp`

* Configure the firewall

### 6. Set Up Firewall

### 7. Set Up Automatic Security Update
