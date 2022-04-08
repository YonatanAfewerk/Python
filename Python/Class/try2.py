# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
print(l)
for i in l:
	print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
print(t)
for i in t:
	print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
	print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
print(d)
for i in d:
	print("% s % d" % (i, d[i]))
