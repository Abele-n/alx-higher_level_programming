#!/bin/bash
# scipt that causes the server to respond with You got me
curl -s -L -X PUT "user_id=98" -H "origin: School" 0.0.0.0:5000/catch_me
