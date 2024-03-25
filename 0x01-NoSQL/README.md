# NoSQL

## Objectives
- What NoSQL means.
- What is the difference between SQL and NoSQL.
- What is ACID.
- What is document storage.
- What are NoSQL types.
- Benefits of NoSQL database.
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database.
- How to use MongoDB

## Environment
- Languages: Python3
- Ubuntu: 20.04 LTS

## Install MongoDB 4.2 in Ubuntu
```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$
```
## Install pymongo
```
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating
```
$ sudo mkdir -p /data/db
```

## To Note:
Most commands used for this project are not up to date with the latest mongo db.
Check the documentation [here](https://www.mongodb.com/docs/manual/).
