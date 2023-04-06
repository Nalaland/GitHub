from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 20)

url = "https://testautomationpractice.blogspot.com/"
first = "Janko"
last = "Hrasko"
phone = "+421908222555"
country = "Slovakia"
city = "Kosice"
email = "smartuser@gmail.com"

driver.get(url)
cookie = driver.find_element(By.XPATH, "//*[@id='cookieChoiceDismiss']")
cookie.click()
#driver.maximize_window()#

'''FORMULAR'''
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="frame-one1434677811"]')))
first_name = driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-1']")
first_name.send_keys(first)
last_name = driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']")
last_name.send_keys(last)
mobile_phone = driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-3']")
mobile_phone.send_keys(phone)
Country = driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-4']")
Country.send_keys(country)
City = driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-5']")
City.send_keys(city)
Email_address = driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-6']")
Email_address.send_keys(email)

'''GENDER'''
Gender = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']")
Gender.click()


'''DNI'''
Tuesday = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_2']")
Tuesday.click()
Wednesday = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_3']")
Wednesday.click()
Thursday = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_4']")
Thursday.click()

'''DROPDOWN'''
dropdown = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))
dropdown.select_by_value("Radio-1")

'''FILES'''
file = driver.find_element(By.XPATH, "//input[@id='RESULT_FileUpload-10']")
file.send_keys(r"C:\Users\Michaela\Desktop\akademy\Akademka.txt")

driver.switch_to.default_content()


'''ALERT'''
alert_cm = driver.find_element(By.XPATH, "//button[@onclick='myFunction()']")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='myFunction()']")))
alert_cm.click()
alert = driver.switch_to.alert
alert.accept()

'''DATE'''
date = driver.find_element(By.XPATH, "//input[@class='hasDatepicker']")
date.click()
current_day = driver.find_element(By.XPATH, "//td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']")
current_day.click()

'''SELECT MENU'''
s_number = Select(driver.find_element(By.XPATH, "//select[@id='number']"))
s_number.select_by_visible_text("4")
s_animal = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
s_animal.select_by_visible_text("Big Baby Cat")

'''DOUBLE CLICK'''
copy_text = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")
action = ActionChains(driver)
action.double_click(copy_text).perform()

'''DRAG AND DROP'''
drag = driver.find_element(By.XPATH, "//div[@id='draggable']")
drop = driver.find_element(By.XPATH, "//div[@id='droppable']")
d_a_d = ActionChains(driver)
d_a_d.click_and_hold(drag)
d_a_d.move_to_element(drop)
d_a_d.release(drop)
