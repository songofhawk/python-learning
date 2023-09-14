if __name__ == "__main__":
    q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
    print( q([3, 1, 42, 32]) )
