from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_dates = driver.find_elements_by_css_selector(".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n+1]={
        "time" : event_times[n].text,
        "name" : event_dates[n].text
    }
print(events)









driver.quit()