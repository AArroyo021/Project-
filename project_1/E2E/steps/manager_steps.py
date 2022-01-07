import time

from behave import Given, When, Then
from selenium.webdriver.common.alert import Alert

@Given(u'The Manager is on the login page')
def step_impl(context):
    context.driver.get("file:///C:/Users/sofia/Desktop/Angel%20Work%20Folder/RevatureProjects-main/RevatureProjects-main/project_1/html_js_css/login_page.html")


@When(u'The Manager types in their correct Username and Password into the respected fields, selects Manager from the RadioButton options and then clicks Login Button')
def step_impl(context):
    context.project_1_manager_page.select_username_input().send_keys("Manager1")
    context.project_1_manager_page.select_password_input().send_keys("Pass1")
    context.project_1_manager_page.select_manager_radio().click()
    context.project_1_manager_page.select_login_button().click()

@Then(u'The Manager should be redirected to their reimbursement viewer page')
def step_impl(context):
    time.sleep(1)
    assert context.driver.title == "ManagerPage"

@Given(u'The Manager is on the reimbursement page')
def step_impl(context):
    context.driver.get("file:///C:/Users/sofia/Desktop/Angel%20Work%20Folder/RevatureProjects-main/RevatureProjects-main/project_1/html_js_css/login_page.html")
    context.project_1_manager_page.select_username_input().send_keys("Manager1")
    context.project_1_manager_page.select_password_input().send_keys("Pass1")
    context.project_1_manager_page.select_manager_radio().click()
    context.project_1_manager_page.select_login_button().click()

@When(u'The Manager clicks on the Pending Button')
def step_impl(context):
    context.project_1_manager_page.select_pending_button().click()
    time.sleep(.5)

@When(u'The Manager clicks on the Claim Number Button')
def step_impl(context):
    context.project_1_manager_page.select_claimNum8_button().click()
    time.sleep(.5)

@When(u'The Manager inputs Approve RadioButton for ClaimStatus and Manager Validation, and inputs their Manager Reasoning')
def step_impl(context):
    context.project_1_manager_page.select_claim_approve_status_radio().click()
    context.project_1_manager_page.select_manager_validation_approve_radio().click()
    context.project_1_manager_page.select_manager_reason_input().send_keys("Some random approval Selenium reason")
    time.sleep(.5)

@When(u'The Manager clicks the Update Button')
def step_impl(context):
    context.project_1_manager_page.select_update_button().click()
    time.sleep(.5)

@Then(u'The Manager gets a Approve Updated Successfully Alert and the page reloads')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert

@When(u'The Manager clicks on the Pending Button again')
def step_impl(context):
    time.sleep(1)
    alert = Alert(context.driver)
    alert.accept()
    time.sleep(1)
    context.project_1_manager_page.select_pending_button().click()
    time.sleep(1)

@When(u'The Manager clicks on the Claim Number Button again')
def step_impl(context):
    context.project_1_manager_page.select_claimNum28_button().click()
    time.sleep(1)

@When(u'The Manager inputs Deny RadioButton for ClaimStatus and Manager Validation, and inputs their Manager Reasoning')
def step_impl(context):
    context.project_1_manager_page.select_claim_deny_status_radio().click()
    context.project_1_manager_page.select_manager_validation_deny_radio().click()
    context.project_1_manager_page.select_manager_reason_input().send_keys("Some random rejection Selenium reason")
    time.sleep(.5)

@When(u'The Manager clicks the Update Button again')
def step_impl(context):
    context.project_1_manager_page.select_update_button().click()
    time.sleep(.5)

@Then(u'The Manager gets a Deny Updated Successfully Alert and the page reloads')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert

@When(u'The Manager clicks on the Completed Button')
def step_impl(context):
    alert = Alert(context.driver)
    alert.accept()
    context.project_1_manager_page.select_completed_button().click()

@Then(u'The Manager should have all the past reimbursement request decisions made with a Time stamp of the date Approved/Denied')
def step_impl(context):
    assert context.driver.title == "ManagerPage"

@When(u'The Manager clicks on the Statistics Button')
def step_impl(context):
    context.project_1_manager_page.select_statistics_button().click()

@Then(u'The Manager should have access to the statistics involving employee reimbursements')
def step_impl(context):
    assert context.driver.title == "ManagerPage"

# @Given(u'The Manager is on the Reimbursement Page')
# def step_impl(context):
#     context.driver.get("file:///C:/Users/sofia/Desktop/Angel%20Work%20Folder/RevatureProjects-main/RevatureProjects-main/project_1/html_js_css/login_page.html")
#     context.project_1_manager_page.select_username_input().send_keys("Manager1")
#     context.project_1_manager_page.select_password_input().send_keys("Pass1")
#     context.project_1_manager_page.select_manager_radio().click()
#     context.project_1_manager_page.select_login_button().click()

@When(u'The Manager clicks on the logout Button')
def step_impl(context):
    context.project_1_manager_page.select_logout_button().click()

@Then(u'The Manager should be redirected to the home page with their login information cleared')
def step_impl(context):
    assert context.driver.title == "Login"