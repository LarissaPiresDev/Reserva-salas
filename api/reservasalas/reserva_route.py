from flask import Blueprint, request, jsonify
from reservasalas.reserva_model import Reserva
from .reserva_model import ReservaIdNaoInteiro, ReservaIdMenorQueZero, ReservaNaoEncontrada, listar_reservas, reserva_por_id, criar_reserva
from database import db
import requests

schoolSystem = 'http://127.0.0.1:5003'
reservas = Blueprint("reservas", __name__)


def validar_turma(turma_id):
    resp = requests.get(f"{schoolSystem}/turmas/{turma_id}")
    return resp.status_code == 200

@reservas.route("/reservas", methods=["POST"])
def create_reserva():
    reserva = request.json
    turma_id = reserva.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    nova_reserva_criada = criar_reserva(reserva)

    return jsonify({'mensagem':'Reserva Criada com Sucesso'}), 201

@reservas.route("/reservas", methods=["GET"])
def get_reservas():
    return jsonify(listar_reservas())

@reservas.route("/reservas/<id>", methods=["GET"])
def reservasPorId(id):
    try:
        reserva = reserva_por_id(id)
        return jsonify(reserva)
    except ReservaIdNaoInteiro:
        return jsonify({'mensagem': 'Id de reserva precisa ser um numero inteiro'}), 400
    except ReservaIdMenorQueZero:
        return jsonify({'mensagem': 'Id de reserva precisa ser um numero maior que zero'}), 400
    except ReservaNaoEncontrada:
        return jsonify({'mensagem': 'Reserva de sala nao encontrada, por favor, insira um id existente'}), 404


