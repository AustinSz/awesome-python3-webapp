# !user/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Austin'

'''
async web application.
'''

from aiohttp import web


async def index(request):
    return web.Response(text='Awesome', content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app, host='127.0.0.1', port=9000)