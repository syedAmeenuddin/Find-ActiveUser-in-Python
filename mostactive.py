_customer="BIGCORP BIGCROP ACME BIGCROP ZORK ZORK ABC BIGCROP ACME BIGCROP BIGCROP ZORK BIGCROP ZORK ZORK BIGCROP ACME BIGCROP ACME BIGCROP ACME LITTLECORP NADIRCORP"
customers =_customer.split(" ")
print(customers);
totlen = len(customers)
trade = 15/100 * totlen
Activecus = {};
passedActiveus = [];
for i in customers:
    lower = i.lower();
    Activecus[lower] = Activecus.get(lower,0) + 1
    cap = lower[0].upper()+lower[1:]
    if Activecus.get(lower) > trade and cap not in passedActiveus:
        passedActiveus.append(cap)
passedActiveus.sort()
print(passedActiveus)
