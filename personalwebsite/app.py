import os

from chalice import Chalice
from jinja2 import Template
import logging

from config import template_directory

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Chalice(app_name='personalwebsite')


@app.route('/')
def index():
    template_file = next(
        file for file in template_directory.iterdir() if 'index.html' == file.name.lower()
    )

    return Template(template_file.read_text()).render(
        cloudfront_url=os.getenv('cloudfront_url'),
        login_url='login',
        logout_url='logout',
        email_me_url='email-me',
        custom_message=None
    )
