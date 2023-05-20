import pytest


@pytest.fixture
def test_data():
    return [{"id": 156456789,
             "date": "2019-08-04T23:15:05.206878",
             "operationAmount": {"amount": "4514.93",
                                 "currency": {"name": "USD",
                                              "code": "USD"}},
             "description": "Открытие вклада",
             "state": "EXECUTED",
             "to": "Счет 75651667383060284188"},
            {"id": 156456789,
             "date": "2018-08-04T23:15:05.206878",
             "operationAmount": {"amount": "4514.93",
                        "currency": {"name": "USD",
                                     "code": "USD"}},
             "description": "Перевод со счета на счет",
             "to": "Счет 75651667383060284188",
             "from": "Счет 19708645243227258542"},
            {"id": 156456789,
             "date": "2017-08-04T23:15:05.206878",
             "operationAmount": {"amount": "4514.93",
                                 "currency": {"name": "USD",
                                              "code": "USD"}},
             "description": "Открытие вклада",
             "to": "Счет 75651667383060284188"}]


@pytest.fixture
def test_data_two():
    return[
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
