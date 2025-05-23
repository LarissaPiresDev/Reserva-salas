from flask import Blueprint, request, jsonify
from reservasalas.reserva_model import Reserva
from .reserva_model import listar_reservas
from database import db
import requests

schoolSystem = 'http://127.0.0.1:5003'
reservas = Blueprint("reservas", __name__)


def validar_turma(turma_id):
    resp = requests.get(f"{schoolSystem}/turmas/{turma_id}")
    return "Turma Encontrada"

@reservas.route("/reservas", methods=["POST"])
def criar_reserva():
    reserva = request.json
    turma_id = reserva.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=reserva.get("sala"),
        data=reserva.get("data"),
        hora_inicio=reserva.get("hora_inicio"),
        hora_fim=reserva.get("hora_fim")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

@reservas.route("/reservas", methods=["GET"])
def get_reservas():
    return jsonify(listar_reservas())


