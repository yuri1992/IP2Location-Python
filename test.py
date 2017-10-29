# Copyright (C) 2005-2016 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the MIT license


import os

from ip2location import IP2Location

database = IP2Location.IP2Location(os.path.join("data", "IP-COUNTRY.BIN"))

passed = 0
failed = 0
test_num = 0

for line in open(os.path.join("data", "country_test_ipv4_data.txt")):
    addr, country_short = line.strip().split()
    rec = database.get_all(addr)

    test_num += 1
    if rec is not None:
        if rec.country_short != country_short:
            failed += 1
            print("Test IP Address %s (Test %d) failed. We got %s but expected %s" \
                    % (addr, test_num, rec and rec.country_short or 'None', country_short))
        else:
            passed += 1

database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"))
for line in open(os.path.join("data", "country_test_ipv6_data.txt")):
    addr, country_short = line.strip().split()
    rec = database.get_all(addr)

    test_num += 1
    if rec is not None:
        if rec.country_short != country_short:
            failed += 1
            print("Test IP Address %s (Test %d) failed. We got %s but expected %s" \
                    % (addr, test_num, rec and rec.country_short or 'None', country_short))
        else:
            passed += 1

print('PASS: %d' % (passed))
print('FAIL: %d' % (failed))
