from functools import wraps
from flask import jsonify, make_response
from .. import app


def docme(ctx):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if ctx.passthrough:
                return f(*args, **kwargs)
            (jsonify({'error': 'Not found'}), 404)
            return make_response(jsonify(ctx.current_rsp.content.to_json()),
                ctx.current_rsp.code)

        endpoint_path = ctx.blueprint.name + '.' + f.__name__
        app.doc.add_endpoint(ctx, endpoint_path)
        return decorated_function
    return decorator
