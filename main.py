inp1 = input().lower()
inp2 = input().lower()

def print_in(inp1,inp2):
    if inp1 < inp2:
        print('-1')
    elif inp1 > inp2:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    print_in(inp1,inp2)
