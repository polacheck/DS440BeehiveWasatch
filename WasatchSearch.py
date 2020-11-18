from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


# def scrapeWasatch(street_address): # uncomment here to create the function for Wasatch County. street

street_address = '8686 E STRAWBERRY' # delete this line if you uncomment the function, it is just a test property

url = 'https://www.wasatch.utah.gov/Services/Information-Lookup-Services/Property-Tax-Information-Lookup/Current-Year-Property-Tax-Lookup'

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(url)

# find the address search box
prop_address_field = browser.find_element_by_css_selector('input[name="dnn$ctr1237$DynamicViews$dgSearchField$ctl05$SearchTextTextBox"]')
print(prop_address_field.get_attribute('id'))

# Enter addresses
prop_address_field.send_keys(street_address) # use this

# Click on the Submit Button
search_button = browser.find_element_by_css_selector('input[name="dnn$ctr1237$DynamicViews$SearchImageButton"]')
print(prop_address_field.get_attribute('name'))
ActionChains(browser).click(search_button).perform()

# wait for link to appear
import time
time.sleep(0.5)

# click link
account_row = browser.find_element_by_css_selector('table#dnn_ctr1237_DynamicViews_dlReport tbody tr td p a')
print(account_row)
ActionChains(browser).click(account_row).perform()

time.sleep(0.5)

# From here it looks for all possible information

parcel_number = browser.find_element_by_xpath('//table/tbody/tr[3]/td[2]').get_attribute("textContent")
serial_number = browser.find_element_by_xpath('//table/tbody/tr[4]/td[2]').get_attribute("textContent")
entry_number = browser.find_element_by_xpath('//table/tbody/tr[5]/td[2]').get_attribute("textContent")
owner_name = browser.find_element_by_xpath('//table/tbody/tr[6]/td[2]').get_attribute("textContent")
mailing_address = browser.find_element_by_xpath('//table/tbody/tr[7]/td[2]').get_attribute("textContent")
tax_district = browser.find_element_by_xpath('//table/tbody/tr[8]/td[2]').get_attribute("textContent")
tax_district_rate = browser.find_element_by_xpath('//table/tbody/tr[9]/td[2]').get_attribute("textContent")
acreage = browser.find_element_by_xpath('//table/tbody/tr[10]/td[2]').get_attribute("textContent")
market_value = browser.find_element_by_xpath('//table/tbody/tr[11]/td[2]').get_attribute("textContent")
taxable_value = browser.find_element_by_xpath('//table/tbody/tr[12]/td[2]').get_attribute("textContent")
land_value = browser.find_element_by_xpath('//table/tbody/tr[13]/td[2]').get_attribute("textContent")
improvements_value = browser.find_element_by_xpath('//table/tbody/tr[14]/td[2]').get_attribute("textContent")
tax_charge = browser.find_element_by_xpath('//table/tbody/tr[15]/td[2]').get_attribute("textContent")
penalties_charged = browser.find_element_by_xpath('//table/tbody/tr[16]/td[2]').get_attribute("textContent")
special_charged = browser.find_element_by_xpath('//table/tbody/tr[17]/td[2]').get_attribute("textContent")
tax_payments = browser.find_element_by_xpath('//table/tbody/tr[18]/td[2]').get_attribute("textContent")
taxes_abated = browser.find_element_by_xpath('//table/tbody/tr[19]/td[2]').get_attribute("textContent")
taxes_balance_due = browser.find_element_by_xpath('//table/tbody/tr[20]/td[2]').get_attribute("textContent")
escrow_processing_company = browser.find_element_by_xpath('//table/tbody/tr[21]/td[2]').get_attribute("textContent")
property_address = browser.find_element_by_xpath('//table/tbody/tr[22]/td[2]').get_attribute("textContent")
square_footage = browser.find_element_by_xpath('//table/tbody/tr[23]/td[2]').get_attribute("textContent")
year_built = browser.find_element_by_xpath('//table/tbody/tr[24]/td[2]').get_attribute("textContent")
back_tax_approx_amount = browser.find_element_by_xpath('//table/tbody/tr[25]/td[2]').get_attribute("textContent")
review_date = browser.find_element_by_xpath('//table/tbody/tr[26]/td[2]').get_attribute("textContent")
brief_legal_taxing_description = browser.find_element_by_xpath('//table/tbody/tr[27]/td[2]').get_attribute("textContent")