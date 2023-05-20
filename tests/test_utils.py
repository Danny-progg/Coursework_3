import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert data, list


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data) == [{"id": 156456789,
                                             "date": "2019-08-04T23:15:05.206878",
                                             "operationAmount": {"amount": "4514.93",
                                                                 "currency": {"name": "USD",
                                                                              "code": "USD"}},
                                             "description": "Открытие вклада",
                                             "state": "EXECUTED",
                                             "to": "Счет 75651667383060284188"}]
    assert get_filtered_data(test_data, filter_empty_from=True) == []


def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x['date'] for x in data] == ["2019-08-04T23:15:05.206878", "2018-08-04T23:15:05.206878", "2017-08-04T23:15:05.206878"]


def test_get_formatted_data(test_data_two):
    data = get_formatted_data(test_data_two)
    assert data == ['26.08.2019 Перевод организации        \nMaestro 1596 83** **** 5199 -> Счет **9589        \n31957.58руб.']
