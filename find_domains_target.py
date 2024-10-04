import socket
from concurrent.futures import ThreadPoolExecutor

def ip_to_domain(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return ip_address, domain_name
    except socket.herror:
        return ip_address, None  # Return None if the IP address cannot be resolved to a domain

def resolve_ips_in_bulk(ip_list):
    results = {}
    with ThreadPoolExecutor(max_workers=10) as executor:  # You can adjust the number of workers
        futures = {executor.submit(ip_to_domain, ip): ip for ip in ip_list}
        
        for future in futures:
            ip, domain = future.result()
            results[ip] = domain
    
    return results

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read lines and strip whitespace/newlines
        return [line.strip() for line in file if line.strip()]

# Example usage
ip_file = 'ips.txt'
ip_addresses = read_ips_from_file(ip_file)

domains = resolve_ips_in_bulk(ip_addresses)

keyword = input("enter search domain: ")
for ip, domain in domains.items():
    if domain and keyword in domain:
        print(f"The domain for IP {ip} is {domain}.")
    else:
        print(f"The domain for IP {ip} is {domain}.")
        
