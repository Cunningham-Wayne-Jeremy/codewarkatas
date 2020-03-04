def telephone_book(n):
    stringify = str(n)
    format = stringify.replace("[", "")
    print(format)
    return print(f"({str(n[:3])})-{n[3:6]}-{n[6:]}")

telephone_book([7,7,0,5,0,5,5,1,9,5])
