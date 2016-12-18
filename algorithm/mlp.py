from __future__ import print_function

from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

from pyspark.sql import SparkSession


def mlp(ticker):
    spark = SparkSession \
        .builder.appName("multilayer_perceptron_classification_example").getOrCreate()

    # Load training data
    data = spark.read.format("libsvm") \
        .load("../data/mlp/" + ticker + ".csv")
    # Split the data into train and test
    splits = data.randomSplit([0.6, 0.4], 1234)
    train = splits[0]
    test = splits[1]
    # specify layers for the neural network:
    # input layer of size 4 (features), two intermediate of size 5 and 4
    # and output of size 2 (classes)
    layers = [4, 100, 200, 2]
    # create the trainer and set its parameters
    trainer = MultilayerPerceptronClassifier(maxIter=1000, layers=layers, blockSize=64, seed=1234)
    # train the model
    model = trainer.fit(train)
    # compute accuracy on the test set
    result = model.transform(test)
    prediction_labels = result.select("prediction", "label")
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    print("Accuracy: " + str(evaluator.evaluate(prediction_labels)))

    spark.stop()


if __name__ == '__main__':
    mlp("AAPL")
