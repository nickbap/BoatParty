import os


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'I_Solemnly_Swear_Im_Up_To_No_Good'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'sqlite:///boat_party.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
