import ipaddress
import socket
import subprocess
from sys import stderr

import psutil

def verify_valid_ip(ip_addr):
    try:
        ipaddress.ip_address(ip_addr)
        return True
    except ValueError:
        return False

# Check to see if a network interface exists
def check_adapter_exists(adapter):
    return adapter in psutil.net_if_addrs()
    
# Grab all the info about the specified network interface
def check_subnet(ipv4, subnet):
    ip_addr_obj = ipaddress.ip_address(ipv4)
    ip_network = ipaddress.ip_network(subnet)
    return ip_addr_obj in ip_network

def get_adapter_amount():
    adapters = list(psutil.net_if_addrs().keys())
    return len(adapters)
    
def get_adapter_status(adapter):
    adapter_info = psutil.net_if_stats()
    return adapter_info[adapter].isup

def get_ipv4_address(adapter):
    for address in psutil.net_if_addrs()[adapter]:
        if address.family == socket.AF_INET:
            return address.address
    else:
        return None

def get_gateway(subnet):
    try:
        # Run the `ip route` command on subnet
        result = subprocess.run(
            ["ip", "route", "show", "dev", subnet], 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True, check=True)

        if len(result.stdout) == 0:
            return "No default route found"
        # Process the output line by line
        for line in result.stdout.decode().split('\n'):
            if line.startswith('default via'):
                route_line = line.split(' ')
                gateway_ip = route_line[2]

                # Verify the gateway is a valid IP address
                if verify_valid_ip(gateway_ip):
                    return gateway_ip
                
        return "Default route not found"
    except subprocess.CalledProcessError:
        return "An error occurred while grabbing the default route"

def ping_test(ip_addr):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", ip_addr],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True, check=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False
    