from flask import Flask, request

app = Flask(__name__)

def reverse_ip(ip):
    # Reverse the IP address
    reversed_ip = '.'.join(ip.split('.')[::-1])
    return reversed_ip

@app.route('/')
def get_reverse_ip():
    # Get the client's IP address from the request headers
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # If there are multiple IP addresses (due to proxies), use the first one
    client_ip = client_ip.split(',')[0].strip()
    
    # Reverse the IP address
    reversed_ip = reverse_ip(client_ip)
    
    return f'Reversed IP: {reversed_ip}'

if __name__ == '__main__':
    app.run(debug=True)
