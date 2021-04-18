"""The main driver of the application."""
from persistence.models import flask_server


if __name__ == "__main__":
    flask_server.run(debug=True, host='localhost', port='8080')
