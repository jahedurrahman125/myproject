# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for task: ruutu
def print_box(width, height, mark):
    for i in range (0,height):
        if height-==1:
            print(mark*width)


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")
    print("")
    print_box(width, height, mark)


main()
