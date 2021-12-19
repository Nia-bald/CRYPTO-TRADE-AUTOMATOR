# CRYPTO-TRADE-AUTOMATOR
automating trade, only wazirx as a broker, does not use trading view, and requires you to run in non-headless mode
currently it only uses MACD strategy, I have no plans on applying it for other strategy, but If you want it, I can work on it.
for money  $$ DOLLA DOLLA $$, Yes, My life is sad I know, thank you.

Before you try to actually use it, I want to make it absoluetly clear that it is not advisable to use this, this is a horribly written programme which can be improved
In a million ways and there probably is a thousand times better version of this somewhere outthere. This was only a personal side project and Originally I did not plan on uploading it on github.


# BUT WHAT DOES IT DO EXACTLY!!!!

Well, calm down you piece of shit.
Given a list of currency pair values. it checks if the difference between MACD - signal line crosses the MACD threshold(see HOW TO USE section) and it trades 100% of the current INR Value you have, So it will buy only if you are not currently invested on a crypto, and sell if MACD - signal line crosses the threshold.


# HOW TO USE

Add the currency pair values and MACD threshold(once diff btwn MACD and signalLine crosses the threshold it will make the trade. By default all threshold are set to 0) on the first and second index of, list "currency_pair_values",
e.g
```
currency_pair_values = [
        ['ETH-INR', 0, 0],
        ['BNB-INR', 0, 0],
        ['LRC-INR', 0.5, 0],
        ['USDT-INR', 0.01, 0.02],
        ['SOL-INR', 0, 0],
        ['ADA-INR', 0, 0],
        ['SHIB-INR', 0, 0],
        ['BTC-INR', 1000, 0],
        #['WRX-INR', 0.01, 0]
    ]
```

The last index can be left empty, originaly it was supposed to represent previous MACD - previous Signal Line value.


also the trade only starts after like 5th candlestick/loop, you can change that if you want, by changing the variable
"LoopLim" to desired value.

or you can make the proggrame not Trade at all by setting "realMODE" = False.
doing this everything will be same, only difference is that it will not press the BUY or SELL button

Also you can change the candlestick on which you wanna operate by replacing the function
```
switchTo5
```

to any of

```
switchTo15
switchTo30
switchTo1

```


I know a lot of it could be taken by user as an input, but like I said, it's a piece of shit programme, and I advise you to not use it.
Btw I can totally work on it more, to make it more user-friendly or even Improve or add new features, but I don't see anyone using it. So if you want that, then please tell me.

