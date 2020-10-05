from pathlib import Path
from typing import Dict, List, Tuple

from sqlalchemy.schema import CreateTable
from sqlalchemy import Integer, create_engine, select

from sqlalchemy_aio import ASYNCIO_STRATEGY

from xml_parse import history_rows, security_rows

from db_schemas import history, securities


# -------------------ENGINE---------------------

def get_db_path() -> Path:
    here = Path.cwd()
    return here / "test.db"


sqlite_db = get_db_path()
engine = create_engine("sqlite:///test.db", strategy=ASYNCIO_STRATEGY)


async def try_make_db() -> None:
    if sqlite_db.exists():
        return

    await engine.execute(CreateTable(history))
    await engine.execute(CreateTable(securities))

    conn = await engine.connect()

    for history_row in history_rows:
        for key in history_row:
            if not history_row[key]:
                history_row[key] = None
        await conn.execute(history.insert().values(**history_row))

    for security_row in security_rows:
        for key in security_row:
            if not security_row[key]:
                security_row[key] = None
        await conn.execute(securities.insert().values(**security_row))

    await conn.close()


# -------------------HISTORY---------------------

async def fetch_all_history() -> List[Tuple]:
    conn = await engine.connect()
    result = await conn.execute(select([history]))
    rows = await result.fetchall()
    await conn.close()

    keys = [c.key for c in history.columns]
    return list(map(
        lambda row: dict(zip(keys, row)),
        rows
    ))


async def insert_into_history(row: Dict) -> None:
    conn = await engine.connect()
    await conn.execute(history.insert().values(**row))
    await conn.close()


# -------------------SECURITIES---------------------

async def fetch_all_securities() -> List[Tuple]:
    conn = await engine.connect()
    result = await conn.execute(select([securities]))
    rows = await result.fetchall()
    await conn.close()

    keys = [c.key for c in securities.columns]
    return list(map(
        lambda row: dict(zip(keys, row)),
        rows
    ))


async def insert_into_securities(row: Dict) -> None:
    conn = await engine.connect()
    await conn.execute(securities.insert().values(**row))
    await conn.close()


async def delete_from_securities(id_: Integer) -> None:
    conn = await engine.connect()
    await conn.execute(history.delete().where(history.c.SECID == id_))
    await conn.execute(securities.delete().where(securities.c.secid == id_))
    await conn.close()


async def update_in_securities(row: Dict) -> None:
    if "secid" in row:
        return "'secid' forbidden to change"
    conn = await engine.connect()
    await conn.execute(
        securities.update().
        where(securities.c.id == row["id"]).
        values(**row)
    )
    await conn.close()


async def fetch_filtered_securities(row: Dict) -> List[List[Tuple]]:
    order_by = row.get("order_by")
    filter_by = {}

    if "tradedate" in row:
        filter_by["history.TRADEDATE"] = row["tradedate"]

    if "emitent_title" in row:
        filter_by["securities.emitent_title"] = row["emitent_title"]

    conn = await engine.connect()

    request = f"""
        SELECT
            securities.secid as secid,
            securities.regnumber as regnumber,
            securities.name as name,
            securities.emitent_title as emitent_title,
            history.TRADEDATE as tradedate,
            history.NUMTRADES as numtrades,
            history.OPEN as open,
            history.CLOSE as close
        FROM history
        JOIN securities ON securities.secid=history.SECID
        {
            '' if not filter_by
            else 'WHERE ' + ' AND '.join(
                [f'{k}=={repr(filter_by[k])}' for k in filter_by]
            )
        }
        {
            f'ORDER BY {order_by}' if order_by else ''
        };"""

    result = await conn.execute(request)
    rows = await result.fetchall()

    await conn.close()

    keys = [
        "secid",
        "regnumber",
        "name",
        "emitent_title",
        "tradedate",
        "numtrades",
        "open",
        "close",
    ]
    return list(map(
        lambda row: dict(zip(keys, row)),
        rows
    ))
