# CentOS 7 LAMP/Laravel Setup


### 1. Install Apache Server

```bash
# Install Apache
sudo yum install httpd
# Start the server
sudo systemctl start httpd.service
# Enable Apache to start on boot
sudo systemctl enable httpd.service
```



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



### 3. Install PHP 7.1 for Laravel

* Laravel 5.5 depends on PHP 7.0+, and PHP 7.1 is not provided by the official RHEL repository so it is required to add "Webtatic" repo in order to install it easily.
```bash
# Install EPEL repository with the following command
sudo yum install epel-release
# Add the Webtatic repo
sudo rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
# Update the repository list
sudo yum repolist
# Install PHP 7.1 and the needed extensions
sudo yum install php71w php71w-common php71w-gd php71w-phar php71w-xml php71w-cli php71w-mbstring php71w-tokenizer php71w-openssl php71w-pdo
```

* Test PHP processing on the Web Server: `sudo vi /var/www/html/info.php`
```php
<?php phpinfo(); ?>
```



### 4. Install Laravel

* For installing the latest version of Laravel, get the Composer dependency manager
```bash
curl -sS https://getcomposer.org/installer | php
```

* Execute the following command to move Composer binary file to the executable path
```bash
mv composer.phar /usr/local/bin/composer
```

* Download and install Laravel directly into Apache document root:
```bash
composer create-project laravel/laravel /var/www/laravel
```



### 5. Set the correct DocumentRoot

* Open the HTTPD global configuration file: `vi /etc/httpd/conf/httpd.conf`
```bash
# Find the line that refers to:
DocumentRoot "/var/www/laravel"
# And change it like below:
DocumentRoot "/var/www/laravel/public"
# Then save and exit.
```

* Restart Apache to take effect:
```bash
systemctl restart httpd
```



### 6. Set the Permissions

* Execute the following command one by one to set the proper permissions:
```bash
sudo chmod -R 775 /var/www/laravel
sudo chown -R apache.apache /var/www/laravel
sudo chmod -R 777 /var/www/laravel/storage/
```

* SELinux related issues
```bash
# Prove this is the problem by turning off selinux with the command
setenforce 0
# This should allow writing, but you've turned off added security server-wide. That's bad. Turn SELinux back
setenforce1
# Then finally use SELinux to allow writing of the file by using this command
chcon -R -t httpd_sys_rw_content_t storage
```

* If your Firewall is active you should execute the following commands in order to allow HTTP and HTTPS ports:
```bash
firewall-cmd –permanent –add-port=80/tcp
firewall-cmd –permanent –add-port=443/tcp
```



### Resources
* [How To Install Linux, Apache, MySQL, PHP (LAMP) stack On CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-centos-7)
* [How to install MySQL 5.6 on CentOS 7](https://dbahire.com/how-to-install-mysql-5-6-on-centos-7/)
* Permissions
  - [Stack Overflow](https://stackoverflow.com/questions/37257975/permissions-issue-with-laravel-on-centos)
  - [Techmint](https://www.tecmint.com/install-laravel-in-centos/)
  - [LaraCast](https://laracasts.com/discuss/channels/laravel/laravel5-gives-blank-page-with-500-status-code-on-apache-fedora22/replies/98874)
