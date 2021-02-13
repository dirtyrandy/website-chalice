import os
from pathlib import Path


template_directory = Path(os.path.abspath(os.path.dirname(__file__))).joinpath('web')
email_template_directory = Path(os.path.abspath(os.path.dirname(__file__))).joinpath('web', 'templates')
asset_directory = Path(os.path.abspath(os.path.dirname(__file__))).joinpath('web', 'assets')
images_directory = Path(os.path.abspath(os.path.dirname(__file__))).joinpath('web', 'images')
# client_secrets_path = Path(os.path.abspath(os.path.dirname(__file__))).joinpath('client_secrets.json')

email_sender = 'noreply@seecook.info'
requester_response_template = 'website_email_response.html'
