import time, re, openpyxl
from selenium import webdriver

browser = webdriver.PhantomJS()
browser.set_window_size(1024, 768)	

wb = openpyxl.load_workbook("excel file goes here")
sheet = wb.get_sheet_by_name("excel sheet names goes here")
newFile = open("coordinates.txt", "a")

for i in range(1, number of rows in wb):
	date = sheet["A"+str(i+1)].value
	url = "https://www.google.com.jm/maps/search/"+date
	browser.get(url)
	time.sleep(1)
	string = browser.current_url
	string = re.sub('.*@','',string)
	string = string.split(",")
	newFile.write(string[0],string[1])
	newFile.write("\n")
	print(str(i+1)+".", string[0]+","+string[1])
