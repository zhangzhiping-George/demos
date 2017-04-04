def bisearch(seq, num, lower=0, upper=None):
    if upper == None: upper = len(seq)-1    
    if seq[lower] == seq[upper]:            
            return upper
    else:
            middle = (lower + upper)//2
            if seq[middle] == num: 
                return middle
            elif seq[middle] > num:
                return bisearch(seq, num, middle, upper)
            else:
                return bisearch(seq, num, lower, middle)


seq = [5,3,7,4,1]
seq.sort()
print(bisearch(seq, 4))
