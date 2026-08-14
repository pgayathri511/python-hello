from  flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
 return """
<html>
<head>
    <title>Azure Cloud Project</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f3f6fa;
            text-align: center;
            padding: 40px;
        }

        h1 {
            color: #0078d4;
        }

        .subtitle {
            color: #555;
            font-size: 18px;
        }

        .cards {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 40px;
        }

        .card {
            background: white;
            width: 220px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 10px #ccc;
        }

        .card h2 {
            color: #0078d4;
        }

        .status {
            margin-top: 35px;
            color: green;
            font-weight: bold;
        }
    </style>
</head>

<body>

    <h1>☁️ Azure Cloud Project</h1>

    <p class="subtitle">
        Python Web Application deployed on Microsoft Azure
    </p>

    <div class="cards">

        <div class="card">
            <h2>🌐 Web App</h2>
            <p>Python application hosted on Azure</p>
        </div>

        <div class="card">
            <h2>💻 Virtual Machine</h2>
            <p>Windows VM configured in Azure</p>
        </div>

        <div class="card">
            <h2>🗄️ Storage</h2>
            <p>Azure Storage Account</p>
        </div>

        <div class="card">
            <h2>🔐 Private Endpoint</h2>
            <p>Private connection to Storage</p>
        </div>

    </div>

    <p class="status">
        ✅ Deployment Successful
    </p>

</body>
</html>
"""
if __name__=="__main__":
  app.run()
