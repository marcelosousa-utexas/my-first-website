from flask import Flask, render_template

class flask_interface():
  app = Flask(__name__)
  
  @app.route("/")
  def hello_word():
    return render_template("home.html")
    #return "<p> Hello, world <p>"

  #if __name__ == "__name__":  
  if __name__ == "app":
    print("hello2")
    app.run(host = '0.0.0.0', debug = True)