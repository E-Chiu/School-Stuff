#!/bin/sh

sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# Allow two-way traffic
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH and ICMP pings
sudo iptables -A INPUT -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p icmp -m icmp --icmp-type 8 -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -p icmp -m icmp --icmp-type 8 -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -p icmp -m icmp --icmp-type 0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -p icmp -m icmp --icmp-type 0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Deny incoming traffic to Linux
sudo iptables -A INPUT -s 10.229.2.0/24 -d 10.229.1.1 -p tcp -m tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j DROP
sudo iptables -A INPUT -s 10.229.2.0/24 -d 10.229.1.1 -p tcp -m tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j DROP
sudo iptables -A INPUT -s 10.229.2.0/24 -d 10.229.1.1 -p tcp -m tcp --dport 20 -m conntrack --ctstate NEW,ESTABLISHED -j DROP
sudo iptables -A INPUT -s 10.229.2.0/24 -d 10.229.1.1 -p tcp -m tcp --dport 21 -m conntrack --ctstate NEW,ESTABLISHED -j DROP

# Allow incoming traffic to Linux
sudo iptables -A INPUT -p tcp -m tcp --dport 20 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 21 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --sport 1024:65535 --dport 1024:65535 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -s 10.229.1.0/24 -j ACCEPT

# Deny incoming traffic to Windows
sudo iptables -A FORWARD -s 10.229.3.0/24 -p tcp -m tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j DROP
sudo iptables -A FORWARD -s 10.229.3.0/24 -p tcp -m tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j DROP
sudo iptables -A FORWARD -s 10.229.3.0/24 -p tcp -m tcp --dport 20 -m conntrack --ctstate NEW,ESTABLISHED -j DROP
sudo iptables -A FORWARD -s 10.229.3.0/24 -p tcp -m tcp --dport 21 -m conntrack --ctstate NEW,ESTABLISHED -j DROP

# Allow incoming traffic to Windows
sudo iptables -A FORWARD -p tcp -m tcp --dport 20 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -p tcp -m tcp --dport 21 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -p tcp -m tcp --sport 1024:65535 --dport 1024:65535 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -p tcp -m tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -p tcp -m tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Deny outgoing traffic from Windows
sudo iptables -A FORWARD -s 10.229.1.2 -d 10.229.3.0/24 -j DROP

# Allow outgoing traffic
sudo iptables -A OUTPUT -p tcp -m tcp --dport 20 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 21 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --sport 1024:65535 --dport 1024:65535 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --sport 443 -m conntrack --ctstate ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -s 10.229.1.0/24 -j ACCEPT
sudo iptables -A FORWARD -s 10.229.1.0/24 -j ACCEPT

# Logging rules to log all dropped packets
sudo iptables -N LOGGING
sudo iptables -A INPUT -j LOGGING
sudo iptables -A OUTPUT -j LOGGING
sudo iptables -A FORWARD -j LOGGING
sudo iptables -A LOGGING -j LOG --log-prefix "DROPPED: " --log-level 4
sudo iptables -A LOGGING -j DROP

# Default rule
sudo iptables -P INPUT DROP
