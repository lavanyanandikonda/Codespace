from flask import Flask
import time
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask Application! Go to <a href='/htop'>/htop</a> to view system information.</h1>"

@app.route('/htop')
def htop():
    try:
        # Updated user details
        full_name = "Lavanya Nandikonda"  # Your full name
        username = "Lavanya Nandikonda"   # Your system username
        
        # Get the current server time in IST
        ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        
        # Fetch the output of the 'top' command
        try:
            top_output = subprocess.getoutput("top -bn 1")
        except Exception as e:
            top_output = f"Error fetching top command: {e}"

        # Generate the HTML content to display
        html_content = f"""
        <h1>System Info</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time in IST:</strong> {ist_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
        """
        return html_content
    except Exception as e:
        return f"<h1>Internal Server Error</h1><p>{e}</p>", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
