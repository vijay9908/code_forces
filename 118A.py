s = input()
print("".join('.'+x for x in s.lower() if x not in 'aeiouy'))
