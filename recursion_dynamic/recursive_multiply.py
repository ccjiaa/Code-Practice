def recursive_multiply(num1, num2):
    #Find the bigger and smaller number to avoid doing extra calls of countdown_multiply
    smaller = min(num1, num2)
    bigger = max(num1, num2)

    product = countdown_multiply(smaller, bigger) #initialize the recursion

    return product

    
def countdown_multiply(min, max):
    if min == 1: #when min reaches 1, add one stack of the bigger number
        return max
    
    #check if smaller number is odd
    is_odd = False
    if min%2 == 1:
        is_odd = True

    num = countdown_multiply(min//2, max) #keep calling self while halving min
    num = num + num #double the current stacks of the biggest number

    #if odd, add one more stack of the bigger number
    if is_odd:
        num += max

    return num


#This is O(log(N)) time, where N is the smaller value in the multiplication
#This is because we keep cutting the smaller number in half, which we do log(N) times. 
#We then do constant work for each division (one addition).
#Thus, O(log(N)) time

print(recursive_multiply(100, 7))