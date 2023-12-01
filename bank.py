def main():
    size = int(input())

    #for loop
    for i in range(0,size):
        for j in range (0,i):
            print('*',end='')
        print('')

#untuk memastikan bahwa nama dari program ini adalah __main__
if __name__ == '__main__':
    main()