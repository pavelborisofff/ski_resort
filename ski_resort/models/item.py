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


class TypeEnum(enum.Enum):
    park = 'PARK'
    tc = 'TC'
    tk = 'TK'
    tr = 'TR'
    ts = 'TS'
    tsd = 'TSD'


class ItemModel(ResortItem):
    # __tablename__ = 'items'
    __abstract__ = True

    status = db.Column(db.Enum(StatusEnum),
                       default=StatusEnum.out_of_order,
                       nullable=False)

    def __init__(self, name, status):
        super().__init__(name)
        self.name = name
        self.status = status


class SlopeModel(ItemModel):
    __tablename__ = 'slopes'

    difficult = db.Column(db.Enum(DifficultEnum),
                          default=DifficultEnum.green,
                          nullable=False)
    length = db.Column(db.Integer)

    def __init__(self, name, status, length, difficult):
        super().__init__(name, status)
        self.name = name
        self.status = status
        self.length = length
        self.difficult = difficult


class LiftModel(ItemModel):
    __tablename__ = 'lifts'

    type = db.Column(db.Enum(TypeEnum),
                     default=TypeEnum.tc)
    length = db.Column(db.Integer)
    open_from = db.Column(db.String(5))
    last_rise = db.Column(db.String(23))
    down_before = db.Column(db.String(5))

    def __init__(self, name, status, length, open_from, last_rise, down_before):
        super().__init__(name, status)
        self.name = name
        self.status = status
        self.length = length
        self.open_from = open_from
        self.last_rise = last_rise
        self.down_before = down_before


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

