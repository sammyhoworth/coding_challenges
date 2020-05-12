
def powerset(it):
    itl = list(it)
    r = [[]]
    for i in itl:
        temp = [[i] + rest for rest in r]
        r += temp
    return r


if __name__ == "__main__":
    input_set = {1,2,'a'}    
    print(powerset(input_set))
