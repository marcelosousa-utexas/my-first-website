from flask import Flask

class flask_interface():
  app = Flask(__name__)
  
  @app.route("/")
  def hello_word():
    return "Hello, world"
    #return "<p> Hello, world <p>"

  #if __name__ == "__name__":  
  if __name__ == "app":
    print("hello2")
    app.run(host = '0.0.0.0', debug = True)