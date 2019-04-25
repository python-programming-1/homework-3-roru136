def collatz(num):
    if num %2 == 0:
        even = num // 2
        print (even)
        return even
            
    elif num %2 == 1:
        odd = 3*num +1
        print(odd)
        return odd


while True:
    print('num:')
    
    try:
        num_input = int(input())
        if num_input == 1:
            print('Enter an integer >1')
        elif num_input>1:
            num_input =collatz(num_input)
            while True:
                if num_input == 1:
                    break
                else:
                    num_input=collatz(num_input)
                      
    except:
        print('Not valid Integer')
        break


