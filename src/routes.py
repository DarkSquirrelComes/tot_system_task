import json
import asyncio

from typing import Awaitable, Callable

from aiohttp import web

from db_engine import (
    fetch_all_history,
    insert_into_history,
    fetch_all_securities,
    insert_into_securities,
    delete_from_securities,
    update_in_securities,
    fetch_filtered_securities
)


router = web.RouteTableDef()


#-------------------ROOT---------------------

@router.get("/")
async def root(request: web.Request) -> web.Response:
    return web.Response(text="Hello world!")


#-------------------HISORY-------------------

@router.get("/history/all")
async def history_all(request: web.Request) -> web.Response:
    res = await fetch_all_history()
    return web.json_response(
        res,
        dumps=lambda data: json.dumps(data, ensure_ascii=False, indent=4)
    )

@router.post("/history/create")
async def history_create(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await insert_into_history(json_from_request)
    return web.json_response({"status": "success"})


#-------------------DECORATORS-----------------

ALLOWED_NAME_SYMBOLS = [chr(i) for i in range(ord('а'), ord('я') + 1)] +\
    [chr(i) for i in range(ord('А'), ord('Я') + 1)] +\
    [chr(i) for i in range(ord('0'), ord('9') + 1)] + [' ']

def handle_incorrect_name(
        func: Callable[[web.Request], Awaitable[web.Response]]
    ) -> Callable[[web.Request], Awaitable[web.Response]]:
    async def handler(request: web.Request) -> web.Response:
        json_from_request = await request.json()

        if not "name" in json_from_request:
            return await func(request)
        elif all(map(
                lambda symbol: symbol in ALLOWED_NAME_SYMBOLS,
                json_from_request["name"]
        )):
            return await func(request)
        else:
            raise ValueError("Incorrect symbol in 'name'")

    return handler

def handle_json_error(
        func: Callable[[web.Request], Awaitable[web.Response]]
    ) -> Callable[[web.Request], Awaitable[web.Response]]:
    async def handler(request: web.Request) -> web.Response:
        try:
            return await func(request)
        except asyncio.CancelledError:
            raise
        except Exception as ex:
            return web.json_response(
                {"status": "failed", "reason": str(ex)}, status=400
            )

    return handler


#-------------------SECURITIES-----------------

@router.get("/securities/all")
async def securities_all(request: web.Request) -> web.Response:
    res = await fetch_all_securities()
    return web.json_response(
                res,
                dumps=lambda data: json.dumps(data, ensure_ascii=False, indent=4)
        )

@router.get("/securities/filtered")
async def securities_filtered(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    res = await fetch_filtered_securities(json_from_request)
    return web.json_response(
                res,
                dumps=lambda data: json.dumps(data, ensure_ascii=False, indent=4)
        )

@router.post("/securities/create")
@handle_incorrect_name
async def securities_create(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await insert_into_securities(json_from_request)
    return web.json_response({"status": "success"})

@router.post("/securities/update")
@handle_incorrect_name
async def securities_update(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await update_in_securities(json_from_request)
    return web.json_response({"status": "success"})

@router.post("/securities/delete")
async def securities_delete(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await delete_from_securities(json_from_request["secid"])
    return web.json_response({"status": "success"})
