from flask import jsonify

def register_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "error": "Bad request",
            "status": 400
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not found",
            "status": 404
        }), 404