import csv


def get_market(ticker):
    with open("./data/sp500-components.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == ticker:
                return row[2]
    return None


# def get_ticker_from_same_market(ticker):
#     market = get_market(ticker)
#     print(market)
#     with open('./data/industry/' + market + '.csv') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             print(row[0])


# if __name__ == '__main__':
#     get_ticker_from_same_market("AAPL")
