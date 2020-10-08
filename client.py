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

print(
    re.get(
        url="http://127.0.0.1:9000/history/all"
    ).content.decode()
)

print(
    re.post(
        url="http://127.0.0.1:9000/history/create",
        json={
            "BOARDID": "ABC",
            "TRADEDATE": "2020-04-15",
            "SHORTNAME": "Рога-и-копыта",
            "SECID": "JPA",
            "NUMTRADES": 1.0,
            "VALUE": 2.0,
            "OPEN": 3.0,
            "LOW": 4.0,
            "HIGH": 5.0,
            "LEGALCLOSEPRICE": 6.0,
            "WAPRICE": 7.0,
            "CLOSE": 8.0,
            "VOLUME": 9.0,
            "MARKETPRICE2": 10.0,
            "MARKETPRICE3": 11.0,
            "ADMITTEDQUOTE": 12.5,
            "MP2VALTRD": 13.0,
            "MARKETPRICE3TRADESVALUE": 14.0,
            "ADMITTEDVALUE": 15.0
        }
    ).content.decode()
)

print(
    re.get(
        url="http://127.0.0.1:9000/securities/all"
    ).content.decode()
)

print(
    re.post(
        url="http://127.0.0.1:9000/securities/create",
        json={
            "secid": "NEW111",
            "shortname": "Акрон",
            "regnumber": "1-03-00207-A",
            "name": "Акрон ПАО ао",
            "isin": "RU0009028674",
            "is_traded": 1,
            "emitent_id": 1418,
            "emitent_title": "Публичное акционерное общество \"Акрон\"",
            "emitent_inn": "5321029508",
            "emitent_okpo": "00203789",
            "gosreg": "1-03-00207-A",
            "type": "common_share",
            "group": "stock_shares",
            "primary_boardid": "TQBR",
            "marketprice_boardid": "TQBR"
    }
    ).content.decode()
)

print(
    re.post(
        url="http://127.0.0.1:9000/securities/create",
        json={
                "secid": "UNIQUEQ_ID",
                "name": "__BAD_NAME__"
            }
    ).content.decode()
)

print(
    re.post(
        url="http://127.0.0.1:9000/securities/update",
        json={
                "id": 2700,
                "regnumber": "1976-94172492",
                "name": "УК Рога и копыта",
            }
    ).content.decode()
)

print(
    re.post(
        url="http://127.0.0.1:9000/securities/delete",
        json={
                "secid": "NEW1111111",
            }
    ).content.decode()
)
