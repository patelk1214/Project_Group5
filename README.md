# Project_Group5: Ketomus Option Trading Application
Our project seeks to develop an option trading application that provides pricing and analytics for trading stock options.

## Scope
We have selected an initial group of 16 liquid stocks to analyze for 1 & 2 month call and put options.
The application retrieves current stock and option pricing quotes and applies Black-Scholes model to derive option analytics.
The output displays an 'option chain' with analytics visualizations in a panel dashboard with user selection of stock and option term by dropdown.

## Finding relevant data 
The application requires current and historical data for stocks, options and interest rates.
After evaluating APIs incl. Alpaca, Quandl, and Alphavantage we found that IEX Cloud API offers a one stop solution for all relevant market data.
Free IEX subscription plan restricts data type and volume available via API, hence we subscribed for a paid service for expanded access.
Our paid subscription is still subject to monthly API caps of 5 million 'data credits.' 
To manage our API request volume we used csv files for ‘data warehousing.'

## Using IEX data
We retrieved the following data:
- COB option prices
- COB stock quotes
- 1yr historical stock data to compute historical volatility
- COB Treasury yield curve

The IEX API requests return JSON format dictionaries which where necessary we converted into datatypes suitable for further analysis.
Retrieving current option prices requires 2 API requests for each ticker: a first to obtain option maturities and a second to obtain the option quote across strike prices for each maturity.
Issues with the raw API data: number of data fields (34), call and put records mixed together, unordered strike prices.
To facilitate analysis we created 1 aggregate dataframe across tickers, option types, and maturities.
To create the ‘option chain’ for each ticker we separated call and put records, re-ordered by strike price, then data sliced by data field and number of strike prices. 
Lastly we appended option analytics to option chain.
Final option chain data fields (per ticker/expiry date): ‘side’, ‘bid’, ‘ask’, ‘strike price’, ‘volume’, ‘open interest’, 'Implied Volatilty', 'delta', 'vega'

## Coding: Option Analytics, Black-Scholes Model & Dashboard


## Visualization 




## Implications & Future Steps

