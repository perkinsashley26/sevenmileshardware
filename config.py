"""Configures the Flask Object."""
import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object."""

    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
