class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            try:
                min_disc = [j for j in prices[i+1:] if j <= prices[i]]
                min_disc = min_disc[0]
            except IndexError as e:
                min_disc = 0
            
            final_price = prices[i] - min_disc
            res.append(final_price)
        return res