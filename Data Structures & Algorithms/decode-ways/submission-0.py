class Solution:
    def numDecodings(self, s: str) -> int:
        """
        U: We are trying to count number of ways we can decode a message. We can do with dfs and backtrackng or 1d idea

        M:
        P:
        for every digital we can say read it as its own or read it with i+1 
        we dont techically give the groupins. we just need to know what groupings are possible
        Ex:
        1223
        we start with 1:
        it can be 1 or 12
        then 2, it can be 2 or 22
        then 2, it can be 2 or 23

        to avoid repitions keep the combinations we are trying in set. so we can look up to see if we already used it
        and we make sure we do not use invalid ones. like anything greater than 26 or 01 or 0something

        """

        one = 1
        two = 0

        for i in range(len(s) -1, -1, -1):
            total_ways = 0

            if s[i] != "0":
                total_ways = one

                if i+1 < len(s) and 10<= int(s[i:i+2]) <=26:
                    total_ways+=two

            two = one
            one = total_ways

        return one
