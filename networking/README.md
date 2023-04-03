# Essential Networking Commands for Linux

## Basic Commands to get Network information on Linux

- ifconfig: This command is used to display the current status of active network interfaces on your Linux system. You can use the '-a' option to show all interfaces, even those that are currently down.

- ip addr show: The  command is a powerful networking tool that allows you to view the current configuration and status of all network interfaces on your Linux system

- ping: The ping command uses the Internet Control Message Protocol (ICMP) to test network connectivity between devices. It is a layer 4 protocol that sends a request to a specific IP address and waits for a response.

- host: If you need to translate a domain name to an IP address, the host command is a reliable way to do it. It provides information about the IP address associated with a given domain name.

- ethtool: This is a powerful command-line utility that allows you to view and modify network interface settings at the kernel level. It can provide detailed information about your Ethernet adapters and diagnose problems with your network.

- dig: This command is used to retrieve DNS (Domain Name System) information for a specific domain name. It can display a wide range of information, including the IP address of the domain, the name server responsible for managing it, and other relevant details.

- whois: This command is used to retrieve information about a domain name, including the owner, administrator, and other related information. It is an essential tool for anyone who needs to perform domain name research or investigate potential cybersecurity threats.

## netstat
The netstat command is a powerful networking tool that is commonly used for troubleshooting and configuration purposes. Additionally, it can serve as a valuable monitoring tool for tracking connections over the network. Whether you need to analyze incoming and outgoing connections, inspect routing tables, monitor port listening, or gather usage statistics, the netstat command has got you covered. In this regard, understanding the basics of netstat usage and its most common applications is essential for network administrators and engineers alike.

### Using netstat with single options
```sh
netstat -a # to enlist all active ports including both tcp and udp ports
netstat -r # to inspect routing table
netstat -p # to print all ports with their process id
netstat -l # to enlist all lintening ports
netstat -e # to print all connection established ports
netstat -c # to refreshe netstat output at regular intervals
netstat -n # to display network address and port number in numeric 
```

### Run netstat combining options
```sh
netstat -at # to enlist all tcp active ports
netstat -au # to enlist all udp ports
netstat -lt # to enlist all listening tcp ports
netstat -lu # to enlist all listening udp ports
netstat -ie # to show all active interfaces. Same as ifconfig
netstat -atp # to print all tcp ports with their process id
netstat -tnl # to print all tcp and listening state port 
netstat -udp
```

### Filtering with netstat


## tcpdump

The 'tcpdump' command is a powerful network packet analyzer tool that is used to capture and analyze network traffic on a Linux system. With tcpdump, you can capture packets transmitted and received on one or more network interfaces in real-time, or you can analyze a saved capture file later. This command provides detailed information about each packet, including its source and destination IP addresses, port numbers, protocol type, packet size, and much more.

```sh
sudo apt-get install tcpdump # to instrall tcpdump
sudo tcpdump # capture all packets
sudo tcpdump -c 10 # capture 10 packets
sudo tcpdump -c 5 -A # capture 5 raw packets
sudo sudo -c 5 -i <interface-name> # capture  5 packets in a specific inerface
sudo tcpdump -i <interface-name> port <port-number> # capture packets in a specific interface's port
sudo tcpdump -XX -i <interface-name> # shows packet on ASCII format>
```
