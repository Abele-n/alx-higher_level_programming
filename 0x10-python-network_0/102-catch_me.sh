#!bin/bash
# scipt that causes the server to respond with You got me
curl -s -X POST "$http://0.0.0.0:5000/catch_me" -d "user_id=98"
