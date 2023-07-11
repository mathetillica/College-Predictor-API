from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = "C:/Users/HP/Desktop/Project/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

s=Service(driver_path)
option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(service=s, options=option)
driver.get("https://cutoffs.iitr.ac.in/")

Serial = []
Year = []
Institute = []
Program = []
Duration = []
Degree = []
Category = []
Pool = []
Opening = []
Closing = []
for j in range(57): 
    row = driver.find_elements("tag name", 'tr')
    i=0
    n=52
    if(j==56): n=5
    for item in row:
        i=i+1
        if (i==1):
            continue
        if(i==n):
            break
        else:
            Serial.append(item.find_element("xpath", './td[1]').text)
            print(Serial[-1])
            Year.append(item.find_element("xpath", './td[2]').text)
            Institute.append(item.find_element("xpath", './td[3]').text)
            Program.append(item.find_element("xpath", './td[4]').text)
            Duration.append(item.find_element("xpath", './td[5]').text)
            Degree.append(item.find_element("xpath", './td[6]').text)
            Category.append(item.find_element("xpath", './td[7]').text)
            Pool.append(item.find_element("xpath", './td[8]').text)
            Opening.append(item.find_element("xpath", './td[9]').text)
            Closing.append(item.find_element("xpath", './td[10]').text)
    element = driver.find_element("xpath", '//*[@id="scroll-ref"]/table/tfoot/tr/th/div/a[10]/i')
    driver.execute_script("arguments[0].click();", element)
driver.quit()
import pandas as pd
df=pd.DataFrame({'Sr.':Serial, 
              'Year':Year, 
              'Institute':Institute,
              'Program':Program,
              'Duration':Duration,
              'Degree':Degree,
              'Category':Category,
              'Pool':Pool,
              'Opening':Opening,
              'Closing':Closing})
df.to_csv('scraped_data.csv', index=False)
print(df)
