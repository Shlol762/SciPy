from physics import *

s1, s2 = Speed(9, 3, unit='cm/s', extra_units=['cm/h']), Speed(9, 2, unit='cm/h', extra_units=['cm/h'])

print(s2.distance.unit)