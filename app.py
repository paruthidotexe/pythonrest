from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

## html pages
@app.route("/")
def home():
    return "Start Page"

if __name__ == '__main__':
    app.run(debug=True, port=7777)


