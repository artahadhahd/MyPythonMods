def arrow(x: int):
    def head():
        star = list(range(x, -1, -2))
        for i in range(x//2,0,-1):
            print(i * " " + star[i] * "*")
        print(x * "*")

    def lines():
        print(f"{(x//2-1) * ' '}***\n" * 5 + f"{(x//2-1) * ' '}***")
    
    head()
    lines()
