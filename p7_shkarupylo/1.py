format_tuple = [37.863, 'Brent', 3, 62.887, 1, 11]
format_tuple[0] = round(format_tuple[0], 2)
format_tuple[3] = round(format_tuple[3], 2)
format_tuple[4] = str(format_tuple[4]).zfill(2)
a = "The price of {1} crude oil fell to $ {0} per barrel, setting a {2}-month anti-record. The current " \
    "price is only {3}% of last year's {1} oil price on the same day ({4}.{5}). "
print(a.format(*format_tuple))
