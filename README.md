# Flag Raiser

## Description
The purpose of this program is create a compiled python file that can be added into a VM instance to check for different characteristics about the machine. 

Flag strings can also be added into the checks as needed.

## Getting Started
### Prerequisites
**Download the git directory**
```bash
git clone https://github.com/Ka5pyr/FlagRaiser.git
cd FlagRaiser
```
**_Recommended Virtual Environment_**
```bash
python3 -m venv venv
source venv/bin/activate
```
**Install Requirements**
```bash
pip install -r requirements.txt
```

## Usage
### Run a test without creating an executable
```bash
python3 main.py -T --db-path="./templates" --db-file="flag-check-template.py"
```
### Creating an Executable
```bash
python3 main.py -B -dP="./templates" -dF="flag-check-template.py" -oF="flag-test"
```

## DB File Creation
### Description
The DB file is actually a json file turned into a Python Dictionary. The reason for this is so that it can be compiled along side the main program.

### Creating the DB File
The file must include "title" and "checks" keys.
The title is for the name of the check as a whole.

```"title": "Ping Checker"```

The "checks" key is connected to a list of dictionaries which includes all the checks the program will run through.

```"checks": [{}]```

Inside each dictionary must include the following:
- **"name": ""**
  + A name of the check itself
- **"description": ""**
  + A brief synopsis of the check
- **"type": ""**
  + What type of check is being run
- "success_flag": ""
  + The flag for the successful completion of the check
  + "" (empty string) if there is no flag wanted
- "print_success": BOOLEAN
  + Print information about the check on success
- "suggestions": ["",""]
  + A list of possible suggestions for the user to get a successful check
- "resources": ["",""]
  + A list of resources to references about the topic of the specific check

### Current Check Types:
#### Adapter Check:
- **Description:**
  + Check to see if a specified Adapter exists
  
- **Required Keys:**
  + "adapter_name" : Name of the Adapter to look for
  
- **Example:**
  + ```"adapter_name" : "eth0"```
#### Adapter Count:
- **Description:**
  + Check to see if a specified number of Adapters exists
  
- **Required Keys:**
  + "adapter_count" : Number of Adapters to look for
  
- **Example:**
  + ```"adapter_count" : 2```
#### Adapter Up:
- **Description:**
  + Check to see if a specified Adapter is classified 'Up'
  
- **Required Keys:**
  + "adapter_name" : Name of the Adapter to look for
  
- **Example:**
  + ```"adapter_name" : "eth0"```
#### Gateway Check:
- **Description:**
  + Check to see if the current gateway IPv4 Address is correct for a specified Network Adapter
  
- **Required Keys:**
  + "adapter_name" : Name of the Adapter to look for
  + "ipv4_address" : Specified IPv4 Address of the expected Gateway
  
- **Example:**
  + ```"adapter_name" : "eth0"```
  + ```"ipv4_address" : "192.168.1.1"```
#### IPv4 Check:
- **Description:**
  + Check to see if the current IPv4 Address is correct for a specified Network Adapter
  
- **Required Keys:**
  + "adapter_name" : Name of the Adapter to look for
  + "ipv4_address" : Specified IPv4 Address of the expected IPv4 Address
  
- **Example:**
  + ```"adapter_name" : "eth0"```
  + ```"ipv4_address" : "192.168.1.1"```
#### Ping Test:
- **Description:**
  + Check to see the machine can ping a list of web addresses and IP's
  
- **Required Keys:**
  + "addresses" : List of web addresses and IP's
  
- **Example:**
  + ```"addresses" : ["192.168.1.1", "example.com", "nasa.gov"]```
#### Subnet Check:
- **Description:**
  + Check to see if a specified network adapter is on the correct subnet
  
- **Required Keys:**
  + "adapter_name" : Name of the Adapter to look for
  + "subnet" : subnet IPv4 Address
  
- **Example:**
  + ```"adapter_name" : "eth0"```
  + ```"subnet" : "192.168.1.0/24"```
## Deployment

## Author: