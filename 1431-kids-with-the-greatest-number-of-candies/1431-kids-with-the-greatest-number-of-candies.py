class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans=[]
        maxi=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxi:
                ans.append(True)
            else:
                ans.append(False)
        return(ans)