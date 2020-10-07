import requests as re

print(
    re.get(
        url="http://127.0.0.1:9000/securities/filtered",
        json={
            "tradedate": "2020-04-15",
            "emitent_title": "Общество с ограниченной ответственностью Управляющая компания \"Надежное управление\"",
            "order_by": "tradedate"
        }
    ).content.decode()
)
