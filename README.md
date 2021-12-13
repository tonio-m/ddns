# DDNS

Usage:

```bash
# install serverless framework binary
curl -o- -L https://slss.io/install | bash

# change these variables on update_route53.py
# HOSTED_ZONE_NAME = "indigena.xyz"
# RECORD_NAME = "bisnaga.indigena.xyz"
# RECORD_TYPE = "A"
# RECORD_TTL = 300

# deploy the lambda funcion on your aws account
# be sure your aws cli is properly configured before doing this. to do this run `aws configure`
serverless deploy | grep -A1 endpoints: 
# endpoints:
#   GET - https://zf8p10v2yi.execute-api.us-east-1.amazonaws.com/

# send a get request to the endpoint to update the DNS record with your ip!!
curl https://zf8p10v2yi.execute-api.us-east-1.amazonaws.com/

# OR run a background job to update it constantly:
while true
do
    wget -qO- https://zf8p10v2yi.execute-api.us-east-1.amazonaws.com/
    sleep 1h
done
```
