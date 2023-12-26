# This programme return the product of all others numbers
# array test
test=[1,2,3,4,5]
def product(test):

# Generate prefixes products
    list_prefixe=[]
    for number in test:
        if list_prefixe:
            list_prefixe.append(list_prefixe[-1]*number)
        else:
            list_prefixe.append(number)
# Generate suffixes products
    list_suffixe=[]
    for number in reversed(test):
        if list_suffixe:
           list_suffixe.append(list_suffixe[-1]*number)
        else:
           list_suffixe.append(number)

# reverse suffixes products
    list_suffixe=list(reversed(list_suffixe))
# Generate result from the product
    result=[]
    for i in range(len(test)):
        if i ==0:
           result.append(list_suffixe[i+1])
        elif i==len(test)-1:
            result.append(list_prefixe[i-1])
        else:
           result.append(list_prefixe[i-1]*list_suffixe[i+1])
           
    return result
   