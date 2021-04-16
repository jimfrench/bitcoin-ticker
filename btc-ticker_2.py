#!/usr/bin/env python2

#Bitcoin currency valuation ticker
#Copyright (C) August 2017 Jim French

import sys
import json
import urllib2
import getopt


def main(argv):
    holdings = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'btc-ticker.py -i <holdings>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'btc-ticker.py -i <holdings>'
            sys.exit()

        elif opt in ("-i"):
            holdings = arg

    request = urllib2.Request('https://api.coindesk.com/v1/bpi/currentprice/GBP.json')

    try:
        response = urllib2.urlopen(request)
    except Exception:
        last_price = "0.00"
    else:
        the_page = response.read().split(",")
        last_price = the_page[15]

    last_price = last_price.replace("\"rate_float\":", "")
    last_price = last_price.replace("}}}", "")
    rate_float = float(last_price.strip())
    valuation = rate_float*float(holdings)
    valuation = int(round(valuation))

    print(""u"\xA3" + str(valuation))


if __name__ == "__main__":
    main(sys.argv[1:])
