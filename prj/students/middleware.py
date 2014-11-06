# -*- coding: utf-8 -*-
from django.db import connection


class QueryCountMiddleware(object):
    '''
    Промежуточный слой, который количество запросов и время их выполнения.
    '''

    def process_response(self, request, response):
        time = 0.0

        # Перебираем в цикле значения 'time' запросов...
        for v in [float(q['time']) for q in connection.queries]:
            # ...и прибавляем значения к переменной time
            time += v

        # Вставляем запросы в время их выполнения перед
        # закрывающим тего body
        response.content = response.content[:-15] + \
            '<p id="middleware">Queries: %s; Time: %s</p>' % \
            (len(connection.queries), time) + response.content[-16:]

        return response
