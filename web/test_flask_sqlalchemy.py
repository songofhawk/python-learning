import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_demo import create_app

app = Flask(__name__)


def main():
    app = create_app()
    with app.app_context():
        db = SQLAlchemy()
        db.init_app(app)
        session = db.session()
        cursor = session.execute('select * from user limit 10').cursor
        # result = cursor.fetchall()
        # print(result)

        # engine = db.engine
        # conn = engine.raw_connection()
        # cursor = conn.cursor()
        # cursor.execute('select * from user limit 10')
        result = cursor.fetchmany(2)
        print(result)
        result = cursor.fetchmany(2)
        print(result)
        result = cursor.fetchone()
        print(result)
        result = cursor.fetchall()
        print(result)


        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('select * from user limit 2')
        # result = cursor.fetchall()
        # print(result)
        # cursor.close()


if __name__ == '__main__':
    main()
