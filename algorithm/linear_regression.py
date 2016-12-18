from __future__ import print_function, division

from pyspark.sql import SparkSession
from pyspark.ml.regression import GeneralizedLinearRegression

import csv


def linear_regression(ticker):
    spark = SparkSession \
        .builder \
        .appName("GeneralizedLinearRegressionExample") \
        .getOrCreate()
    # Load training data
    dataset = spark.read.format("libsvm").load("../data/lr/" + ticker + "_no_today.csv")
    glr = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=10, regParam=0.3)

    # Fit the model
    model = glr.fit(dataset)

    # predict
    today_close_value = 0
    yesterday_close_value = 0
    with open("../data/lr/" + ticker + ".csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in reader:
            if count is 0:
                today_close_value = row[0]
                count += 1
            elif count is 1:
                yesterday_close_value = row[0]
                break

    # print(today_close_value)
    # print(yesterday_close_value)

    predict_close_value = -1 * float(str(model.coefficients[0])) + float(str(model.intercept))
    # print(predict_close_value)
    spark.stop()
    if predict_close_value >= today_close_value >= yesterday_close_value:
        return True
    elif predict_close_value <= today_close_value <= yesterday_close_value:
        return True
    elif yesterday_close_value <= predict_close_value <= today_close_value:
        return True
    else:
        return False


def get_accuracy():
    true_positive = 0
    total = 0
    f = open('result_lr.csv', 'w')
    with open('../data/ticker_list.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            print(row[0])
            total += 1
            flag = linear_regression(row[0])
            if flag is True:
                true_positive += 1
                f.write(row[0] + '\n')
    print(true_positive / total)
    f.close()
    return true_positive / total


if __name__ == '__main__':
    linear_regression("AAPL")
    # get_accuracy()