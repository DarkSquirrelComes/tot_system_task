from sqlalchemy import (
    Column, Integer, Float, MetaData, Table, Text)


metadata = MetaData()
securities = Table(
    'securities', metadata,
    Column('id', Integer, primary_key=True),
    Column('secid', Text),
    Column('shortname', Text),
    Column('regnumber', Text),
    Column('name', Text),
    Column('isin', Text),
    Column('is_traded', Integer),
    Column('emitent_id', Integer),
    Column('emitent_title', Text),
    Column('emitent_inn', Text),
    Column('emitent_okpo', Text),
    Column('gosreg', Text),
    Column('type', Text),
    Column('group', Text),
    Column('primary_boardid', Text),
    Column('marketprice_boardid', Text),
)

metadata = MetaData()
history = Table(
    'history', metadata,
    Column('BOARDID', Text),
    Column('TRADEDATE', Text),
    Column('SHORTNAME', Text),
    Column('SECID', Text),
    Column('NUMTRADES', Float),
    Column('VALUE', Float),
    Column('OPEN', Float),
    Column('LOW', Float),
    Column('HIGH', Float),
    Column('LEGALCLOSEPRICE', Float),
    Column('WAPRICE', Float),
    Column('WAPRICE', Float),
    Column('CLOSE', Float),
    Column('VOLUME', Float),
    Column('MARKETPRICE2', Float),
    Column('MARKETPRICE3', Float),
    Column('ADMITTEDQUOTE', Float),
    Column('MP2VALTRD', Float),
    Column('MARKETPRICE3TRADESVALUE', Float),
    Column('ADMITTEDVALUE', Float),
    Column('WAVAL', Float),
)
