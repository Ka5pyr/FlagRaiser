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


## Deployment

## Author: