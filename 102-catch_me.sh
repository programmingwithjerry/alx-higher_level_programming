#!bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s -L -X PUT -H "Origin: You got me!" -d "user_id=98" http://0.0.0.0:5000/catch_me
