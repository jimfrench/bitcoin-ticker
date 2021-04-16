#!/usr/bin/env python2

#Bitcoin currency valuation ticker
#Copyright (C) August 2017 Jim French

import traceback
import sys
import json
import urllib2


holdings = 0.33910153

request = urllib2.Request('http://coinmarketcap.northpole.ro/api/v5/BTC.json')

try:
    response = urllib2.urlopen(request)
except Exception:
    last_price = "0.00"
    tb = traceback.format_exc()
    print tb
else:
    the_page = response.read().split(",")
    last_price = the_page[49]
    
last_price = last_price.replace("\"gbp\":", "")
last_price = last_price.replace("\"", "")

rate_float = float(last_price.strip())
valuation = rate_float*float(holdings)
valuation = int(round(valuation))

print "<txt><span font-size='smaller' weight='normal' fgcolor='Orange'>&#163;",valuation,"</span></txt>"

