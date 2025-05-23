from flask import Blueprint, request, jsonify
from reservasalas.reserva_model import Reserva
from database import db
import requests

reservas = Blueprint("reservas", __name__)


def validar_turma(turma_id):
    resp = requests.get(f"http://localhost:5003/turmas/{turma_id}")
    return resp.status_code == 200

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
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        } for r in reservas
    ])
