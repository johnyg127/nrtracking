from flask import Flask, request, send_file
from datetime import datetime
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
# Set up simple file logging for email opens (no extra logging details)
def log_to_file(message):
    with open('tracking.txt', 'a') as log_file:
        log_file.write(message + '\n')


@app.route('/track/pixel.png')
@cross_origin()
def track_email():
    # Get the recipient's IP address
    recipient_ip = request.remote_addr

    # Create the log message in the desired format
    log_message = f"Email opened from IP {recipient_ip} at {datetime.now()}"

    # Log the message to a file
    log_to_file(log_message)

    # Serve a transparent 1x1 pixel image
    return send_file('pixel.png', mimetype='image/png')


