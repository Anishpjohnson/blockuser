# Block User Auth0
----

# Pre-Request:
- install pyhton3
- please mention the user id (which we need to disable) under app.py
- please create .env file with crediantials of Auth0

> Sample env file look like below:
vi .env
```
AUTH0_DOMAIN=phenotips-staging.auth0.com
AUTH0_CLIENT_ID=***************************
AUTH0_CLIENT_SECRET=***************************
```

# How to Use:
```
pip3 install -r requirments.txt
python3 app.py
```

# Output
```
$ python3 app.py
<Response [200]>
<Response [200]>
```
