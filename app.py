##import flask 
from flask import Flask, request

app = Flask(__name__)

def reverse_ip_address(ip):
    # Reverse the IP address
    reversed_ip = '.'.join(ip.split('.')[::-1])
    return reversed_ip

@app.route('/')
def get_reverse_ip_address():
    # Get the client's public IP address from the request headers
    get_client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # # If there are multiple IP addresses (due to proxies), use the first one
    # client_ip = client_ip.split(',')[0].strip() ## would uncomment this later for testing
    
    # Reverse the public IP address
    reversed_public_ip = reverse_ip_address(get_client_ip)
    
    return f'Here you go, your reversed public IP: {reversed_public_ip}'

if __name__ == '__main__':
    app.run(debug=True)
