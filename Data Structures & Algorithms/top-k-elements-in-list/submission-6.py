class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need bucket sort to sort it
        # Make a dictioanry to find the most frequent elements
        # Then a bucket to sort the frequecies. The index will correspond to the freq and the value inside will corespond to value in numb which ahs the freq




        # make a coutner with freq
        nums_freq = Counter(nums)
        
        #make the buckets
        buckets = [[] for _ in range(len(nums)+1)]

        # loop through freq and put it in the buckets

        for key, freq in nums_freq.items():
            #We will use freq as index
            buckets[freq].append(key)

        
        # after we have the buckets ready
        # we just need the last k freq buckets
        # So we can do a result array
        result = []
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i]:
                # we need another loop to put everything in buckets[i] wihtout exceeding k
                for j in buckets[i]:
                    result.append(j)
                    if len(result) == k:
                        return result
    
                    
        