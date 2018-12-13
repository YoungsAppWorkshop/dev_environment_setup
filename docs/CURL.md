# Curl Use Cases



### Synopsis
```
curl [options] [URL...]
```



### Options


* `-d`    : (HTTP) Sends the specified data in a POST request to the HTTP server


* `-i`    : (HTTP) Include the HTTP-header in the output


* `-H`    : (HTTP) Extra header to include in the request when sending HTTP to a server


* `-u`, `--user <user:password>`
  - Specify the user name and password to use for server authentication. Overrides -n, --netrc and --netrc-optional


* `-v`, `--verbose`
  - Be more verbose/talkative during the operation. Useful for debugging and seeing what's going on "under the  hood".


* `-O`, `--remote-name`
  - Write output to a local file named like the remote file we  get.


### Examples


* GET requests
```
curl -X GET -u user:password -i http://www.example.com/path
curl -v -u token:blank -i http://www.example.com/path
```


* POST requests
```
curl -X POST -H "Content-Type: application/json" -d '{"username":"young", "password": "1234"}' -i http://www.example.com/path
```



* Download Resources
```
curl -O http://download.redis.io/redis-stable.tar.gz
```



### Resources
* [Oracle Curl Man Page](https://docs.oracle.com/cd/E86824_01/html/E54763/curl-1.html)
