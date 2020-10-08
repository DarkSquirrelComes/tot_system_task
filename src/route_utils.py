from typing import Awaitable, Callable

import json

from aiohttp import web


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
            raise ValueError("incorrect symbol in 'name'")

    return handler

def handle_error(
        func: Callable[[web.Request], Awaitable[web.Response]]
    ) -> Callable[[web.Request], Awaitable[web.Response]]:
    async def handler(request: web.Request) -> web.Response:
        try:
            return await func(request)
        except Exception as ex:
            return web.json_response(
                {"status": "failed", "reason": str(ex)}, status=400,
                dumps=lambda data: json.dumps(data, ensure_ascii=False, indent=4)
            )

    return handler

def build_response(data=None):
    return web.json_response(
                {"status": "success", "data": data} if data else {"status": "success"},
                dumps=lambda data: json.dumps(data, ensure_ascii=False, indent=4)
        )
