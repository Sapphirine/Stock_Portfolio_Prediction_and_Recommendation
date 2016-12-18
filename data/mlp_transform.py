import csv

from dateutil.parser import parse

dir_path = "mlp/"


def transform(ticker):
    with open('tickers/' + ticker + '.csv') as csvfile:
        # skip first row
        next(csvfile, None)
        f = open(dir_path + ticker + '.csv', 'w')
        reader = csv.reader(csvfile, delimiter=',')

        prev_close = None
        for row in reader:
            open_price = row[1]
            high_price = row[2]
            low_price = row[3]
            close_price = row[4]
            if prev_close is None:
                prev_close = close_price
                continue
            new_row = ""
            # open, low, high, close
            if prev_close > close_price:
                new_row += "1"
            else:
                new_row += "0"
            new_row += " 1:" + open_price + " 2:" + high_price + " 3:" + low_price + " 4:" + close_price + ' \n'
            # print(new_row)
            prev_close = close_price
            f.write(new_row)

    f.close()


def transform_all():
    with open('../data/ticker_list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            ticker = row[0]
            # print(ticker)
            transform(ticker)


if __name__ == '__main__':
    transform_all()
