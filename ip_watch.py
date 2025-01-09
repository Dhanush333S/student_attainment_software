import socket
import time
import requests

# Flask server credentials
FLASK_URL = "https://studentattainment.pythonanywhere.com/write"  # Replace with your actual Flask server URL
AUTHORIZED_USERNAME = "100bd919fc25d9aea85cf1400c52e6a1558357330a0b9f5550a521d41e5226c4"  # Replace with your username
AUTHORIZED_PASSWORD = "3394b4c8e567604828bc7d8f8ffed599d9821706b5a13c2dd3d64501a67dbf9c"  # Replace with your password

def get_local_ip():
    """Get the local IP address of the machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Connect to a remote server to determine the local IP address (it won't actually connect).
        s.connect(('10.254.254.254', 1))  # You can change this IP to any remote address.
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'  # Default to localhost if unable to find the IP
    finally:
        s.close()
    return local_ip

def update_ip(ip_address):
    """Send the updated IP address to the Flask server."""
    data = {
        "username": AUTHORIZED_USERNAME,
        "password": AUTHORIZED_PASSWORD,
        "ip_address": ip_address
    }
    try:
        response = requests.post(FLASK_URL, data=data)
        if response.status_code == 200:
            print(f"IP address successfully updated to {ip_address} on the server.")
        else:
            print(f"Failed to update IP: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error while sending the IP address: {e}")

def monitor_ip():
    """Monitor the local IP address and send updates if it changes."""
    current_ip = get_local_ip()
    print(f"Initial Local IP: {current_ip}")
    update_ip(current_ip)  # Send the initial IP to the server

    while True:
        time.sleep(5)  # Check every 5 seconds
        new_ip = get_local_ip()
        if new_ip != current_ip:
            print(f"IP changed! New Local IP: {new_ip}")
            update_ip(new_ip)  # Send the updated IP to the server
            current_ip = new_ip

# Start monitoring
monitor_ip()
