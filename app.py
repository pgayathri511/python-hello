from  flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
  return """
  <h1>Azure Cloud Project</h1>
  <h2>Python Web Application</h2>
  <p>My python application is deployed successfully on Microsoft Azure.</p>
  """
if __name__=="__main__":
  app.run()
