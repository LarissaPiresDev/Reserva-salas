from config import db

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    hora_inicio = db.Column(db.String(10), nullable=False)
    hora_fim = db.Column(db.String(10), nullable=False)

    def __init__(self, turma_id, sala, data, hora_inicio, hora_fim):
        self.turma_id = turma_id
        self.sala = sala
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim

    def to_dict(self):
        return {'id': self.id, 'turma_id': self.turma_id, 
                'sala': self.sala, 'data': self.data, 
                'hora_inicio': self.hora_inicio, 'hora_fim': self.hora_fim}

class ReservaIdNaoInteiro(Exception):
    pass

class ReservaIdMenorQueZero(Exception):
    pass

class ReservaNaoEncontrada(Exception):
    pass

class TurmaJaReservada(Exception):
    pass


def listar_reservas():
    reservas = Reserva.query.all()
    return [reserva.to_dict() for reserva in reservas]

def reserva_por_id(id):
    try:
        id = int(id)
    except ValueError:
        raise ReservaIdNaoInteiro
    if id <=0:
        raise ReservaIdMenorQueZero

    reserva = Reserva.query.get(id)
    if not reserva:
        raise ReservaNaoEncontrada
    return reserva.to_dict()

def criar_reserva(nova_reserva):
    new_reserva = Reserva(
        turma_id=int(nova_reserva['turma_id']),
        sala=str(nova_reserva['sala']),
        data=str(nova_reserva['data']),
        hora_inicio=str(nova_reserva['hora_inicio']),
        hora_fim=str(nova_reserva['hora_fim'])
    )

    db.session.add(new_reserva)
    db.session.commit()
    return new_reserva.to_dict()


def verificar_turma_reservada(turma_id, data):
    reserva_existente = Reserva.query.filter_by(turma_id=turma_id, data=data).first()
    if reserva_existente:
        raise TurmaJaReservada
