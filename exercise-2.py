def index_power(numnbers, n):
    try:
        result = numnbers[n] ** n
        return result
    except:
        return -1
    
print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0))
print(index_power([1, 2], 3))

