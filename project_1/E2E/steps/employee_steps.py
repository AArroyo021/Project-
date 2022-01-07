import time

from behave import Given, When, Then
from selenium.webdriver.common.alert import Alert


@Given(u'The Employee is on the login page')
def step_impl(context):
    context.driver.get("file:///C:/Users/sofia/Desktop/Angel%20Work%20Folder/RevatureProjects-main/RevatureProjects-main/project_1/html_js_css/login_page.html")

@When(u'The Employee types in their correct Username and Password into the respected fields and clicks Login Button')
def step_impl(context):
    context.project_1_employee_page.select_username_input().send_keys("Employee1")
    context.project_1_employee_page.select_password_input().send_keys("PasswordABC")
    context.project_1_employee_page.select_login_button().click()

@Then(u'The Employee should be redirected to their reimbursements page')
def step_impl(context):
    time.sleep(1)
    assert context.driver.title == "EmployeePage"

@Given(u'The Employee is on the Reimbursement Page')
def step_impl(context):
    context.driver.get("file:///C:/Users/sofia/Desktop/Angel%20Work%20Folder/RevatureProjects-main/RevatureProjects-main/project_1/html_js_css/login_page.html")
    context.project_1_employee_page.select_username_input().send_keys("Employee1")
    context.project_1_employee_page.select_password_input().send_keys("PasswordABC")
    context.project_1_employee_page.select_login_button().click()
    time.sleep(1)

@When(u'The Employee clicks on the Create A Reimbursement Button')
def step_impl(context):
    context.project_1_employee_page.select_create_reimbursement_button().click()
    time.sleep(1)

@When(u'The Employee inputs their reasoning for a reimbursement')
def step_impl(context):
    context.project_1_employee_page.select_reason_input().send_keys("Selenium sends a reason")

@When(u'The Employee inputs a valid claim amount')
def step_impl(context):
    context.project_1_employee_page.select_amount_input().send_keys("711")

@When(u'The Employee clicks the Create Button')
def step_impl(context):
    context.project_1_employee_page.select_create_button().click()
    time.sleep(1)

@Then(u'The Employee gets a Reimbursement Created Alert')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert

@When(u'The Employee clicks on the Completed Reimbursements Button')
def step_impl(context):
    #clearing an alert
    alert = Alert(context.driver)
    alert.accept()
    context.project_1_employee_page.select_completed_reimbursement_button().click()
    time.sleep(2)

@Then(u'The Employee should have all their past reimbursement request with all the information pertaining them appear')
def step_impl(context):
    assert context.driver.title == "EmployeePage"

@When(u'The Employee clicks on the logout Button')
def step_impl(context):
    context.project_1_employee_page.select_logout_button().click()

@Then(u'The Employee should be redirected to the home page with their login information cleared')
def step_impl(context):
    assert context.driver.title == "Login"