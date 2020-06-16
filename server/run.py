#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import connexion
from flask_cors import CORS
from logbook import Logger
from flask import request




if __name__ == '__main__':

    log = Logger('dx-captain')
    log.info("database mapping generating")
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='specs/')
    # CORS(app.app)
    app.add_api('api.yaml', arguments={'title': 'api'})
    log.info("api.yaml loaded!")
    log.info("error handler added")

    @app.app.before_request
    def before():
        log.trace('>'*40)
        len_data = 0
        data = connexion.request.data
        if data:
            len_data = len(connexion.request.data)
            if len_data > 256:
                data = data[:256]
        info = "BEFORE> {} {} -> {} {}:{}".format(connexion.request.remote_addr,
                                                  connexion.request.method,
                                                  connexion.request.full_path,
                                                  len_data,
                                                  data)
        log.trace(info)

    @app.app.after_request
    def after(response):
            response.direct_passthrough = False
            len_data = 0
            data = response.data
            if data:
                len_data = len(response.data)
                if len_data > 256:
                    data = data[:256]
            info = "AFTER> {} {} -> {} {}:{}".format(request.remote_addr,
                                                     request.method, request.full_path, len_data, data)
            log.trace(info)
            log.trace('<'*40)
            return response
    app.run(host='0.0.0.0', port=8998, debug=True)
