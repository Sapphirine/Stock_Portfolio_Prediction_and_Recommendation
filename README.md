# Stock Portfolio Prediction and Recommendation
## Project structure
### Main functions and folders

```
/algorithm/linear_regression.py: 
  perform Linear Regression classification and prediction 
  upon all ticker data daily. please check report for alrogithm detail
/algorithm/mlp.py: 
  perform Multilayer Perceptron.
/algorithm/result_lr.csv: 
  result of bullish tickers
/data/fetch.py: 
  utility functions for getting ticker info given date period, 
  returning ticker info, low price, high price, open price, close 
  price and adjusted close price
/data/industry/, /data/split_market.py: 
  splitted tickers for all industries performed by the latter function
/data/lr/, /data/linear_regression_transform.py: 
  ticker data preprocessed for Linear Regression 
  classification and prediction by latter function
/data/mlp/, /data/mlp_transform.py:
  ticker data preprocessed for MLP classification
  and prediction by latter function
/data/plot.py: 
  utility function for plotting pythong figures 
  for Spark Machine Learning result
/static/: 
  main static files for frontend rendering and logic
stock.py: 
  rest api using Flask
flaskr.db: 
  routine clean and init db sql file
db_util.py: 
  utility functions for connecting to sqlite db
market_util.py: 
  utility functions for inserting corresponding data to sqlite tables
csv_to_db.py: 
  utility functions for converting csv data to sqlite db rows
```

### Usage
User could search by tickers (must be S&P 500) currently and see whether it will be bullish or not. 
Also, user could check prediction result for same market stock. We use Linear Regression, Multi-variate
Linear Regression and Multilayer Perceptron (NN) for classification upon the stock ticker data daily.

