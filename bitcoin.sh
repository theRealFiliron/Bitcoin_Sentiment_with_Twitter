wget -O bitcoin.txt "https://finance.yahoo.com/quote/BTC-USD/"; cat bitcoin.txt | egrep -o 'data-reactid="34">[0-9.,]*' | sed 's/data-reactid="34">//' | tr -d '/n'
