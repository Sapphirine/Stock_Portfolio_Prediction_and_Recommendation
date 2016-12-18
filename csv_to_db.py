import db_util
import market_util
import csv


def insert_lr(db):
    with open('algorithm/result_lr.csv') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            db.execute("INSERT INTO result_lr (id, ticker) VALUES (NULL,\'" + row[0] + '\');')
            db.commit()


def insert_market(db):
    with open('algorithm/result_lr.csv') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            market = market_util.get_market(row[0])
            market = market.replace(" ", "_")
            db.execute("INSERT INTO " + market + " (id, ticker) VALUES (NULL ,\'" + row[0] + '\');')
            db.commit()


if __name__ == '__main__':
    # run flaskr.db first
    with db_util.app.app_context():
        db = db_util.get_db()
        insert_lr(db)  # run once every day
        insert_market(db)  # run once forever
        db.close()
