#2024/2/11 Flights
# selenium based driver to obtain flights 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def findPriceForDate(dateStr): # 2024-10-01
    element = driver.find_element(By.XPATH, "//*[@data-iso='"+dateStr+"']")
    child_elements = element.find_elements(By.XPATH, ".//*[starts-with(text(), '£')]")
    priceStr = child_elements[0].text
    numberStr = priceStr[1:] 
    number = float(numberStr)
    return number

def searchWithRange(oneSearchRange):
    url = oneSearchRange['url']
    daysRange = oneSearchRange['daysRange']
    dateRanges = oneSearchRange['dateRanges']
    results = []

    print("")
    print(f"Searching {daysRange} days")

    driver.get(url)

    time.sleep(2)

    try: 
        element = driver.find_element(By.XPATH, "//*[contains(@aria-label, 'Accept all')]")
        element.click()
    except:
        print("No Accept All button, probabaly already accepted")

    time.sleep(5)

    element = driver.find_element(By.XPATH, "//*[@data-value and starts-with(@data-value, '2024-10-')]")
    element.click()  # Example: Click on the Start month

    time.sleep(20)


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
                oneVal=findPriceForDate(dateStr)
                print(f"{oneKey}: £{oneVal}")
                results.append({'dayStr': oneKey, "price": oneVal})
            except:
                print(""+dateStr+": NO PRICE") 
    
    return results

def main():
    
    daterangeOctNov = [{'year': 2024, 'month': 10, 'daysMax': 31}, {'year': 2024, 'month': 11, 'daysMax': 30}]
    searchRanges = [{"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTEwagwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI1LTAxLTA1agwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 87,
                     "dateRanges": daterangeOctNov
                     }, 
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTEwagwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI1LTAxLTA0agwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 86,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI1LTAxLTA1agwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 88,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI1LTAxLTAyagwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 85,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI1LTAxLTAxagwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 84,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTEyLTMxagwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 83,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTEyLTMwagwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 82,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTEyLTI5agwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 81,
                     "dateRanges": daterangeOctNov},
                     {"url":"https://www.google.com/travel/flights/search?tfs=CBwQAhooEgoyMDI0LTEwLTA5agwIAhIIL20vMDJtNzdyDAgDEggvbS8wN2RmaxooEgoyMDI0LTEyLTI4agwIAxIIL20vMDdkZmtyDAgCEggvbS8wMm03N0ABSAFwAYIBCwj___________8BmAEB",
                     "daysRange": 80,
                     "dateRanges": daterangeOctNov},

                     ]

    foundPrices = []
    for oneSearchRange in searchRanges:
        try:
            oneSearchRangeResults = searchWithRange(oneSearchRange)
            foundPrices.extend(oneSearchRangeResults)
        except:
            print(f"\n\nError for {oneSearchRange['daysRange']}\n")

    
    def sort_by_price(item):
        return item['price']

    foundPrices.sort(key=sort_by_price)  # Sort by price ascending
    topPrices = foundPrices

    print ("\nTop 10\n")
    for topPrice in topPrices[:10]:
        print(f"{topPrice['dayStr']}: £{topPrice['price']}"); 

    input("Press Enter to END") 

main()