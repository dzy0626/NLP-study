"""You are given n types of coin denominations of values v(1) < v(2) < ... < v(n) (all integers). 
   Assume v(1) = 1, so you can always make change for any amount of money C. Give an algorithm 
   which makes change for an amount of money C with as few coins as possible. """
class MakingChangeSolution():
    def __init__(self, coinDenominationOfValues):
        self.coinDenominationOfValues = sorted(coinDenominationOfValues)
        self.optimalNumberOfCoinsFromOneToC = {}

    def changeMinNumberCoins(self, C):
        self.moneyFromOneToC = list(map(str, range(1, C + 1)))
        if C in self.coinDenominationOfValues:
            optimalNumberOfCoins = 1
        else:
            optimalNumberOfCoins = self.findOutMinNumber(C)
        return optimalNumberOfCoins
            
    def findOutMinNumber(self, C):
        import math
        for money in self.coinDenominationOfValues:
            self.optimalNumberOfCoinsFromOneToC[str(money)] = 1
        for i in range(0, C):
            if self.moneyFromOneToC[i] in self.optimalNumberOfCoinsFromOneToC.keys():
                continue
            allChoiceOfChanging = []
            for j in range(0, math.ceil(i/2)):
                choice = self.optimalNumberOfCoinsFromOneToC[str(i - j)] +self.optimalNumberOfCoinsFromOneToC[str(j + 1)]
                allChoiceOfChanging.append(choice)
            self.optimalNumberOfCoinsFromOneToC[str(i+1)] = min(allChoiceOfChanging)
        return self.optimalNumberOfCoinsFromOneToC[str(C)]


w = MakingChangeSolution([1, 3, 5, 10, 100])
minCoins = w.changeMinNumberCoins(14)
print(minCoins)
