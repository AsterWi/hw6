result = []
def divider(a, b):
    try:
        return a/b
    except (TypeError,ZeroDivisionError):
        print(f"{TypeError}: {a}/{b} caused error")

data = {10: 2, 2: 5, "123": 4, 18: 0, tuple([]): 15, 8 : 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)
print(result)