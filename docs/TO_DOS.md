# DSME RGP project To Do List


### 1. CENTOS_SETUP



### 2. Install MySQL version 5.6 on CentOS

* Install MySQL
```bash
# Setup Oracle’s MySQL repository,
sudo yum install http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
# Check that the repository is effectively active
sudo yum repolist enabled | grep "mysql.*-community.*"
# Install the server packages
sudo yum install mysql-community-server
```

* Start/Enable MySQL
```bash
# Start MySQL
sudo systemctl start mysqld
# Enable MySQL to start on boot
sudo systemctl enable mysqld.service
# Check status of MySQL
sudo systemctl status mysqld
# Run mysql_secure_installation for security
sudo mysql_secure_installation
```

* Migrate schema



### 3. Node.js Setup

* Install NVM: [GitHub](https://github.com/creationix/nvm)

* Node.js LTS: `nvm install --lts`

* Install PM2: `npm install -g pm2`



### 4. Check if the AWS api server is connectable on the DSME server.
