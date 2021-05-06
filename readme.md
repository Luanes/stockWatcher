<h1 align="center"> Welcome to Stock Watcher project! </h1>

<hr>

<h2 align="center"> Motivation </h3>
<p> This project aims to create custom ways to gather and analyze Stock market. Also it can be used as a playground for forecast methods </p>

<hr>

<h2 align="left"> How to use </h3>

<h3> 1. Requirements </h2>
<ul>
    <li> Google Sheet sheets with an API enabled and credentials</li>
    <li> A sheet with 2 tabs (Stocks and Quotation) </li>
    <li> MongoDB database connection </li>
</ul>

<h3> 2. Configuration </h4>
<ol>
    <li> Change Creds.json to your Google Sheets API credentials </li>
    <li> On libs change the mongoDB connection on SheetWatcher.py, Stock.py and StockQuotation.py</li>
</ol>

<hr>

<h3> 3. Execution </h4>

<h4> 3.1 Track stocks </h5>

<h6> Run <b><i>python -c "import trackStocks; trackStocks.handler('','')"</b></i> to track stocks from the google sheets</h6>

<h4> 3.2 Stock Quotation </h5>

<h6> Run <b><i>python -c "import stockQuotation; stockQuotation.handler('','')"</b></i> to track stocks from the google sheets</h6>

<h4>Google Sheet sample </h4>

<h6> https://docs.google.com/spreadsheets/d/1ZJ91fUv-XgWOkuh3_G2KPCbjGmSF0TlhX-_xo_V-nr8/edit?usp=sharing </h6>