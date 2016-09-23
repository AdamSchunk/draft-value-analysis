import csv
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
for year in range(2000,2017):
	driver.get("http://www.drafthistory.com/index.php/years/" + str(year))
	csvFile = open("draft_order_"+str(year)+".csv", 'wb')

	for row in driver.find_elements_by_tag_name("tr")[2:-9]:
		values = [str(x.text) for x in row.find_elements_by_tag_name("td")]
		print(values)
		writer = csv.writer(csvFile)
		writer.writerow(values)
