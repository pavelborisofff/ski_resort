from db import db
from resort_item import ResortItem
import enum


class StatusEnum(enum.Enum):
    open = 'O'
    paused = 'P'
    closed = 'C'
    out_of_order = 'OO'


class DifficultEnum(enum.Enum):
    green = 'G'
    blue = 'B'
    red = 'R'
    black = 'B'


class KindEnum(enum.Enum):
    park = 'PARK'
    tc = 'TC'
    tk = 'TK'
    tr = 'TR'
    ts = 'TS'
    tsd = 'TSD'


class ItemModel(ResortItem):
    __abstract__ = True

    status = db.Column(db.Enum(StatusEnum),
                       default=StatusEnum.out_of_order,
                       nullable=False)

    def __init__(self, name, status):
        super().__init__(name)
        self.name = name
        self.status = status

    def json(self):
        return {'name': self.name, 'status': self.status}


class SlopeModel(ItemModel):
    __tablename__ = 'slopes'

    difficult = db.Column(db.Enum(DifficultEnum),
                          default=DifficultEnum.green,
                          nullable=False)
    length = db.Column(db.Integer)
    night = db.Column(db.Boolean, default=False)
    night_time = db.Column(db.ARRAY(db.String(5)))

    def __init__(self, name, status, length, difficult, night: bool = False, night_time: list = None):
        super().__init__(name, status)
        self.name = name
        self.status = status
        self.length = length
        self.difficult = difficult
        self.night = night
        self.night_time = night_time or ('00:00', '23:59')

    def json(self):
        return ItemModel.json(self).update({'length': self.length, 'difficult': self.difficult})


class LiftModel(ItemModel):
    __tablename__ = 'lifts'

    type = db.Column(db.Enum(KindEnum),
                     default=KindEnum.tc)
    length = db.Column(db.Integer)
    open_from = db.Column(db.String(5))
    last_rise = db.Column(db.ARRAY(db.String(5)))
    down_before = db.Column(db.String(5))

    def __init__(self, name, status, length, open_from, last_rise, down_before):
        super().__init__(name, status)
        self.name = name
        self.status = status
        self.length = length
        self.open_from = open_from
        self.last_rise = last_rise
        self.down_before = down_before

    def json(self):
        return ItemModel.json(self).update({'length': self.length, 'open_from': self.open_from,
                                            'last_rise': self.last_rise, 'down_before': self.down_before})


class ActModel(ItemModel):
    __tablename__ = 'acts'

    open_from = db.Column(db.String(5))
    open_till = db.Column(db.String(5))
    icon = db.Column(db.String(100))

    def __init__(self, name, status, open_from, open_till, icon):
        super().__init__(name, status)
        self.name = name
        self.status = status
        self.open_from = open_from
        self.open_till = open_till
        self.icon = icon

