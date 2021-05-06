<h1 align="center"> Welcome to Stock Watcher project! </h1>

<hr>

<h3 align="center"> Motivation </h3>
<p> This project aims to create custom ways to gather and analyze Stock market. Also it can be used as a playground for forecast methods.</p>

<hr>

<h3 align="left"> How to use </h3>

<h4> 1. Requirements </h2>
<ul>
    <li> Google Sheet sheets with an API enabled and credentials</li>
    <li> A sheet with 2 tabs (Stocks and Quotation) </li>
    <li> MongoDB database connection </li>
</ul>

<h4> 2. Configuration </h4>
<ol>
    <li> Change Creds.json to your Google Sheets API credentials </li>
    <li> On libs change the mongoDB connection on SheetWatcher.py, Stock.py and StockQuotation.py</li>
</ol>

<hr>

<h4> 3. Execution </h4>

<h5> 3.1 Track stocks </h5>

<p> Run <b><i>python -c "import trackStocks; trackStocks.handler('','')"</b></i> to track stocks from the google sheets</p>

<h5> 3.2 Stock Quotation </h5>

<p> Run <b><i>python -c "import stockQuotation; stockQuotation.handler('','')"</b></i> to track stocks from the google sheets</p>