date +'%b_%d_%R' | tr -d '\n' | sed 's/^/python getTweets.py /' > run.sh
