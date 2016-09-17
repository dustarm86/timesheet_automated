from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# opens Firefox and goes to the CMS login page
browser = webdriver.Firefox()
browser.get('https://www.cmsonline.info/User/Account/LogOn?https://www.cmsonline.info/')
#ask_users_username = raw_input("Enter your username for CMS\n")
#ask_users_password = raw_input("Enter your password for CMS\n")

# enter UN and PW into CMS then clicks login button
username = browser.find_element_by_xpath(".//*[@id='UserName']")
username.send_keys('YOURLOGIN')
pw = browser.find_element_by_xpath(".//*[@id='Password']")
pw.send_keys('YOURPASSWORD')
login_button = browser.find_element_by_xpath(".//*[@id='btnOk']").click()

# brings browser to submit timesheet page and clicks on your contract number
browser.get('https://www.cmsonline.info/Timesheet/SubmitTimesheet')
contract_number = browser.find_element_by_xpath(".//*[@id='YOURCONTRACT#']").click()

# enters hours for monday
monday_start_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_0__StartHour']")
monday_start_hours.send_keys('9')
monday_start_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_0__StartMinute']")
monday_start_mins.send_keys('00')
monday_finish_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_0__FinishHour']")
monday_finish_hours.send_keys('17')
monday_finish_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_0__FinishMinute']")
monday_finish_mins.send_keys('00')

# enters hours for tuesday
tuesday_start_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_1__StartHour']")
tuesday_start_hours.send_keys('9')
tuesday_start_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_1__StartMinute']")
tuesday_start_mins.send_keys('00')
tuesday_finish_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_1__FinishHour']")
tuesday_finish_hours.send_keys('17')
tuesday_finish_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_1__FinishMinute']")
tuesday_finish_mins.send_keys('00')

# enters hours for wednesday
wednesday_start_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_2__StartHour']")
wednesday_start_hours.send_keys('9')
wednesday_start_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_2__StartMinute']")
wednesday_start_mins.send_keys('00')
wednesday_finish_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_2__FinishHour']")
wednesday_finish_hours.send_keys('17')
wednesday_finish_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_2__FinishMinute']")
wednesday_finish_mins.send_keys('00')

# enters hours for thursday
thursday_start_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_3__StartHour']")
thursday_start_hours.send_keys('9')
thursday_start_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_3__StartMinute']")
thursday_start_mins.send_keys('00')
thursday_finish_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_3__FinishHour']")
thursday_finish_hours.send_keys("17")
thursday_finish_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_3__FinishMinute']")
thursday_finish_mins.send_keys('00')

# enters hours for friday
friday_start_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_4__StartHour']")
friday_start_hours.send_keys('9')
friday_start_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_4__StartMinute']")
friday_start_mins.send_keys('00')
friday_finish_hours = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_4__FinishHour']")
friday_finish_hours.send_keys('17')
friday_finish_mins = browser.find_element_by_xpath(".//*[@id='TimesheetUkWeeklyOnlineModel_TimesheetDetailModels_4__FinishMinute']")
friday_finish_mins.send_keys('00')

# clicks submit button
submit_button = browser.find_element_by_xpath(".//*[@id='btnSubmit']").click()
time.sleep(30)

# opens firefox to comcast's salesforce timesheet
browser.get("https://entssoext.cable.comcast.com/siteminderagent/forms/DMZLoginForm/login.fcc?TYPE=33554433&REALMOID=06-000a8bae-eb31-1347-a4ed-7b2a93bff065&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-Go2vzlZxjIj3vn9tVz%2fPTaj%2fQQCqjAqcXeiruDYzOwimCfzuqPBxKShNc2bj8UqW&TARGET=-SM-https%3a%2f%2fentssoext%2ecable%2ecomcast%2ecom%2fforecast%2f")

# enters comcast's enterprise username and pw and clicks sign in button
enterprise_un = browser.find_element_by_xpath(".//*[@id='username']")
enterprise_un.send_keys("YOURLOGIN")
enterprise_pw = browser.find_element_by_xpath(".//*[@id='password']")
enterprise_pw.send_keys("YOURPASSWORD")
enterprise_signin_button = browser.find_element_by_xpath("html/body/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[1]/td/form/table/tbody/tr[4]/td[2]/p/input").click()

# open weekly capitalization form for contractor
select_name_capform = browser.find_element_by_xpath(".//*[@id='theTable1']/tbody/tr/td[2]/a").click()

# enter hours into salesforce for monday-friday
monday_hours = browser.find_element_by_xpath(".//*[@id='pgTSEntry:theForm:pgTS:childList:tableid:0:day1']")
monday_hours.send_keys('8')
tuesday_hours = browser.find_element_by_xpath(".//*[@id='pgTSEntry:theForm:pgTS:childList:tableid:0:day2']")
tuesday_hours.send_keys('8')
wednesday_hours = browser.find_element_by_xpath(".//*[@id='pgTSEntry:theForm:pgTS:childList:tableid:0:day3']")
wednesday_hours.send_keys('8')
thursday_hours = browser.find_element_by_xpath(".//*[@id='pgTSEntry:theForm:pgTS:childList:tableid:0:day4']")
thursday_hours.send_keys('8')
friday_hours = browser.find_element_by_xpath(".//*[@id='pgTSEntry:theForm:pgTS:childList:tableid:0:day5']")
friday_hours.send_keys('8')
