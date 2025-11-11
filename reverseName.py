def reverseName(name):
    first, last = name.split(" ")
    return f"{last}, {first}"
def main():
    names = int(input("How many names will you enter? "))
    for i in range(names):
        name = input("Enter a name, beginning with first name: ")
        print(f"Revered name is {reverseName(name)}")
main()