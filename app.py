from  flask import Flask
app=Flask(__name)
@app.route("/")
def home():
  return "Hello!My python app is deployed successfully on Azure."
if __name__=="__main__":
app.run()
