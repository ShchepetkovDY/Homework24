from flask import Blueprint, jsonify, request, Response
from marshmallow import ValidationError
from processing import get_resault
from model import RequestSchema
from typing import Union, Tuple

query_blueprint = Blueprint('main', __name__)

file_name = 'data/apache_logs.txt'


@query_blueprint.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
    """
    Представление, получающее и обрабатывающее POST запрос, в котором передаются словарь парных параметров:
    cmd1: str, value1: str -  параметры поиска
    cmd2: str, value2: str - параметры сортировки
    filename: str - файл, по которому осуществляется поиск
    """

    data = request.json
    try:
        check_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    cmd = check_data.get('cmd1')
    value = check_data.get('value1')
    filename = check_data.get('filename')
    data = get_resault(cmd, value, filename, None)

    cmd = check_data.get('cmd2')
    value = check_data.get('value2')
    filename = check_data.get('filename')
    result = get_resault(cmd, value, filename, data)

    return jsonify(result)
