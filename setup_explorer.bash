#!/bin/bash

if [[ $EUID > 0 ]]; then
  echo "This script requires sudo"
  exit 1
fi

echo "Type a new password for connecting to the explorer web gui"
read -p "Password: " -s password
echo

while [ -z "$password" ]; do
  echo "Password cannot be blank"
  read -p "Password: " -s password
  echo
done

echo -n $password | md5sum | cut -d ' ' -f 1 > /opt/brickpiexplorer/passwd.md5
