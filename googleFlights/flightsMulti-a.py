#2024/2/11 Flights
# selenium based driver to obtain flights 

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

def getSearchQueryBKK():
    title = "EDI-BKK-TKO"
    foundPrices = []
    innerFoundPrices = []

    daterangeAugSep = [{'year': 2024, 'month': 8, 'daysMax': 31}, {'year': 2024, 'month': 9, 'daysMax': 30}]
    daterangeOctNov = [{'year': 2024, 'month': 10, 'daysMax': 31}, {'year': 2024, 'month': 11, 'daysMax': 30}]
    incrementDaysRange = 10
    innerIncrementDaysRange = 15
    maxDaysInFirstCountryTotal = 21
    minDaysInFirstCountryEachSide = 3
    
    searchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAhIIL20vMDJtNzdyDAgDEggvbS8wZm4yZxooEgoyMDI0LTEwLTIwagwIAxIIL20vMGZuMmdyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": incrementDaysRange,
                     "dateRanges": daterangeAugSep,
                     "foundPrices": foundPrices},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wZm4yZxooEgoyMDI0LTEyLTI4agwIAxIIL20vMGZuMmdyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": incrementDaysRange,
                     "dateRanges": daterangeOctNov,
                     "foundPrices": foundPrices},
                     ]
    
    innerSearchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAxIIL20vMGZuMmdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTA5LTMwagwIAxIIL20vMDdkZmtyDAgDEggvbS8wZm4yZ0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": innerIncrementDaysRange,
                     "dateRanges": daterangeAugSep,
                     "foundPrices": innerFoundPrices},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTAxagwIAxIIL20vMGZuMmdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTExLTMwagwIAxIIL20vMDdkZmtyDAgDEggvbS8wZm4yZ0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": innerIncrementDaysRange,
                     "dateRanges": daterangeOctNov,
                     "foundPrices": innerFoundPrices},
    ]
    return {
        "title": title,
        "foundPrices": foundPrices,
        "innerFoundPrices": innerFoundPrices,
        "searchRanges": searchRanges,
        "innerSearchRanges": innerSearchRanges,
        "maxDaysInFirstCountryTotal": maxDaysInFirstCountryTotal,
        "minDaysInFirstCountryEachSide": minDaysInFirstCountryEachSide
        }

def getSearchQueryTPE():
    title = "EDI-TPE-TKO"
    foundPrices = []
    innerFoundPrices = []

    daterangeAugSep = [{'year': 2024, 'month': 8, 'daysMax': 31}, {'year': 2024, 'month': 9, 'daysMax': 30}]
    daterangeOctNov = [{'year': 2024, 'month': 10, 'daysMax': 31}, {'year': 2024, 'month': 11, 'daysMax': 30}]
    incrementDaysRange = 1
    innerIncrementDaysRange = 1
    maxDaysInFirstCountryTotal = 21
    minDaysInFirstCountryEachSide = 3
    
    searchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAhIIL20vMDJtNzdyDAgDEggvbS8wZnRreBooEgoyMDI0LTEwLTIwagwIAxIIL20vMGZ0a3hyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": incrementDaysRange,
                     "dateRanges": daterangeAugSep,
                     "foundPrices": foundPrices},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wZnRreBooEgoyMDI0LTEyLTI4agwIAxIIL20vMGZ0a3hyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": incrementDaysRange,
                     "dateRanges": daterangeOctNov,
                     "foundPrices": foundPrices},
                     ]
    
    innerSearchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAxIIL20vMGZ0a3hyDAgDEggvbS8wN2RmaxooEgoyMDI0LTA5LTMwagwIAxIIL20vMDdkZmtyDAgDEggvbS8wZnRreEABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": innerIncrementDaysRange,
                     "dateRanges": daterangeAugSep,
                     "foundPrices": innerFoundPrices},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTAxagwIAxIIL20vMGZ0a3hyDAgDEggvbS8wN2RmaxooEgoyMDI0LTExLTMwagwIAxIIL20vMDdkZmtyDAgDEggvbS8wZnRreEABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": innerIncrementDaysRange,
                     "dateRanges": daterangeOctNov,
                     "foundPrices": innerFoundPrices},
    ]
    return {
        "title": title,
        "foundPrices": foundPrices,
        "innerFoundPrices": innerFoundPrices,
        "searchRanges": searchRanges,
        "innerSearchRanges": innerSearchRanges,
        "maxDaysInFirstCountryTotal": maxDaysInFirstCountryTotal,
        "minDaysInFirstCountryEachSide": minDaysInFirstCountryEachSide
        }

