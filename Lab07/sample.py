try:
    print(H)
except ConnectionRefusedError as cfe:
    raise cfe
except OSError as oe:
    print("Error: {0}".format(type(oe).__name__))
except Exception as e:
    print("False")
else:
    print("True")
