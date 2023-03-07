from typing import Optional
from functions import filter_query, limit_query, map_query, sort_query, unique_query, regex_query
from typing import Iterable, Dict, List, Callable

QUERY_DICT: Dict[str, Callable] = {
    'filter': filter_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query,
    'regex': regex_query,
}


def read_file(file_name: str) -> Iterable[str]:
    with open(f'data/{file_name}') as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        new_data: Iterable[str] = read_file(file_name)
    else:
        new_data = data
    return list(QUERY_DICT[cmd](value=value, data=new_data))


def get_resault(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> Iterable[str]:
    """
    Функция, которая возвращает результат поиска, по заданным параметрам
    """
    return build_query(cmd, value, file_name, data)
