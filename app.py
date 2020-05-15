# from models import CINEMAS, API_KEYS, MOVIES, CINEMA_MOVIE, SHOW_TIMES, BOOKINGS
from functools import wraps
import logging
from flask import Flask, jsonify, request
app = Flask(__name__)

API_KEYS = [
    {
        'name': 'Momo00000000',
        'value': '2d4278333671cd4b6b06a74742ebbca12'
    }
]
CINEMAS = [
    {
        'id': 1,
        'name': 'CGV HCM'
    },
    {
        'id': 2,
        'name': 'CGV HN'
    },
    {
        'id': 3,
        'name': 'CGV DN'
    },
    {
        'id': 4,
        'name': 'CGV BH'
    }
]

MOVIES = [
    {
        'id': 1,
        'name': 'Ironman 1',
    },
    {
        'id': 2,
        'name': 'Avenger: End Game'
    },
    {
        'id': 3,
        'name': 'Thor: Ragnarok'
    },
    {
        'id': 4,
        'name': 'Doctor Strange'
    }
]

CINEMA_MOVIE = [
    {
        'cinema_id': 1,
        'movie_id': 1,
    },
    {
        'cinema_id': 1,
        'movie_id': 2,
    },
    {
        'cinema_id': 3,
        'movie_id': 3,
    },
    {
        'cinema_id': 4,
        'movie_id': 4,
    },
]

SHOW_TIMES = [
    {
        'id': 1,
        'datetime': '2020-04-16 8:00:00',
        'cinema_number': 1,
        'movie_id': 2,
        'cinema_id': 1
    },
    {
        'id': 2,
        'datetime': '2020-04-16 8:00:00',
        'cinema_number': 2,
        'movie_id': 3,
        'cinema_id': 1
    },
    {
        'id': 3,
        'datetime': '2020-04-16 19:00:00',
        'cinema_number': 2,
        'movie_id': 2,
        'cinema_id': 2
    },
    {
        'id': 4,
        'datetime': '2020-04-16 18:00:00',
        'cinema_number': 3,
        'movie_id': 4,
        'cinema_id': 3
    },
    {
        'id': 5,
        'datetime': '2020-04-16 22:00:00',
        'cinema_number': 4,
        'movie_id': 3,
        'cinema_id': 4
    }
]

BOOKINGS = [
    {
        'id': 1,
        'showtime_id': 1,
        'sheet_number': 1,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 2,
        'showtime_id': 1,
        'sheet_number': 2,
        'booked': True,
        'amount': 100000
    },
    {
        'id': 3,
        'showtime_id': 1,
        'sheet_number': 3,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 4,
        'showtime_id': 1,
        'sheet_number': 4,
        'booked': True,
        'amount': 100000
    },
    {
        'id': 5,
        'showtime_id': 1,
        'sheet_number': 5,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 6,
        'showtime_id': 2,
        'sheet_number': 6,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 7,
        'showtime_id': 2,
        'sheet_number': 7,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 8,
        'showtime_id': 2,
        'sheet_number': 8,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 9,
        'showtime_id': 2,
        'sheet_number': 9,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 10,
        'showtime_id': 2,
        'sheet_number': 10,
        'booked': False,
        'amount': 100000
    },
    {
        'id': 11,
        'showtime_id': 2,
        'sheet_number': 10,
        'booked': False,
        'amount': 100000
    },
]


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('api_key', '')
        valid_key = api_key and any(api_key in key['value'] for key in API_KEYS) or False
        if valid_key:
            return view_function(*args, **kwargs)
        else:
            message = 'Error! Unauthorized. Invalid Api Key!'
            logging.warning(message)
            return jsonify({
                'message': message
            }), 401
    return decorated_function


