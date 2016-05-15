#!/usr/bin/env python

def app(env, start_response):
    data = env['QUERY_STRING'].replace("&", "\n")
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
 
