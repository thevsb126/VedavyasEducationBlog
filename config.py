import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'we_have_a_city_to_burn'
