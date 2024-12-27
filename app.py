from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_custom_domain():
    # Get the full host (domain + port)
    full_host = request.host

    # Extract the domain name only (without port)
    domain_name = request.host.split(':')[0]
    
    return jsonify({
        "full_host": full_host,
        "domain_name": domain_name
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
