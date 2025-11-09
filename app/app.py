from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { margin-top: 0; }
        .button {
            background: white;
            color: #667eea;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Welcome to My Flask App!</h1>
        <p>This app is running on Fly.io</p>
        <p>Visit counter: {{ counter }}</p>
        <a href="/about" class="button">About Page</a>
    </div>
</body>
</html>
"""

ABOUT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>About - My Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { margin-top: 0; }
        .button {
            background: white;
            color: #667eea;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            display: inline-block;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📖 About This App</h1>
        <p>This is a simple Flask web application deployed on Fly.io!</p>
        <p>Built with Python and Flask.</p>
        <a href="/" class="button">Back to Home</a>
    </div>
</body>
</html>
"""

visit_counter = 0

@app.route('/')
def home():
    global visit_counter
    visit_counter += 1
    return render_template_string(HOME_TEMPLATE, counter=visit_counter)

@app.route('/about')
def about():
    return render_template_string(ABOUT_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
