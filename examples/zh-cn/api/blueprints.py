from .. import app
from .captcha import captcha_api
from .sms import sms_api

# Register API buleprint

app.register_blueprint(captcha_api)

app.register_blueprint(sms_api)
