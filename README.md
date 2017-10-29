# IP2Location 9.0.0

Enable Thread safe IPLocation use.

```
from ip2location import IP2Location

IP_LOCATION = IP2Location.IP2Location(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'IP-COUNTRY.BIN'))

def get_ip(ip):
   return IP_LOCATION.get_country_short(self.ipaddress)
```


This is a IP2Location Python library that enables the user to find the country, region or state, city, latitude and longitude, US ZIP code, time zone, Internet Service Provider (ISP) or company name, domain name, net speed, area code, weather station code, weather station name, mobile country code (MCC), mobile network code (MNC) and carrier brand, elevation, and usage type by IP address or hostname originates from. The library reads the geo location information
from **IP2Location BIN data** file.

Supported IPv4 and IPv6 address.

For more details, please visit:
[http://www.ip2location.com/developers/python](http://www.ip2location.com/developers/python)

# Requirements
1. Python 2.2 and above

# Installation
1. Unzip the package.
2. Execute python setup.py build
3. Execute python setup.py install

# Testing
    python sample.py
    python test.py

# Sample BIN Databases
* Download free IP2Location LITE databases at [http://lite.ip2location.com](http://lite.ip2location.com)  
* Download IP2Location sample databases at [http://www.ip2location.com/developers](http://www.ip2location.com/developers)

# Support
Email: support@ip2location.com.  
URL: [http://www.ip2location.com](http://www.ip2location.com)
