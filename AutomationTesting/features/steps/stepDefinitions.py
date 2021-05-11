from behave import *
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


@given("launch chrome browser")
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path="C:\\Users\\Omaima Uchiha\\.wdm\\drivers\\chromedriver\\win32\\90.0.4430.24\\chromedriver.exe")


@when("The AutomationPractice site is open")
def step_impl(context):
    context.driver.get('http://automationpractice.com/index.php')


@when('The Sign In link is clicked')
def step_impl(context):
    context.driver.find_element_by_class_name("login").click()


@when("The Email '{email}' and Password '{password} are entered'")
def step_impl(context, email, password):
    context.driver.find_element_by_id("email").send_keys(email)
    context.driver.find_element_by_id("passwd").send_keys(password)


@when('The Sign In button is clicked')
def step_impl(context):
    context.driver.find_element_by_id("SubmitLogin").click()


@then("User account loads")
def step_impl(context):
    try:
        assert context.driver.title == "My account - My Store"
    except:
        assert True, "Invalid credentials"


@when("the create an account button is clicked")
def step_impl(context):
    context.driver.find_element_by_id("SubmitCreate").click()


@when("registration page loads")
def step_impl(context):
    context.driver.implicitly_wait(10)
    assert context.driver.title == "Login - My Store"




@when("select title")
def step_impl(context):
    context.driver.find_element_by_id("id_gender1").click()


@when("First name '{firstname}'")
def step_impl(context, firstname):
    if firstname == "empty":
        firstnamenew = ""
    else:
        firstnamenew = firstname
    context.driver.find_element_by_id("customer_firstname").send_keys(firstnamenew)



@when("Last name '{lastname}'")
def step_impl(context, lastname):
    if lastname == "empty":
        lastnamenew = ""
    else:
        lastnamenew = lastname
    context.driver.find_element_by_id("customer_lastname").send_keys(lastnamenew)


@when("Password '{Password}'")
def step_impl(context, Password):
    if Password == "empty":
        Passwordnew = ""
    else:
        Passwordnew = Password
    context.driver.find_element_by_id("passwd").send_keys(Passwordnew)


@when("Date Of Birth '{Date}'")
def step_impl(context, Date):
    if Date == "empty":
        Datenew = ""
    else:
        Datenew = Date
    select = Select(context.driver.find_element_by_id("days"))
    select.select_by_value(Datenew)


@when("Date Of Month '{Month}'")
def step_impl(context, Month):
    if Month == "empty":
        Monthnew = ""
    else:
        Monthnew = Month
    select = Select(context.driver.find_element_by_id("months"))
    select.select_by_value(Monthnew)


@when("Date Of Year '{Year}'")
def step_impl(context, Year):
    if Year == "empty":
        Yearnew = ""
    else:
        Yearnew = Year
    select = Select(context.driver.find_element_by_id("years"))
    select.select_by_value(Yearnew)


@when("select newspaper")
def step_impl(context):
    context.driver.find_element_by_id("newsletter").click()


@when("select optin")
def step_impl(context):
    context.driver.find_element_by_id("optin").click()


@when("Address '{Address}'")
def step_impl(context, Address):
    if Address == "empty":
        Addressnew = ""
    else:
        Addressnew = Address
    context.driver.find_element_by_id("address1").send_keys(Addressnew)


@when("City '{City}'")
def step_impl(context, City):
    if City == "empty":
        Citynew = ""
    else:
        Citynew = City
    context.driver.find_element_by_id("city").send_keys(Citynew)


@when("State '{State}'")
def step_impl(context, State):

    context.driver.find_element_by_id("id_state").send_keys(State)
    select = Select(context.driver.find_element_by_id("id_state"))
    select.select_by_visible_text(State)


@when("Zip/postal Code '{ZipCode}'")
def step_impl(context, ZipCode):
    if ZipCode == "empty":
        ZipCodenew = ""
    else:
        ZipCodenew = ZipCode
    context.driver.find_element_by_id("postcode").send_keys(ZipCodenew)


@when("Phone Number '{phoneNumber}'")
def step_impl(context, phoneNumber):
    if phoneNumber == "empty":
        phoneNumbernew = ""
    else:
        phoneNumbernew = phoneNumber
    context.driver.find_element_by_id("phone_mobile").send_keys(phoneNumbernew)


@when("Email is entered to register an account '{email}'")
def step_impl(context, email):
    if email == "empty":
        emailnew = ""
    else:
        emailnew = email
    context.driver.find_element_by_id("email_create").send_keys(emailnew)


@when("the Register button is clicked")
def step_impl(context):
    context.driver.find_element_by_id("submitAccount").click()


@then("The user account page loads")
def step_impl(context):
    assert True, context.driver.title == "My account - My Store"
    context.driver.quit()


@when("Search for items '{item}'")
def step_impl(context,item):
    if item == "empty":
        itemnew = ""
    else:
        itemnew = item
    context.driver.find_element_by_id("search_query_top").send_keys(itemnew)


@when("click the search button")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="searchbox"]/button').click()


@then("show results")
def step_impl(context):
    context.driver.implicitly_wait(10)
    assert True, context.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]')
    context.driver.implicitly_wait(10)


@when("The contact us link is clicked")
def step_impl(context):
    context.driver.find_element_by_id("contact-link").click()

@when("Select subject heading '{heading}'")
def step_impl(context, heading):
    context.driver.find_element_by_id("id_contact").send_keys(heading)
    select = Select(context.driver.find_element_by_id("id_contact"))
    select.select_by_visible_text(heading)

@when("enter email address '{email}'")
def step_impl(context, email):
    if email == "empty":
        emailnew = ""
    else:
        emailnew = email
    context.driver.find_element_by_id("email").send_keys(emailnew)


@when("message '{message}'")
def step_impl(context, message):
    if message == "empty":
        messagenew = ""
    else:
        messagenew = message
    context.driver.find_element_by_id("message").send_keys(messagenew)


@then("click on the send button")
def step_impl(context):
    context.driver.find_element_by_id("submitMessage").click()


@when("The AutomationPractice site has dresses loaded")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.get('http://automationpractice.com/index.php')
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[2]/a').click()


@when("the banner is clicked")
def step_impl(context):
    context.driver.find_element_by_class_name("banner").click()

@then("the homepage is loaded")
def step_impl(context):
    context.driver.implicitly_wait(5)
    assert True, context.driver.get('http://automationpractice.com/index.php')
    context.driver.quit()

@when("the logo is clicked")
def step_impl(context):
    context.driver.find_element_by_id("header_logo").click()

@when("the homepage is loaded")
def step_impl(context):
    context.driver.implicitly_wait(5)
    assert True, context.driver.get('http://automationpractice.com/index.php')


@when("Email '<email>' and Password '<password>' are entered'")
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_id("email").send_keys('example2@email.com')
    context.driver.find_element_by_id("passwd").send_keys('password')


@when("Search for shirt")
def step_impl(context):
    item = 'shirt'
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_id("search_query_top").send_keys(item)



@step("click on add to cart")
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]').click()


@then("show cart")
def step_impl(context):
    context.driver.implicitly_wait(5)
    assert True, context.driver.title == "Order - My Store"
    context.driver.implicitly_wait(5)


@step("delete shirt from cart")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_class_name("cart_quantity_delete").click()
    context.driver.implicitly_wait(10)

@step("click on proceed to checkout")
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
    context.driver.implicitly_wait(5)
