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

## Coding: Option Analytics (option_analytics_v2.ipynb), Black-Scholes Model (blackscholesmodel.py). 

o  We broke our code down to three integral parts (Black-Scholes, Options Analytics, and Dashboard). 

o We first retrieved End of the Day Option Prices from IEX Cloud for tickers in scope, one at a time and load the Options data into pandas data frame. The clean       up process for the data retrieved from IEX was one of the parts we spent a lot of time on. We also ran into data reliability issues and some data points experienced a lag in being updated in the IEX cloud.

o  The next step was to retrieve the COB Quotes and historical price data for each ticker in scope. This included the most recent closing price, market cap, 52 weeks high/low, PE Ratios and 1 year Historical Prices from IEX cloud which allowed us to calculate following:

       Daily return

       Rolling 30-day standard deviation

       The annualized standard deviation (historical volatility)

o The second step was to analyze different strike prices for each ticker in scope to find the closest strike price from the current strike price.

o  For this phase of our project, we chose to focus on options with 30-60 days to expiry and thus have retrieved Treasury rates from IEX for 1- and 3-month maturities.

o  We then loaded the Call & Put option data for different maturities into separate data frames and stored them in a dictionary for later use.

o  Our next step was to calculate Implied Volatility & Options Greeks for option chain one ticker at a time and update relevant ticker dataframe in the Option Data dictionary.

       To do this, we referred to the Black-Scholes Model and the Netwton-Raphson method for root solving. Note that: one issue we encountered here is that the Black Scholes model computes the price for European options while we are using American options.

       After computing the Implied Volatility, the next step was to calculate the Delta and Vega for each option strike and add them into the Option DF we had already created. 

       Our findings showed that Newton’s Method did not converge for some of the options, mostly away from the money, about 25 % and higher.

o  Once we calculated the Implied Vol and the Greeks, they are added into the data frame, all we had to do was concatenate the Put and Call data frames of each ticker into the final option data dictionary to later access for the dashboard and smiles.


## Visualization - (dashboard.ipynb)

o  Once we had everything loaded in the necessary data frames, it was time to move on to the visualization part. We did experience a few issues in creating the tables             (everything was jammed together, and it was impossible to read the table) and the graphs (some tickers were not showing in the drop down of the graphs and it took us a while to figure out the issue) initially, however, after thorough research we were able to successfully.

o  We created two different visualizations:

    	An option chain table with two tabs each representing the different maturities in our scope and a drop down for the user to select a ticker from the watchlist. When the User chooses a ticker teh plot will refresh to plot Volatility Smile for the chosen ticker. 

    	The option chain table showed the user all the different fields we extracted from IEX cloud and was separated by the type of option available (Call options on the left and Put options on the right)
    

## Implications & Future Steps

o  Broader stock selection for user

o	More option maturities

o	Additional option analytics, eg Gamma, Theta & Rho

o	Monte carlo simulations for Option volatility and stock prices

o	More analytics visualizations

o	Enhance dashboard, eg full stock quotes 

o	Other asset classes, eg cryptocurrencies, FX 

o	NR - Method does not converge for all the data points in Option Chain (implement  a more robust numerical method for American Option)

o	Create a website to host the dashboard

