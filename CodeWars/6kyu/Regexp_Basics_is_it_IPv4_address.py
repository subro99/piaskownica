import re
def ipv4_address(address):
    pattern = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\Z")
    result = re.search(pattern, address)
    return bool(result)