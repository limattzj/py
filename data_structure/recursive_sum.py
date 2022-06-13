def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


if __name__ == "__main__":

    x = sum([1, 2, 3, 4])
    print(x)
