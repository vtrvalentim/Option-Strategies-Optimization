from Strategy_Folder.StrategyBaseModule import *

class Strategy44(StrategyBase):

    #4.4. Short call

    #Properties:
    #maxprofit (float)
    #maxprofitindex (int)
    #breakeven (float)
    #breakevenindex (int)
    #asset1 = short call
    #qtty1 = 1

    def __init__(self,stock,asset1,qtty1,fee):
    
        StrategyBase.__init__(self,"short call",stock,asset1=asset1,qtty1=qtty1)

        #1. split self.priceatmaturity

        #split 1: elements <= asset1.strike
        split1 = self.priceatmaturity[self.priceatmaturity<=asset1.strike]
        #split 2: elements > asset1.strike
        split2 = self.priceatmaturity[self.priceatmaturity>asset1.strike]


        #2. use split results to create cte valued arrays

        #out1 from split 1: output element values = -asset1.price-asset3.price+(2*asset2.price)
        vout1 = asset1.price
        out1 = np.full(split1.shape,vout1)


        #3. use split results to create function valued arrays

        #out 2 from split 2: output elements func = asset1.price - self.priceatmaturity[i] + asset1.strike
        vout2 = asset1.price + asset1.strike
        out2 = [(vout2 - x) for x in split2]


        #4. join output arrays into one
        self.profit = np.concatenate((out1,out2))


        #5. Calculating properties
        self.maxprofitindex = np.argmax(self.profit)
        self.maxprofit = np.amax(self.profit)
        self.cost = vout1
        self.cost,self.profit = AccountForFee(fee,self.profit,self.cost,self.qtty1,self.qtty2,self.qtty3,self.qtty4)
        self.breakeven,self.breakevenindex = GetBreakEvenPoint(self.profit,1,self.graphprecision,self.xaxisrange)
        self.risk = 4


        pass
    pass
