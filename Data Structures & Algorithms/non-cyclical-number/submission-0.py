class Solution:
    def isHappy(self, n: int) -> bool:
        # Return true if non-cyclic or return false if cyclic
        #Conditons to be non-cyclic
            #split the the digits and square and sum it
            # IF IT IS 1, CYCLIC 
            #IF NOT REPEAT THE STEP TILL WE HAVE FOUND THE LOOP
            # NEED TO STORE THE SUM IF SUM IS THERE AGAIN PROBABLY A LOOP

            seen = set()

           
            
            while n not in seen:
                if n == 1:
                    return True
                seen.add(n)
                sum_digits = 0
                # seperate the digits
                while n > 0:
                    digit = n %10
                    sum_digits+=digit **2
                    n//=10
                n = sum_digits
            return False
                
