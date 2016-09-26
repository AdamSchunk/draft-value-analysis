import csv
import numpy as np
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.foxsports.com/nfl/san-francisco-49ers-team-roster?season=2016")

yearMenu = driver.find_element_by_id("wisbb_ddlseason")
teamMenu = driver.find_element_by_id("wisbb_ddlTeams")

teamURLs = [str(team.get_attribute("value"))[:-4] for team in teamMenu.find_elements_by_tag_name("option")]

for year in range(2000,2017):
	for teamURL in teamURLs:
		driver.get("http://www.foxsports.com" + teamURL + str(year))
		sleep(1)


		
