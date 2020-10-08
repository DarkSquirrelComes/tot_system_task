import json
import asyncio

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

from route_utils import handle_incorrect_name, handle_error, build_response


router = web.RouteTableDef()


#-------------------ROOT---------------------

@router.get("/")
@handle_error
async def root(request: web.Request) -> web.Response:
    return web.Response(text="Hello world!")


#-------------------HISORY-------------------

@router.get("/history/all")
@handle_error
async def history_all(request: web.Request) -> web.Response:
    res = await fetch_all_history()
    return build_response(res)

@router.post("/history/create")
@handle_error
async def history_create(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await insert_into_history(json_from_request)
    return build_response()


#-------------------SECURITIES-----------------

@router.get("/securities/all")
@handle_error
async def securities_all(request: web.Request) -> web.Response:
    res = await fetch_all_securities()
    return web.json_response(
                res,
                dumps=lambda data: json.dumps(data, ensure_ascii=False, indent=4)
        )

@router.get("/securities/filtered")
@handle_error
async def securities_filtered(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    res = await fetch_filtered_securities(json_from_request)
    return build_response(res)

@router.post("/securities/create")
@handle_error
@handle_incorrect_name
async def securities_create(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await insert_into_securities(json_from_request)
    return build_response()

@router.post("/securities/update")
@handle_error
@handle_incorrect_name
async def securities_update(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await update_in_securities(json_from_request)
    return build_response()

@router.post("/securities/delete")
@handle_error
async def securities_delete(request: web.Request) -> web.Response:
    json_from_request = await request.json()
    await delete_from_securities(json_from_request["secid"])
    return build_response()
