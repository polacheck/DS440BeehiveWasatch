from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

# def scrapeWasatch(street_num, street_name):

url = 'https://www.wasatch.utah.gov/Services/Information-Lookup-Services/Property-Tax-Information-Lookup/Current-Year-Property-Tax-Lookup'

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(url)

# find the address search box
prop_address_field = browser.find_element_by_css_selector('input[name="dnn$ctr1237$DynamicViews$dgSearchField$ctl05$SearchTextTextBox"]')
print(prop_address_field.get_attribute('id'))

# Enter addresses
prop_address_field.send_keys('8686 E STRAWBERRY')  # using an example property here
# prop_address_field.send_keys(street_name)

# Click on the Submit Button
search_button = browser.find_element_by_css_selector('input[name="dnn$ctr1237$DynamicViews$SearchImageButton"]')
print(prop_address_field.get_attribute('name'))
ActionChains(browser).click(search_button).perform()

#Works up until here

#account_row = browser.find_element_by_link_text("View Details")
account_row = browser.find_element_by_link_text("View Details")
#account_row = browser.findElement(By.xpath('//*[@id="dnn_ctr1237_DynamicViews_dlReport"]/tbody/tr[2]/td[1]/p/a'));
#account_row = browser.find_element_by_css_selector('input.dnn_ctr1237_DynamicViews_dlReport')
#print(account_row.get_attribute('innerHTML'))
ActionChains(browser).click(account_row).perform()

