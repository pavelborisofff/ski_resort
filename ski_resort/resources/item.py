from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel, SlopeModel, LiftModel, ActModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='Name of Resort Item cannot be left blank'
    )
    parser.add_argument(
        'status',
        type=str,
        required=True,
        help='Status of Resort Item cannot be left blank'
    )

    @staticmethod
    @jwt_required()
    def get(name: str) -> (dict, int):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json(), 200
        return {'message': f"Item '{name}' not found"}, 404
