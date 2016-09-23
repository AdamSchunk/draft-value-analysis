from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#for year in range(2000,2016):
driver = webdriver.Firefox()
driver.get("http://www.drafthistory.com/index.php/years/" + str(2000))

for row in driver.find_elements_by_tag_name("tr")[2:4]:
	for value in row.find_elements_by_tag_name("td"):
		print value.text


print(element[5].get_attribute("value"))
