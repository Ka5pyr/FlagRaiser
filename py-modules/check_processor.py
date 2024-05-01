import sys

sys.path.append('./py-modules/')
import net_info
import format_message


def adapter_check(check):
    try: 
        adapter = check['adapter_name']
        if net_info.check_adapter_exists(adapter):
            format_message.print_check_pass(check)
        else:
            issue = f"Adapter '{adapter}' does not exist"
            format_message.print_check_fail(check, issue)
            sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")

def adapter_count(check):
    correct_adapter_amount = check['adapter_amount']
    current_adapter_count = net_info.get_adapter_amount()

    if current_adapter_count == (correct_adapter_amount + 1):
        format_message.print_check_pass(check)
    else:
        issue = f"Adapter count is {current_adapter_count} instead of {correct_adapter_amount + 1}"
        format_message.print_check_fail(check, issue)
        sys.exit(0)
        
def adapter_up(check):
    adapter = check['adapter_name']
    if net_info.get_adapter_status(adapter):
        format_message.print_check_pass(check)
    else:
        issue = f"Adapter '{adapter}' is down"
        format_message.print_check_fail(check, issue)
        sys.exit(0)

# Check to see if the Gateway is set correctly
def gateway_check(check):
    ip_addr = check['ipv4_address'] 
    adapter = check['adapter_name']
    gateway = net_info.get_gateway(adapter)

    if gateway[0].isalpha():
        issue = f"Adapter '{adapter}' does not have a default route"
        format_message.print_check_fail(check, issue)
    elif ip_addr == gateway:
        format_message.print_check_pass(check)
    else:
        issue = f"Gateway IP Address '{gateway}' does not match '{ip_addr}'"
        format_message.print_check_fail(check, issue)

# Function to Validate the Correct IP Address is Assigned
def ipv4_check(check):
    correct_ip = check['ipv4_address']
    adapter = check['adapter_name']
    if net_info.check_adapter_exists(adapter):
        current_ip = net_info.get_ipv4_address(adapter)
    
        if correct_ip == current_ip:
            format_message.print_check_pass(check)
        else:
            issue = f"IP Address '{correct_ip}' does not match Current IPv4 Address '{current_ip}'"
            format_message.print_check_fail(check, issue)
            sys.exit(0)
    else:
        issue = f"Adapter '{adapter}' does not exist"
        format_message.print_check_fail(check, issue)
        sys.exit(0)

def ping_test(check):
    addresses = check['addresses']
    for address in addresses:
        if not net_info.ping_test(address):
            issue = f"Ping test failed for {address}"
            format_message.print_check_fail(check, issue)
            sys.exit(0)
    format_message.print_check_pass(check)

def subnet_check(check):
    subnet = check['subnet']
    adapter = check['adapter_name']
    ipv4_addr = net_info.get_ipv4_address(adapter)

    if ipv4_addr is not None:
        if net_info.check_subnet(ipv4_addr, subnet):
            format_message.print_check_pass(check)
        else:
            issue = "Adapter is not on the correct subnet"
            format_message.print_check_fail(check, issue)
            sys.exit(0)
    else:
        issue = "Make sure the adapter is enabled"
        format_message.print_check_fail(check, issue)
        sys.exit(0)

# Verify there is at least one check to process
def check_checks_amount(checks):
    if len(checks) == 0:
        print("No checks found in the file.")
        sys.exit(0)

# Function to process the checks from the JSON Check File
def process_checks():
    import db
    
    data = db.data
    checks = data['checks']
    title = data['title']
    
    # Verify there are checks to process
    check_checks_amount(checks)

    # Print the title
    format_message.print_title(title)
    
    # Parse through the checks
    for check in checks:
        # print(f"Check: {check['name']}")
        if check['type'] == 'adapter_check':    
            adapter_check(check)
        elif check['type'] == 'adapter_count':
            adapter_count(check)
        elif check['type'] == 'adapter_up':
            adapter_up(check)
        elif check['type'] == 'gateway_check':
            gateway_check(check)
        elif check['type'] == 'ipv4_check':
            ipv4_check(check)
        elif check['type'] == 'ping_test':
            subnet_check(check)
        elif check['type'] == 'subnet_check':
            subnet_check(check)
        else:
            print(f"Error: Unknown check type '{check['type']}'")
            sys.exit(0)