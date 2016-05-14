#!/usr/bin/env python

def app(env, start_response):
    data = bytes(env['QUERY_STRING'].replace("&", "\n"), encoding="UTF-8")
    print(data)
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
 
