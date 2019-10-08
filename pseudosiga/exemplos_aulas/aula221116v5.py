from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('echo4.html')

@app.route("/aprovado", methods=['POST'])
def echo():
  p1 = int(request.form("p1"))
  p2 = int(request.form("p2"))
  if (((p1+p2)/2)>= 7):
    return render_template('aprovado.html')
  else:
    p3 = ((p1+p2)/2)
    return render_template('provafinal.html')
    
@app.route("/provafinal")
def echo():
  p1 = int(request.form("p1"))
  p2 = int(request.form("p2"))
  p3 = ((p1+p2)/2)
  if (p3 < 5):
    return render_template('reprovado.html')

@app.route("/reprovado", methods=['POST'])
def echo():
    return render_template('reprovado.html')

if __name__ == "__main__":
    app.run(debug=True)