def getSearchQuerySEOUL():
    title = "EDI-SEOUL-TKO"
    foundPrices = []
    innerFoundPrices = []

    daterangeAugSep = [{'year': 2024, 'month': 8, 'daysMax': 31}, {'year': 2024, 'month': 9, 'daysMax': 30}]
    daterangeOctNov = [{'year': 2024, 'month': 10, 'daysMax': 31}, {'year': 2024, 'month': 11, 'daysMax': 30}]
    incrementDaysRange = 10
    innerIncrementDaysRange = 15
    maxDaysInFirstCountryTotal = 21
    minDaysInFirstCountryEachSide = 3
    
    searchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAhIIL20vMDJtNzdyDAgDEggvbS8waHNxZhooEgoyMDI0LTEwLTIwagwIAxIIL20vMGhzcWZyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": incrementDaysRange,
                     "dateRanges": daterangeAugSep,
                     "foundPrices": foundPrices},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8waHNxZhooEgoyMDI0LTEyLTI4agwIAxIIL20vMGhzcWZyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": incrementDaysRange,
                     "dateRanges": daterangeOctNov,
                     "foundPrices": foundPrices},
                     ]
    
    innerSearchRanges = [
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTA4LTAxagwIAxIIL20vMGhzcWZyDAgDEggvbS8wN2RmaxooEgoyMDI0LTA5LTMwagwIAxIIL20vMDdkZmtyDAgDEggvbS8waHNxZkABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": innerIncrementDaysRange,
                     "dateRanges": daterangeAugSep,
                     "foundPrices": innerFoundPrices},
        {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTAxagwIAxIIL20vMGhzcWZyDAgDEggvbS8wN2RmaxooEgoyMDI0LTExLTMwagwIAxIIL20vMDdkZmtyDAgDEggvbS8waHNxZkABSAFwAYIBCwj___________8BmAEB",
                     "incrementDaysRange": innerIncrementDaysRange,
                     "dateRanges": daterangeOctNov,
                     "foundPrices": innerFoundPrices},
    ]
    return {
        "title": title,
        "foundPrices": foundPrices,
        "innerFoundPrices": innerFoundPrices,
        "searchRanges": searchRanges,
        "innerSearchRanges": innerSearchRanges,
        "maxDaysInFirstCountryTotal": maxDaysInFirstCountryTotal,
        "minDaysInFirstCountryEachSide": minDaysInFirstCountryEachSide
        }

def getAllSearchQueries():
    return [getSearchQuerySEOUL()]
    return [getSearchQueryBKK(), getSearchQueryTPE(), getSearchQuerySEOUL()]

def findPriceForDate(driver, dateStr): # 2024-10-01
    element = driver.find_element(By.XPATH, "//*[@data-iso='"+dateStr+"']")
    child_elements = element.find_elements(By.XPATH, ".//*[starts-with(text(), '£') or starts-with(text(), '$') or starts-with(text(), '€') or starts-with(text(), '¥')]") 
    priceStr = child_elements[0].text
    numberStr = priceStr[1:] 
    numberStr = numberStr.replace(",", "")
    numberStr = numberStr.replace("K", "000")
    number = float(numberStr)
    return number

def searchWithRange(oneSearchRange):
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1280, 720)

    
    url = oneSearchRange['url']
    incrementDaysRange = oneSearchRange['incrementDaysRange']
    dateRanges = oneSearchRange['dateRanges']
    foundPrices = oneSearchRange['foundPrices']

    results = []

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

    element = driver.find_element(By.XPATH, "//*[contains(text(), 'day trips')]")
    dayTripsStr = element.text
    firstNumberStr = dayTripsStr.split()[0]
    daysRange = int(firstNumberStr)
    print("")
    print(f"Searching {daysRange} days")

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
                    date_obj = datetime.strptime(dateStr, "%Y-%m-%d")  # Parse the string into a datetime object
                    startEpoch = int(date_obj.timestamp())  # Convert to epoch timestamp
                    oneDaySeconds = (60 * 60 * 24)
                    endEpoch = startEpoch + (daysRange * oneDaySeconds)
                    pricePerDay = oneVal / daysRange
                    print(f"{oneKey}: £{oneVal}: PPD:£{pricePerDay}")
                    results.append({'dayStr': oneKey, "price": oneVal, "pricePerDay": pricePerDay, "startEpoch": startEpoch, "endEpoch": endEpoch, "days":daysRange})
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
    foundPrices.extend(results)
    return results

def sendToSlack(payloadStr):
    #return
    webhook_url = 'https://hooks.slack.com/services/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'
    data = {'text': payloadStr}
    headers = {'Content-type': 'application/json'}

    response = requests.post(webhook_url, headers=headers, json=data) 

    if response.status_code == 200:
        print("Sent to Slack OK")
    else:
        print("Send to Slack Error: An error occurred:", response.text) 

def isFlightComboCompatible(oneFound, oneInnerFound, maxDaysInFirstCountryTotal, minDaysInFirstCountryEachSide):

    oneDay = (60 * 60 * 24)
    minRangeDays = oneDay * minDaysInFirstCountryEachSide
    innerStartsAfterFirst = oneInnerFound['startEpoch'] > (oneFound['startEpoch'] + minRangeDays)
    innerEndsBeforeFirst = oneInnerFound['endEpoch'] < (oneFound['endEpoch'] - minRangeDays)
    daysInFirstCountryTotalSec = (oneInnerFound['startEpoch'] - oneFound['startEpoch']) + (oneFound['endEpoch'] - oneInnerFound['endEpoch'])
    daysInFirstCountryTotal = daysInFirstCountryTotalSec / oneDay
    daysInFirstCountryOK = daysInFirstCountryTotal <= maxDaysInFirstCountryTotal
    
    return innerStartsAfterFirst and innerEndsBeforeFirst and daysInFirstCountryOK

def buildFlightCombo(title, oneFoundPrice, oneInnerFoundPrice):
    totalPrice = oneFoundPrice['price'] + oneInnerFoundPrice['price']
    totalDays = oneFoundPrice['days']
    pricePerDay = totalPrice / totalDays
    return {'title':title, 'flight':oneFoundPrice, 'innerFlight':oneInnerFoundPrice, 'pricePerDay':pricePerDay, 'totalDays':totalDays, 'totalPrice': totalPrice}

def buildFlightCombinations(title, foundPrices, innerFoundPrices, maxDaysInFirstCountryTotal, minDaysInFirstCountryEachSide):
    flightCombos = []
    for oneFoundPrice in foundPrices:
        for oneInnerFoundPrice in innerFoundPrices:
            if isFlightComboCompatible(oneFoundPrice, oneInnerFoundPrice, maxDaysInFirstCountryTotal, minDaysInFirstCountryEachSide):
                newFlightCombo = buildFlightCombo(title, oneFoundPrice, oneInnerFoundPrice)
                flightCombos.append(newFlightCombo)
    return flightCombos

