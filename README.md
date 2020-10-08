## End-points и примеры запросов/ответов:

<details><summary>GET /history/all</summary>
  
```json
{
    "status": "success",
    "data": [
        {
            "BOARDID": "TQBR",
            "TRADEDATE": "2020-04-15",
            "SHORTNAME": "АбрауДюрсо",
            "SECID": "ABRD",
            "NUMTRADES": 171.0,
            "VALUE": 734875.0,
            "OPEN": 135.5,
            "LOW": 133.5,
            "HIGH": 136.5,
            "LEGALCLOSEPRICE": 134.5,
            "WAPRICE": 135.0,
            "CLOSE": 134.5,
            "VOLUME": 5440.0,
            "MARKETPRICE2": 135.0,
            "MARKETPRICE3": 135.0,
            "ADMITTEDQUOTE": 134.5,
            "MP2VALTRD": 734875.0,
            "MARKETPRICE3TRADESVALUE": 734875.0,
            "ADMITTEDVALUE": 734875.0,
            "WAVAL": null
        },
        {
            "BOARDID": "TQDE",
            "TRADEDATE": "2020-04-15",
            "SHORTNAME": "АСКО ао",
            "SECID": "ACKO",
            "NUMTRADES": 148.0,
            "VALUE": 497102.0,
            "OPEN": 4.04,
            "LOW": 3.94,
            "HIGH": 4.24,
            "LEGALCLOSEPRICE": 4.0,
            "WAPRICE": 4.08,
            "CLOSE": 4.02,
            "VOLUME": 121700.0,
            "MARKETPRICE2": null,
            "MARKETPRICE3": 4.08,
            "ADMITTEDQUOTE": 4.0,
            "MP2VALTRD": 0.0,
            "MARKETPRICE3TRADESVALUE": 501202.0,
            "ADMITTEDVALUE": 0.0,
            "WAVAL": null
        }
    ]
}
```
</details>

<details><summary>POST history/create</summary>
request:
  
```json
{
    "BOARDID": "ABC",
    "TRADEDATE": "2020-04-15",
    "SHORTNAME": "Рога-и-копыта",
    "SECID": "ABRD",
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
```

response (secid already exists):

```json
{
    "status": "success"
}

```

response (no such secid):

```json
{
    "status": "failed",
    "reason": "No such secid"
}

```

</details>

<details><summary>GET /securities/all</summary>
response:

```json
[
    {
        "id": 2699,
        "secid": "AFKS",
        "shortname": "Система ао",
        "regnumber": "1-05-01669-A",
        "name": "АФК \"Система\" ПАО ао",
        "isin": "RU000A0DQZE3",
        "is_traded": 1,
        "emitent_id": 2046,
        "emitent_title": "ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО \"АКЦИОНЕРНАЯ ФИНАНСОВАЯ КОРПОРАЦИЯ \"СИСТЕМА\"",
        "emitent_inn": "7703104630",
        "emitent_okpo": "27987276",
        "gosreg": "1-05-01669-A",
        "type": "common_share",
        "group": "stock_shares",
        "primary_boardid": "TQBR",
        "marketprice_boardid": "TQBR"
    },
    {
        "id": 2700,
        "secid": "AFLT",
        "shortname": "Аэрофлот",
        "regnumber": "1-01-00010-A",
        "name": "Аэрофлот-росс.авиалин(ПАО)ао",
        "isin": "RU0009062285",
        "is_traded": 1,
        "emitent_id": 1300,
        "emitent_title": "Публичное акционерное общество \"Аэрофлот – российские авиалинии\"",
        "emitent_inn": "7712040126",
        "emitent_okpo": "29063984",
        "gosreg": "1-01-00010-A",
        "type": "common_share",
        "group": "stock_shares",
        "primary_boardid": "TQBR",
        "marketprice_boardid": "TQBR"
    }
]
```

</details>


<details><summary>GET /securities/filtered</summary>
request (here can be subset of this fields):
  
```json
{
    "tradedate": "2020-04-15",
    "emitent_title": "Общество с ограниченной ответственностью Управляющая компания \"Надежное управление\"",
    "order_by": "tradedate"
}
```
  
response:

```json
{
    "status": "success",
    "data": [
        {
            "secid": "RU000A0JT8U8",
            "regnumber": "1976-94172492",
            "name": "УК Надеж.управ.ЗПИФУралНедв1",
            "emitent_title": "Общество с ограниченной ответственностью Управляющая компания \"Надежное управление\"",
            "tradedate": "2020-04-15",
            "numtrades": 0.0,
            "open": null,
            "close": null
        }
    ]
}

```

</details>

<details><summary>POST /securities/create</summary>

request:

```json
{
    "secid": "AKRN",
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

```

response can be:

```json
{
    "status": "failed",
    "reason": "'secid' already exists"
}

```

response can be:

```json
{
    "status": "success"
}

```
___

request:
```json
{
    "secid": "UNIQUEQ_ID",
    "name": "__BAD_NAME__"
}

```

response:

```json
{
    "status": "failed",
    "reason": "incorrect symbol in 'name'"
}

```


</details>

<details><summary>POST /securities/update</summary>

___

request:

```json
{
    "secid": "123",
    "regnumber": "1976-94172492",
    "name": "УК НадежуправЗПИФУралНедв",
    "emitent_title": "Общество с ограниченной ответственностью Управляющая компания \"Надежное управление\"",
    "tradedate": "2020-04-15",
    "numtrades": 0.0
}

```

response:

```json
{
    "status": "failed",
    "reason": "'id' not specified"
}
```

___

request:

```json
{
    "id": 2700,
    "secid": "123",
    "regnumber": "1976-94172492",
    "name": "УК НадежуправЗПИФУралНедв",
    "emitent_title": "Общество с ограниченной ответственностью Управляющая компания \"Надежное управление\"",
    "tradedate": "2020-04-15",
    "numtrades": 0.0
}

```

response:

```json
{
    "status": "failed",
    "reason": "'secid' prohibited to change"
}
```

___

request:

```json
{
    "id": 2700,
    "name": "УК Рога-и-копыта"
}

```

response:

```json
{
    "status": "failed",
    "reason": "Incorrect symbol in 'name'"
}

```

___

request:

```json
{
    "id": 2700,
    "name": "УК Рога и копыта"
}

```

response:

```json
{
    "status": "success"
}

```

</details>

<details><summary>POST /securities/delete</summary>

request:

```json
{
    "secid": "NEW1111111",
}

```

response:

```json
{
    "status": "success"
}
```

</details>
