from flask import Flask

app =Flask(__name__)

@app.route("/")
def name():
    return "Sri Ranga Sujeevan" 


@app.route("/registerNumber")
def register_number():
    return "22IT058"





@app.route("/department")
def department():
    return "IT(Information Technology)"

if __name__ == "__main__":
    app.run(debug =True)
    
      