def getFlightCombinationsForQuery(searchQuery):
    foundPrices = searchQuery['foundPrices']
    innerFoundPrices = searchQuery['innerFoundPrices']
    searchRanges = searchQuery['searchRanges']
    innerSearchRanges = searchQuery['innerSearchRanges']
    title = searchQuery['title']
    maxDaysInFirstCountryTotal = searchQuery['maxDaysInFirstCountryTotal']
    minDaysInFirstCountryEachSide = searchQuery['minDaysInFirstCountryEachSide']
    
    hThreads = []

    def SafeCall(oneSearchRange):
        try:
            searchWithRange(oneSearchRange)
        except Exception as e:
            print(f"\n\nError for {oneSearchRange}, {e}\n")


    for oneSearchRange in searchRanges:
        newThread = threading.Thread(target=SafeCall, args=(oneSearchRange,))
        hThreads.append(newThread)
        newThread.start()

    for hThread in hThreads:
        hThread.join()
    hThreads = []

    for oneSearchRange in innerSearchRanges:
        newThread = threading.Thread(target=SafeCall, args=(oneSearchRange,))
        hThreads.append(newThread)
        newThread.start()
    
    # wait for all threads to finish
    for hThread in hThreads:
        hThread.join()
    
    finalFlightCombinations = buildFlightCombinations(title, foundPrices, innerFoundPrices, maxDaysInFirstCountryTotal, minDaysInFirstCountryEachSide)
    print (f"Total Combinations = {len(foundPrices) * len(innerFoundPrices)}")
    print (f"Usable Combinations = {len(finalFlightCombinations)}")
    return finalFlightCombinations

def displayResults(finalFlightCombinations):
    
    def sortByInnerFlightTimeDescending(item):
        return -(item['innerFlight']['endEpoch'] - item['innerFlight']['startEpoch'])

    def sort_by_price(item):
        return item['totalPrice'], sortByInnerFlightTimeDescending(item)
    
    def sort_by_ppd(item):
        return item['pricePerDay'], sortByInnerFlightTimeDescending(item)
    
    finalFlightCombinations.sort(key=sort_by_ppd)  # Sort by ppd ascending
    topPrices = finalFlightCombinations

    payloadStr = []

    def capture_print(message):
        payloadStr.append(message)

    now = datetime.now()
    date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")  # Example: '2023-11-18 20:22:40'
    print(date_time_string)

    str = f"{date_time_string}\nTop 10 PPD\n"
    print (str)
    capture_print(str)

    def dispTop10(priceList):
        for topPrice in priceList[:10]: 
            def buildFlightStr(flight):
                date_obj = datetime.fromtimestamp(flight['startEpoch'])
                startDate = date_obj.strftime("%Y%m%d")
                days = flight['days']
                date_obj = datetime.fromtimestamp(flight['endEpoch'])
                endDate = date_obj.strftime("%m%d")
                price = flight['price']
                return f"{startDate}~{endDate}({days} days)£{price}"
            
            
            firstFlight = topPrice['flight']
            innerFlight = topPrice['innerFlight']
            
            oneDayEpoch = (60*60*24)
            firstSegmentDays = (innerFlight['startEpoch'] - firstFlight['startEpoch']) / oneDayEpoch
            finalSegmentDays = (firstFlight['endEpoch'] - innerFlight['endEpoch']) / oneDayEpoch
            buildDurationStr = f"first {firstSegmentDays} days, last {finalSegmentDays} days"
            title = topPrice['title']
            str = f"{title}: £{topPrice['totalPrice']}  PPD: £{topPrice['pricePerDay']:.2f} \n1) {buildFlightStr(firstFlight)}\n2) {buildFlightStr(innerFlight)}\n{buildDurationStr}\n"
            print(str); 
            capture_print(str)
    
    dispTop10(topPrices)
    
    finalFlightCombinations.sort(key=sort_by_price)  # Sort by price ascending
    topPrices = finalFlightCombinations

    str = "\nTop 10 prices\n"
    print (str)
    capture_print(str)

    dispTop10(topPrices)

    payloadStr_final = "\n".join(payloadStr)
    sendToSlack(payloadStr_final)

def main():
    
    allSearchQueries = getAllSearchQueries()

    finalFlightCombinations = []
    for searchQuery in allSearchQueries:
        time.sleep(2) #give it a sec to cool down on subsequent driver calls
        newFlightCombinations = getFlightCombinationsForQuery(searchQuery)
        finalFlightCombinations.extend(newFlightCombinations)

    # now sort and display the best flights
    displayResults(finalFlightCombinations)

main()