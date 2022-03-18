#alternatively can use return str(x) == str(x)[::-1] for a faster runtime, surprisingly memory usage is the same
#[::-1] is shorthand indexing to check the reverse

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        
        rev_num=0
        digit=0
        
        #continues running as long as there are still digits to check
        #when floor division becomes larger than the number, the condition stops bc
        #when it is larger than the number it is dividing by, it equals 0
        while(x//10**digit != 0):
            #1: "chops" the number
            #2: adds on what the next digit will be (if any)
            
                    #1            #2
            rev_num=(rev_num*10)+(x//(10**digit)%10)
            digit+=1
        return (x==rev_num)
