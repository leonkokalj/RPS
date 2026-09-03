
def hello():
    oddelek = input("kateri oddelek si?")
    if oddelek.lower() == "1.ri":
        print(f"hello {oddelek} ♥")
    else:
        print(f"hello {oddelek}")

def poštevanka():
    x = int(input ("izberi si število"))
    y= 1
    while y <= 10:
        print(f"{y} * {x} = {y * x}")
        y += 1
        
    

if __name__ == "__main__":
    # hello()
    poštevanka()

