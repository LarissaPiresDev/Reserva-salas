from flask import Flask
from config import app, db
from reservasalas.reserva_route import reservas

app.register_blueprint(reservas)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG']) 