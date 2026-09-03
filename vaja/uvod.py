
def hello():
    oddelek = input("kateri oddelek si?")
    if oddelek.lower() == "1.ri":
        print(f"hello {oddelek} ♥")
    else:
        print(f"hello {oddelek}")

        
if __name__ == "__main__":
    hello()