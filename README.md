# restful-api-contract
A "batteries included" document generator and Mock server for RESTful API contract

##Demo

####Demo Site
[http://yulix-demo-api-contract.daoapp.io/](http://yulix-demo-api-contract.daoapp.io/)

####Snapshot
![](http://o6j1da0aj.bkt.clouddn.com/image/png/demo_api_contract_en.png)

##Quick start

####Copy the example
$ ./init.py 
####Build Docker image
docker build -t demo .
####Run container
docker run -d -p 8080:5000 demo
####Open browser and visit http://localhost:8080



