#!/bin/bash

if [[ $EUID > 0 ]]; then
  echo "This script requires sudo"
  exit 1
fi

read -p "College username: " user
read -p "Password: " -s passwd
echo

# hash the password
hash=$(echo -n $passwd | iconv -t utf16le | openssl md4 -r | cut -d" " -f1)

cat <<EOT >>/etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB

network={
	ssid="Imperial-WPA"
	priority=1
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="${user}@ic.ac.uk"
	password=hash:${hash}
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
}
EOT

systemctl restart wpa_supplicant_wlan0.service
