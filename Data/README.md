# DATA SOURCES
 
Historical stock price data acquired from Yahoo Finance. This can be utilized to calculate volatility. Riskless interest rates can be obtained from T-bill yields (under one year).

## Yahoo Finance Data 
[Yahoo Finance](https://finance.yahoo.com/) is an excellent source for historical equity prices and option chains, which include implied volatilties (presumably from inverting the Black-Scholes formula).

## Riskless Rates Data 
The [Treasury](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield) provides data on daily Treasury yield curve interest rates. 

## Options Chain Examples 

See below for the options data on equities implemented within this projects notebooks for the CRR and JR models: 

| Company | Ticker | Industry |  Options Chain  | Historical Stock Price Data | 
| --- | --- | --- | --- | --- |
| American Airlines | `AAL` | Aviation |  [options](https://finance.yahoo.com/quote/AAL/options/)  |  [price data](https://finance.yahoo.com/quote/AAL/history?p=AAL) |
| Norwegian Cruise Line | `NCLH` | Cruise lines | [options](https://finance.yahoo.com/quote/NCLH/options/)| [price data](https://finance.yahoo.com/quote/NCLH/history?p=NCLH) |
| Newmont Corporation | `NEM` | Gold mining | [options]()| [price data](https://finance.yahoo.com/quote/NCLH/history?p=NCLH)|
| Lithium Americas Corp. | `ticker` | Lithium mining | [options](https://finance.yahoo.com/quote/NEM/options?p=NEM) | [price data](https://finance.yahoo.com/quote/NEM/history?p=NEM) |
| McDonald's Corp. | `ticker` | Fast-food | [options]() | [price data]() |
| Coca-Cola Corp. | `ticker` | Food & Beverage | [options]() | [price data]() |
| Carvana | `ticker` | Auto retail | [options]() | [price data]() |
| Credit Acceptance Corp. | `CACC` | Auto finance | [options]() | [price data]() |
| Banco Santander | `SAN` | Retail banking | [options]() | [price data]() |
| Simon Property Group | `SPG` | Real estate| [options]() | [price data]() |
| Pool Corp. | `SPG` | Real estate| [options]() | [price data]() |
| Glencore | `SPG` | Real estate| [options]() | [price data]() |
| Nordic American Tanker | `NAT` | Real estate| [options]() | [price data]() |




