#!/usr/bin/python
# -*- coding: utf-8 -*-

from api import app

if __name__ == "__main__":
    application = app.create_app()

    application.run(debug=True, host='0.0.0.0', port=int(8000))
