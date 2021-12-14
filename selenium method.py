from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pushbullet import PushBullet
import sys

pb = PushBullet('o.7kBuEUI8FaYRxnRoFJtaBfKs9GCfpC3c')
try:
    # ------- setting up list of drivers
    pb.push_note("Hello Faggot", "Python script is on")
    currency_pair_values = [
        # ['ETH-INR', 0, 0, 0],
        # ['BTC-INR', 5000, 4237, 911],
        # ['BNB-INR', 0, 0, 0],
        # ['LRC-INR', 0.5, -0.4206, -1.1067],
        #['USDT-INR', 0.01, 0.02],
        # ['SOL-INR', 0, 0, 0],
        #['ADA-INR', 0, 0],
        ['SHIB-INR', 0.000002, 0],
        # ['BTC-INR', 1000, 8089],
        # ['SHIB-INR', 0, 0],
        #['WRX-INR', 0.01, 0]
    ]
    # args: currency pair, alert threshold, prev MACD - prev Signal Line

    # opens up the browser for each currency-pair
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://wazirx.com/exchange/')
    input("Enter anything after logged in: ")

    # need a login code here

    driver.get('https://wazirx.com/exchange/' + currency_pair_values[0][0])
    j = 1
    # --------------initialization loop initializes all the tabs corresponding to currency_pair_values--------------
    # no problem here works flawlessly
    while j < len(currency_pair_values):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[j])
        driver.get('https://wazirx.com/exchange/' + currency_pair_values[j][0])
        j += 1

    input()

    # ------------------------------------------------------various actions------------------------------------------
    # ------------------------------------------------need to place these in a module--------------------------------

    # below 3 functions works flawlessly, size can be reduced, reducing the size will result in more compilation time

    def switchTo30(driver):
        # switching to 30 min candlestick
        candle30 = driver.find_element(by='xpath',
                                       value=r'/html/body/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/span[4]')
        candle30.click()
        sleep(2)

    def switchTo15(driver):

        candle15 = driver.find_element(by='xpath',
                                       value=r'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/span[3]')
        candle15.click()
        sleep(2)

    def switchTo1(driver):

        candle1 = driver.find_element(by='xpath',
                                      value=r'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/span[1]')
        candle1.click()
        sleep(2)

    def switchTo5(driver):
        candle5 = driver.find_element(by='xpath',
                                      value=r'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/span[2]')
        candle5.click()
        sleep(2)


    # below 3 functions requires selenium to get into an iframe
    # but at the end of all the code we return to default frame
    def selectTheMACDIndicator(driver):
        # presses the indicator list button
        Indicator_chooser_button = driver.find_element(by="xpath",
                                                       value=r'/html/body/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/button[1]')
        Indicator_chooser_button.click()
        driver.switch_to.frame(0)  # switches to indicator list frame
        sleep(2)
        # Opens up the MACD indicator
        MACD_indicator_button = driver.find_element(by="xpath",
                                                    value=r'/html/body/div[5]/div/div/div[1]/div/div[3]/div/div[48]')
        MACD_indicator_button.click()

        # Closes indicator list
        Indicator_close_button = driver.find_element(by='xpath',
                                                     value='/html/body/div[5]/div/div/div[1]/div/div[1]/span')
        Indicator_close_button.click()
        driver.switch_to.default_content()

    def GetMACD(driver):
        driver.switch_to.frame(0)
        sleep(1)
        # gets the MACD Value
        MACD_value = driver.find_element(by='xpath',
                                         value='/html/body/div[2]/div[1]/div/div[1]/div[2]/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
        if MACD_value.text[0] == '−':
            buffer = MACD_value.text[1:]
            driver.switch_to.default_content()
            return '-' + buffer
        else:
            buffer = MACD_value.text
            driver.switch_to.default_content()
            return buffer

    def GetSignalLine(driver):
        driver.switch_to.frame(0)
        sleep(1)
        SignalLineValue = driver.find_element(by='xpath',
                                              value='/html/body/div[2]/div[1]/div/div[1]/div[2]/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')

        if SignalLineValue.text[0] == '−':
            buffer = SignalLineValue.text[1:]
            driver.switch_to.default_content()
            return '-' + buffer
        else:
            buffer = SignalLineValue.text
            driver.switch_to.default_content()
            return buffer

    def buyingAt(driver, percentage=100, lowestPrice=True, realMode=False):

        # Clicking the buttons
        buyTab = driver.find_element(by='xpath', value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[1]/div[1]')
        buyTab.click()

        if lowestPrice:
            lowestPriceButton = driver.find_element(by='xpath',
                                                    value="/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[2]/div/div/div[2]/span")
            lowestPriceButton.click()

        if percentage == 25:
            button25 = driver.find_element(by='xpath',
                                           value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div/div[2]/div[2]/button[1]')
            button25.click()
        elif percentage == 50:
            button50 = driver.find_element(by='xpath',
                                           value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div/div[2]/div[2]/button[2]')
            button50.click()
        elif percentage == 75:
            button75 = driver.find_element(by='xpath',
                                           value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div/div[2]/div[2]/button[3]')
            button75.click()
        elif percentage == 100:
            button100 = driver.find_element(by='xpath',
                                            value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div/div[2]/div[2]/button[4]')
            button100.click()

        # getting the info
        buyingAtelement = driver.find_element(by='xpath',
                                              value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[2]/div/div/input')
        buyingAtValue = buyingAtelement.get_attribute('value')

        totalINRelement = driver.find_element(by='xpath',
                                              value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div/div[1]/input')

        totalINR = totalINRelement.get_attribute('value')

        totalBoughtelement = driver.find_element(by='xpath',
                                                 value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div/div/input')
        totalBought = totalBoughtelement.get_attribute('value')

        if realMode:
            buy_button = driver.find_element(by='xpath',
                                             value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/button')
            buy_button.click()

        return {"totalINR": totalINR, "totalBought": totalBought, "buyingAT": buyingAtValue}

    def sellingAt(driver, percentage=100, HighestPrice=True, realMode=False):

        # Clicking the buttons
        sellTab = driver.find_element(by='xpath', value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[1]/div[2]')
        sellTab.click()

        if HighestPrice:
            HighestPriceButton = driver.find_element(by='xpath',
                                                     value="/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[2]/div/div/div[2]/span")
            HighestPriceButton.click()

        if percentage == 25:
            button25 = driver.find_element(by='xpath',
                                           value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div/div[2]/div[2]/button[1]')
            button25.click()
        elif percentage == 50:
            button50 = driver.find_element(by='xpath',
                                           value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div/div[2]/div[2]/button[2]')
            button50.click()
        elif percentage == 75:
            button75 = driver.find_element(by='xpath',
                                           value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div/div[2]/div[2]/button[3]')
            button75.click()
        elif percentage == 100:
            button100 = driver.find_element(by='xpath',
                                            value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div/div[2]/div[2]/button[4]')
            button100.click()

        # getting the info
        sellingAtelement = driver.find_element(by='xpath',
                                               value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[2]/div/div/input')
        sellingAtValue = sellingAtelement.get_attribute('value')

        totalINRelement = driver.find_element(by='xpath',
                                              value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div/div/input')

        totalINR = totalINRelement.get_attribute('value')

        totalsoldelement = driver.find_element(by='xpath',
                                               value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div/div[1]/input')
        totalsold = totalsoldelement.get_attribute('value')

        if realMode:
            sell_button = driver.find_element(by='xpath',
                                              value='/html/body/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div/form/button')
            sell_button.click()
        return {"totalINR": totalINR, "totalsold": totalsold, "sellingAT": sellingAtValue}

    # for loop part of initialization which sets each tab to a preferred candlestick value
    # also selects the macd indicator
    for i in range(len(currency_pair_values)):
        driver.switch_to.window(driver.window_handles[i])
        switchTo5(driver)
        selectTheMACDIndicator(driver)

    pb.push_note("Hello", "While loop Started")

    percent = 100
    j = 1
    status = False
    changeAsset = len(driver.window_handles)

    # The Main loop which runs, collecting the data and using actions to buy or not buy coins
    while True:
        # if condition in case there is a new window it sets all the candlestick in the new window to preferred
        # candlestick and selects the MACD indicator
        if changeAsset != len(driver.window_handles):
            for i in range(changeAsset, len(currency_pair_values)):
                driver.switch_to.window(driver.window_handles[i])
                switchTo5(driver)  # 2 sec
                selectTheMACDIndicator(driver) # 2 sec

        sleep(10)
        for i in range(len(driver.window_handles)):
            if(len(driver.window_handles) > 1):
                driver.switch_to.window(driver.window_handles[i])
            cdiff = float(GetMACD(driver)) - float(GetSignalLine(driver))

            if currency_pair_values[i][2] < currency_pair_values[i][1] <= cdiff:
                buy_details = buyingAt(driver, percentage=percent,realMode=status)
                print(str(buy_details) + " " + str(currency_pair_values[i][0]))
                pb.push_note('Hello friend', 'Bought ' + currency_pair_values[i][0] + '\n details:' + str(buy_details))
            if currency_pair_values[i][2] > 0 >= cdiff:
                sell_details = sellingAt(driver, percentage=percent, realMode=status)
                print(str(sell_details) + " " + str(currency_pair_values[i][0]))
                pb.push_note('Hello friend', 'sold' + currency_pair_values[i][0] + '\n details:' + str(sell_details))

            print("cdiff:" + str(cdiff) + " pdiff:" + str(currency_pair_values[i][2]))
            currency_pair_values[i][2] = cdiff

        if changeAsset != len(driver.window_handles):
            sleep(290 - 2*len(currency_pair_values) - 4*(abs(changeAsset - len(driver.window_handles))))
        else:
            sleep(290 - 2*len(driver.window_handles))

        if j == 5:
            status = True

        changeAsset = len(driver.window_handles)

        print("loop no." + str(j))
        j += 1
        

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
