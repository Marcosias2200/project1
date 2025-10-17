from datetime import datetime

def filter_by_state(data, state='EXECUTED'):
    """ Фильтрует список транзакций по состоянию."""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, descending=True):
    """param1 (тип): Описание первого параметра.
    - param2 (тип): Описание второго параметра."""
    return sorted(
        data,
        key=lambda item: datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=descending
    )