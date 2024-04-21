#2024/2/11 Flights
# selenium based driver to obtain flights 
# crontab -e
# 11 5 * * *  /data/data/com.termux/files/usr/bin/python3 /data/data/com.termux/files/home/storage/flights/test-view.py
# test * * * * *  /data/data/com.termux/files/usr/bin/python3 /data/data/com.termux/files/home/storage/flights/aa.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import requests
from datetime import datetime
import threading

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")

def findPriceForDate(driver, dateStr): # 2024-10-01
    element = driver.find_element(By.XPATH, "//*[@data-iso='"+dateStr+"']")
    child_elements = element.find_elements(By.XPATH, ".//*[starts-with(text(), '£')]")
    priceStr = child_elements[0].text
    numberStr = priceStr[1:] 
    numberStr = numberStr.replace(",", "")
    numberStr = numberStr.replace("K", "000")
    number = float(numberStr)
    return number

def searchWithRange(oneSearchRange, returnArray):
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1280, 720)

    url = oneSearchRange['url']
    daysRange = oneSearchRange['daysRange']
    incrementDaysRange = oneSearchRange['incrementDaysRange']
    dateRanges = oneSearchRange['dateRanges']

    results = []

    print("")
    print(f"Searching {daysRange} days")

    driver.get(url)

    time.sleep(2)

    try: 
        element = driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Accept all')]")
        element.click()
        time.sleep(5)
    except:
        print("No Accept All button, probabaly already accepted")

    boxSelectYear = dateRanges[0]['year']
    boxSelectMonth = dateRanges[0]['month']
    monthSpace = "0" if boxSelectMonth < 10 else ""
    
    searchStr = f"//*[@data-value and starts-with(@data-value, '{boxSelectYear}-{monthSpace}{boxSelectMonth}-')]"
    element = driver.find_element(By.XPATH, searchStr)
    element.click()  # Opens the dates dialog on screen
    time.sleep(20)

    while incrementDaysRange > 0:

        for oneDaterange in dateRanges:
            year = oneDaterange['year']
            month = oneDaterange['month']
            daysMax = oneDaterange['daysMax']

            for i in range(1, daysMax+1):
                monthSpacer = "0" if month < 10 else ""
                daySpacer = "0" if i < 10 else ""

                dateStr = f"{year}-{monthSpacer}{month}-{daySpacer}{i}"
                try: 
                    oneKey=f"{dateStr}({daysRange})"
                    oneVal=findPriceForDate(driver, dateStr)
                    pricePerDay = oneVal / daysRange
                    print(f"{oneKey}: £{oneVal}: PPD:£{pricePerDay}")
                    results.append({'dayStr': oneKey, "price": oneVal, "pricePerDay": pricePerDay})
                except:
                    print(""+dateStr+": NO PRICE") 

        incrementDaysRange = incrementDaysRange - 1
        daysRange = daysRange + 1

        if incrementDaysRange > 0:
            # look for 'day trips'
            element = driver.find_element(By.XPATH, "//*[contains(text(), 'day trips')]")
            dayTripsStr = element.text
            firstNumberStr = dayTripsStr.split()[0]
            firstNumber = int(firstNumberStr)
            print(f"{firstNumber} days found")
            parent_element = element.find_element(By.XPATH, '..')
            children_elements = parent_element.find_elements(By.XPATH, '*')  # Finds all direct children
            index = children_elements.index(element)
            nextElement = children_elements[index+1]
            print("Incrementing by 1")
            nextElement.click()
            print("Waiting to populate next list")
            time.sleep(14)

    driver.quit()
    returnArray.extend(results)
    return results

def sendToSlack(payloadStr):
    webhook_url = 'https://hooks.slack.com/services/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'
    data = {'text': payloadStr}
    headers = {'Content-type': 'application/json'}

    response = requests.post(webhook_url, headers=headers, json=data) 

    if response.status_code == 200:
        print("Sent to Slack OK")
    else:
        print("Send to Slack Error: An error occurred:", response.text) 

def main():

    daterangeJulAug = [{'year': 2024, 'month': 7, 'daysMax': 31}, {'year': 2024, 'month': 8, 'daysMax': 31}]
    daterangeSepOct = [{'year': 2024, 'month': 9, 'daysMax': 30}, {'year': 2024, 'month': 10, 'daysMax': 31}]
    daterangeAugSep = [{'year': 2024, 'month': 8, 'daysMax': 31}, {'year': 2024, 'month': 9, 'daysMax': 30}]
    daterangeOctNov = [{'year': 2024, 'month': 10, 'daysMax': 31}, {'year': 2024, 'month': 11, 'daysMax': 30}]
    startDays = 80
    finishDays = 89 - startDays
    searchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTEwLTIwagwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": startDays,
                     "incrementDaysRange": finishDays,
                     "dateRanges": daterangeAugSep},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTEyLTI4agwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": startDays,
                     "incrementDaysRange": finishDays,
                     "dateRanges": daterangeOctNov},
                     ]

    foundPrices = []
    hThreads = []

    def SafeCall(oneSearchRange, foundPrices):
        try:
            searchWithRange(oneSearchRange, foundPrices)
        except:
            print(f"\n\nError for {oneSearchRange['daysRange']}\n")

    for oneSearchRange in searchRanges:
        newThread = threading.Thread(target=SafeCall, args=(oneSearchRange, foundPrices,))
        hThreads.append(newThread)
        newThread.start()
    
    # wait for all threads to finish
    for hThread in hThreads:
        hThread.join()
    
    def sort_by_price(item):
        return item['price']
    
    def sort_by_ppd(item):
        return item['pricePerDay']
    
    foundPrices.sort(key=sort_by_ppd)  # Sort by ppd ascending
    topPrices = foundPrices

    payloadStr = []

    def capture_print(message):
        payloadStr.append(message)

    now = datetime.now()
    date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")  # Example: '2023-11-18 20:22:40'
    print(date_time_string)

    str = f"{date_time_string}\nTop 10 PPD\n"
    print (str)
    capture_print(str)

    for topPrice in topPrices[:10]: 
        str = f"{topPrice['dayStr']}: £{topPrice['price']} PPD £{topPrice['pricePerDay']:.2f}"
        print(str); 
        capture_print(str)
    
    foundPrices.sort(key=sort_by_price)  # Sort by price ascending
    topPrices = foundPrices

    str = "\nTop 10 prices\n"
    print (str)
    capture_print(str)

    for topPrice in topPrices[:10]:
        str = f"{topPrice['dayStr']}: £{topPrice['price']} PPD £{topPrice['pricePerDay']:.2f}"
        print(str)
        capture_print(str) 

    payloadStr_final = "\n".join(payloadStr)
    sendToSlack(payloadStr_final)

main()