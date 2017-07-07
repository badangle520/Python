tuple1 = (0, 1, 2, 3)
tuple2 = tuple1[:2] +  ('a',) + tuple1[2:] 
print(tuple2)

tuple2 = tuple2[:2] + tuple2[3:]
print(tuple2)

del tuple2
print(tuple2)

