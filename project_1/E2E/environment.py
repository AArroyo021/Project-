from behave.runner import Context
from selenium import webdriver
from page_object_model.project_1_employee_page import Project1EmployeePom
from page_object_model.project_1_manager_page import Project1ManagerPom


def before_all(context: Context):
    context.driver = webdriver.Chrome("project_1/E2E/chromedriver.exe")
    context.project_1_employee_page = Project1EmployeePom(context.driver)
    context.project_1_manager_page = Project1ManagerPom(context.driver)
    context.driver.implicitly_wait(4)


def after_all(context: Context):
    context.driver.quit()