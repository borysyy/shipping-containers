import os
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    @classmethod
    def get_all(cls):
        return cls.query.order_by(desc(Messages.id)).all()


# Home page
@app.route("/", methods=["GET"])
def index():
  current_messages = Messages.get_all()
  
  return render_template("index.html", current_messages=current_messages)


# Save the message
@app.route("/save_message", methods=["POST"])
def save_message():
    if request.method == "POST":
                
        data = request.get_json();
        name = data.get("name")
        message = data.get("message")
        
        new_message = Messages(
            name = name,
            message = message
        )
        
        db.session.add(new_message)
        db.session.commit()
        
        return jsonify({"status": "success", "message": "Message saved!"})

    

        
    

if __name__ == '__main__':
    app.run(debug=True)