def get_data(datas, id=None, field=None, value=None):
    if id:
        res = [rec for rec in datas if rec['id'] == id]
        if not res:
            message = 'Warning: Resource not found!'
            logging.warning(message)
            return {'message': message}
    elif field and value:
        if isinstance(value, int):
            res = [rec for rec in datas if value == rec.get(field)]
        else:
            res = [rec for rec in datas if value in rec.get(field)]
    else:
        res = datas
    return res


@app.route('/')
def hello():
    return '<h1>Well come to Flask API</h1>'


@app.route('/api/cinema', methods=['GET'])
@app.route('/api/cinema/<int:id>', methods=['GET'])
@app.route('/api/cinema/name/<name>', methods=['GET'])
@require_appkey
def get_cinema(id=None, name=None):
    if id:
        response = get_data(CINEMAS, id)
    elif name:
        response = get_data(CINEMAS, field='name', value=name)
    else:
        response = get_data(CINEMAS)
    return jsonify(response), 200


@app.route('/api/movie', methods=['GET'])
@app.route('/api/movie/<int:id>', methods=['GET'])
@app.route('/api/movie/name/<name>', methods=['GET'])
@app.route('/api/movie/cinema/<int:cinema_id>', methods=['GET'])
@require_appkey
def get_movie(id=None, name=None, cinema_id=None):
    if id:
        response = get_data(MOVIES, id)
    elif name:
        response = get_data(MOVIES, field='name', value=name)
    elif cinema_id:
        movie_ids = [cm['movie_id'] for cm in CINEMA_MOVIE if cm['cinema_id'] == cinema_id]
        response = [m for m in MOVIES if m['id'] in movie_ids]
    else:
        response = get_data(MOVIES)
    return jsonify(response), 200


@app.route('/api/showtime/movie/<int:movie_id>', methods=['GET'])
@app.route('/api/showtime/cinema/<int:cinema_id>', methods=['GET'])
@app.route('/api/showtime/<int:cinema_id>/<int:movie_id>', methods=['GET'])
@require_appkey
def get_showtimes(movie_id=None, cinema_id=None):
    datas = SHOW_TIMES
    if cinema_id:
        datas = get_data(datas, field='cinema_id', value=cinema_id)
    if movie_id:
        datas = get_data(datas, field='movie_id', value=movie_id)
    return jsonify(datas), 200


@app.route('/api/sheets/<int:showtime_id>', methods=['GET'])
@require_appkey
def get_sheets(showtime_id):
    datas = BOOKINGS
    datas = get_data(datas, field='showtime_id', value=showtime_id)
    return jsonify([
        {
            'id': data['id'],
            'numer': data['sheet_number'],
            'booked': data['booked'],
            'amount': data['amount']}
        for data in datas
    ]), 200


@app.route('/api/sheet/booking', methods=['POST', 'PUT'])
@require_appkey
def post_book_sheet():
    kw = request.args
    sheet_id = kw.get('sheet_id', '0')
    book = kw.get('book')
    book = book and book in ['True', 'true'] and True or False
    datas = [rec for rec in BOOKINGS if rec['id'] == int(sheet_id)]
    sheet_value = datas and datas[0] or {}
    if not sheet_value:
        message = 'Error: Sheet %s does not exists!' % sheet_id
        logging.error(message)
        return jsonify({
                'message': message
            }), 404
    else:
        if sheet_value['booked'] and book:
            # Sheet has already book but request to book a gain
            message = 'Not Acceptable: Sheet %s has already booked!' % sheet_id
            logging.error(message)
            return jsonify({'message': message}), 400
        elif not sheet_value['booked'] and not book:
            message = 'Not Acceptable: Sheet %s has already cancelled!' % sheet_id
            logging.error(message)
            return jsonify({'message': message}), 400
        else:
            sheet_value.update({'booked': book})
    return jsonify({
        'message': 'Booked Successfully!'
    }), 200


if __name__ == '__main__':
    # https://stackoverflow.com/questions/26423984/unable-to-connect-to-flask-app-on-docker-from-host
    app.run(host="0.0.0.0", debug=True)
