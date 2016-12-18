import csv


# run for once
def split_market():
    with open('sp500-components.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            industry = row[2]
            f = open('industry/' + industry + '.csv', 'a')
            ticker = row[0] + '\n'
            f.write(ticker)
            # get tickers
    f.close()


if __name__ == '__main__':
    split_market()
