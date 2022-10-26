# MATHS- Calculates the average of numbers within an array
def arrayAverage(array):
    holder = 0
    for i in range(len(array)):
        holder += array[i]
    return holder / len(array)

# GRAPHICS- creates two triangles, one in the opposite direction
def draw(x: int):
    format = [i for i in range(1, x+1)]
    # format = list(range(1, x + 1))
    for i in range(x-1, -1, -1):
        print(format[x-1-i] * ' ' + format[i] * '$')
    for n in range(2,x+1):
        print(x * ' ' + n * '$')

# TODO: finish and add Arrow.py (Graphics related)