## Deploy React App using Apache 2.4



### 1. Prepare React App to be Deployed

* Build Production code: `npm run build` or `yarn build`

* Move all files/directories into document root:
  - ex) `/var/www/html`



### 2. Configure Apache Server

* Enable `mod_rewrite`: `sudo a2enmod rewrite`

* Configure Apache VirtualHost: `/etc/apache2/sites-available/YOUR_APP_CONFIGURATION.conf`
```
<VirtualHost *:80>
        ServerName example.com
        ServerAlias www.example.com
        ServerAdmin webmaster@example.com

        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        <Directory "/var/www/html">
                RewriteEngine on
                # Don't rewrite files or directories
                RewriteCond %{REQUEST_FILENAME} -f [OR]
                RewriteCond %{REQUEST_FILENAME} -d
                RewriteRule ^ - [L]
                # Rewrite everything else to index.html to allow html5 state links
                RewriteRule ^ index.html [L]
        </Directory>
</VirtualHost>
```

* Enable New Configuration: `sudo a2ensite YOUR_APP_CONFIGURATION.conf`

* Restart Server: `sudo apache2ctl restart`



### 3. Resources
* [Create-React-App Docs](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#deployment)
* [Apache Module mod_rewrite](https://httpd.apache.org/docs/2.4/mod/mod_rewrite.html)
* [VirtualHost configuration](https://gkedge.gitbooks.io/react-router-in-the-real/content/apache.html)
