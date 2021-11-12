def main():
    
    N=int(input())
    a=1
    for i in range(1,N+1):
        for j in range(1,N-i+1):
            print("0",end=" ")
        for z in range(1,2*i):
            if(z<=i):
                print(str(a-(i-z))+" ",end="")
            else:
                print(str(a+(i-z)) + " ",end="")
        for j in range(1,N-i+1):
            print("0",end=" ")
        a+=2
        print()

    return 0

if __name__ == '__main__':
    main()