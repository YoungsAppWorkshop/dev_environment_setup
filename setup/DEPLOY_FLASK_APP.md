## Deploy Python3/Flask Apps using Apache 2.4



### 1. Install Dependencies
```
sudo apt-get install apache2
sudo apt-get install python3-pip
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libapache2-mod-wsgi-py3
```



### 2. Install Virtualenv
```
sudo pip3 install virtualenv
```



### 3. Initialize the Project
* Clone the Project Repository
  - In `/var/www/` directory: `git clone YOUR_REPOSITORY_NAME`


* Install the Project Dependencies using Virtualenv
```
sudo virtualenv venv
sudo su
. venv/bin/activate
pip3 install -r requirements.txt
# When Using Postgres DB
pip3 install psycopg2
```

* Create `.gitignore` file (if necessary)
```
*.pyc
venv/
instance/
```

* Generate Secret Key and Put it in `instance/config.py`
```
>>> import os
>>> os.urandom(24)
```

* Set up Project configuration
```
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
```

* Create `YOUR_APP_NAME.wsgi` file
```
import sys  
sys.path.insert(0, '/var/www/readable_api_server')
activate_this = '/var/www/readable_api_server/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
from app import app as application
```

* Apache2 log files
  - `/var/log/apache2/access.log`
  - `/var/log/apache2/error.log`



### 4. Deploy Your App using `.wsgi` script
* Edit: `/etc/apache2/sites-available/YOUR_APP_CONFIGURATION.conf`
```
<VirtualHost *:80>
        ServerName example.com
        ServerAlias www.example.com
        ServerAdmin webmaster@example.com

        ErrorLog ${APACHE_LOG_DIR}/YOUR_APP_NAME-error.log
        CustomLog ${APACHE_LOG_DIR}/YOUR_APP_NAME-access.log combined

        WSGIDaemonProcess YOUR_APP_NAME processes=1 threads=2
        WSGIScriptAlias / /var/www/YOUR_APP_DIRECTORY/YOUR_APP_NAME.wsgi

        <Directory /var/www/YOUR_APP_DIRECTORY>
                WSGIProcessGroup YOUR_APP_NAME
                WSGIApplicationGroup %{GLOBAL}
                Require all granted
        </Directory>
</VirtualHost>
```
* Enable New Configuration: `sudo a2ensite YOUR_APP_CONFIGURATION.conf`
* Restart Server: `sudo apache2ctl restart`



### 5. Database Configuration (Postgres)
* Create a New User/Role/Database (as the same name)
```
# USER_NAME == ROLE_NAME == DATABASE_NAME
sudo adduser USER_NAME
sudo -u postgres createuser --interactive   # No Super User
sudo -u postgres createdb DATABASE_NAME
```

* Set Up Postgres Database Password
```
# Connect DB as USER_NAME
sudo -u USER_NAME psql
# Check connection info
\conninfo
# Change password
\password
```



### 6. Set Web Server Files/Directories Permissions
* In `/var/www/` directory:
```
chown -R USER_NAME YOUR_APP_DIRECTORY/
chgrp -R www-data YOUR_APP_DIRECTORY/
chmod -R 750 YOUR_APP_DIRECTORY/
chmod +t YOUR_APP_DIRECTORY/
```

* In your project directory: `git config core.filemode false`



### 7. Resources
- [File Permissions - Sticky bit ](https://help.ubuntu.com/community/FilePermissions#Sticky_Bit)
- [How To Set Up Apache Virtual Hosts on Ubuntu 14.04 LTS](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts)
- [Serverfault Thread about files/folders permissions ](https://serverfault.com/questions/357108/what-permissions-should-my-website-files-folders-have-on-a-linux-webserver)
- [Stack Over Flow: What does Apache's “Require all granted” really do?](https://serverfault.com/questions/549517/what-does-apaches-require-all-granted-really-do)
- [VirtualHost Examples](https://httpd.apache.org/docs/2.4/vhosts/examples.html)
