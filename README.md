# GoogleDDNSClient
Upload your IP to Google Dynamic DNS recorder.
## Why use it
If the IP of your server is changing or you start a new server but don't  know what's the IP, you can use the docker to upload your IP to Google Domain


## How to use

#### build docker
* **Username** : AWS Dynamic DNS-> credential of ***Username***
* **Password** : AWS Dynamic DNS-> credential of ***Password***
* **Domain_name**: your domain name of the Dynamic DNS

#### run docker

```docker run
docker pull qinbatista/googleddnsclient && docker run -itd qinbatista/googleddnsclient
```

#### build on Apple Silicon
```
--platform linux/amd64
```
# Docker-AWS-DDNS-US
# Docker-AWS-DDNS-US
