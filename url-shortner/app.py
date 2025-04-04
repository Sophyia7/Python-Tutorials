from flask import Flask, request, render_template, redirect 
from flask_sqlalchemy import SQLAlchemy 
import string, random 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

class URL(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  original_url = db.Column(db.String(500), nullable=False)
  short_code = db.Column(db.String(15), unique=True, nullable=False)

def generate_short_code(length=10):
  characters = string.ascii_letters + string.digits
  return ''.join(random.choices(characters, k=length))
  

@app.before_request
def create_table():
  db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    original_url = request.form['url']
    short_code = generate_short_code()
    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    return f"Shortened URL: {request.host}/{short_code}"
  return render_template('index.html')

@app.route('/<short_code>')
def redirect_url(short_code):
  url_entry = URL.query.filter_by(short_code=short_code).first()
  if url_entry:
    return redirect(url_entry.original_url)
  else:
    return "URL not found!", 404 


if __name__ == '__main__':
  app.run(debug=False)