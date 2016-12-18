import matplotlib
import matplotlib.pyplot as plt
import csv
import numpy as np

with open('AALonly61.csv') as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',')
    i = 0
    # date date close_price close price
    close_price = range(43)
    date = range(43)
    column_volume = range(43)
    for row in reader2:
        if i == 0:
            i += 1
        elif i > 0:
            column_volume[i - 1] = float(row[5])
            close_price[i - 1] = float(row[4])
            date[i - 1] = row[0][2:10]
            i += 1

    date.reverse()
    close_price.reverse()

    n = 0
    xx = range(43)
    for m in range(43):
        if n % 7 == 2:
            n += 2
            xx[m] = n
            n += 1
        else:
            xx[m] = n
            n += 1

    column3 = range(22)

    yy = range(0, 43, 2)
    i = 0
    for m in range(0, 43, 2):
        yy[i] = xx[m]
        column3[i] = date[m]

        i += 1

    new_x = np.array(xx)
    x = -new_x + 60
    new_y = np.array(close_price)
    coefficient = -0.163916667
    intercept = 48.34408959

    plt.figure(1)
    plt.scatter(xx, close_price, label='Close price')
    plt.plot(x, new_x * coefficient + intercept, 'r')
    plt.title('Close price of AAL in last two months')
    plt.xticks(yy, column3, fontsize=7, rotation=30)
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('close price($)')
    plt.savefig('AALcloseprice.png', format='png')
