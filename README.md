# Project_Group5
Option Trading Applicatio: 

## Scope: 


## Type of Data,  Data Source, Clean up 



## Option Analytics - Calculation of IMplied Vol & Greeks 


## Coding: Option Analytics, Black-Scholes Model & Dashboard

###o  We broke our code down to three integral parts (Black-Scholes, Options Analytics, and Dashboard). 

###o  We first analyzed different strike prices for each ticker in scope to find the closest strike price from the current strike price.

###o  The second step was to retrieve End of the Day Option Prices from IEX Cloud for tickers in scope, one at a time and load the Options data into pandas data frame. The clean       up process for the data retrieved from IEX was one of the parts we spent a lot of time on. We also ran into data reliability issues and some data points experienced a lag       in being updated in the IEX cloud.

###o  The next step was to retrieve the historical data for each ticker in scope. This included the most recent closing price, market cap, 52 weeks high and low, PE Ratios along       with other details from IEX cloud and save them into a data frame. This allowed us to calculate:

####   Daily return

####   Rolling 30-day standard deviation

####   The annualized standard deviation

###o  For this phase of our project, we chose to focus on options with 30-60 days to expiry and thus have retrieved Treasury rates from IEX for 1- and 3-month maturities.

###o  We then loaded the Call & Put option data for different maturities into separate data frames and stored them in a dictionary for later use.

###o  Our next step was to calculate Implied Volatility & Options Greeks for option chain one ticker at a time and update relevant ticker dataframe in the Option Data dictionary.

####   To do this, we referred to the Black-Scholes Model and the Netwton-Raphson method for root solving. Note that: one issue we encountered here is that the Black Scholes            model computes the price for European options while we are using American options.

####   After computing the Implied Volatility, the next step was to calculate the Delta and Vega for each option strike and add them into the Option DF we had already created. 

####   Our findings showed that Newton’s Method does not converge for options that are ~20% away from the money.

###o  Once we calculated the Implied Vol and the Greeks and added them into the data frame, all we had to do was concatenate the Put and Call data frames of each ticker into the       final option data dictionary to later access for the dashboard and smiles.


## Visualization 

###o  Once we had everything loaded in the necessary data frames, it was time to move on to the visualization part. We did experience a few issues in creating the tables             (everything was jammed together, and it was impossible to read the table) and the graphs (some tickers were not showing in the drop down of the graphs and it took us a while     to figure out the issue) initially, however, after thorough research we were able to successfully.

###o  We created two different visualizations:

####	An option chain table with two tabs each representing the different maturities in our scope and a drop down for the user to select a ticker from the watchlist.

####	The option chain table showed the user all the different fields we extracted from IEX cloud and was separated by the type of option available (Call options on the              right and Put options on the left)

####	The Smiles were linked to the maturities tab selected in the option chain and had a separate drop down for the user to select a ticker. We plotted the Smiles                     separately for Calls and Puts but in the future we would like to combine the two together as they should be.


## Implications & Future Steps

###o  Broader stock selection for user

###o	More option maturities

###o	Additional option analytics, eg Gamma, Theta & Rho

###o	Monte carlo simulations for Option volatility and stock prices

###o	More analytics visualizations

###o	Enhance dashboard, eg full stock quotes 

###o	Other asset classes, eg cryptocurrencies, FX 

###o	NR - Method does not converge for all the data points in Option Chain (implement  a more robust numerical method for American Option)

###o	Create a website to host the dashboard

