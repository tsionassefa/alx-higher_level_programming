#!/bin/bash
# send a POST request to the passed URL using curl, and display 
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

