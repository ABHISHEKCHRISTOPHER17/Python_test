import time

from behave import *

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Helper.base import generate_random

from features.steps.uac import step_uac

from utils.config_reader import get_config

from Logs import log_files
 
logger = log_files.get_logs()
 
 
@given('Naviagte to user access control')

def step_user_access_control(context):

    step_uac(context)
 
 
@when('The user lands on user access control page')

def step_verify_uac_page(context):

    WebDriverWait(context.driver, 30).until(

        EC.presence_of_element_located((By.XPATH, "//span[text()='User Access Control' and @class='ant-typography !font-semibold text-regal-blue text-2xl css-1ybnqqa']"))

    )
 
 
@then('Verify the assertion of user tab')

def step_verify_user_tab(context):

    try:

        user_tab = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH, "//p[text()='Users' and @class=' !mb-0']"))

        )

        assert user_tab, "User tab element not found"
 
    except Exception as e:

        assert False, "Element not found within given time"
 
 
@step('Verify the assertion of roles tab')

def step_verify_roles_tab(context):

    try:

        roles_tab = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH, "//p[text()='Roles' and @class='!mb-0 ']"))

        )

        assert roles_tab, "Roles tab element not found"
 
    except Exception as e:

        assert False, "Element not found within the given time"
 
 
@step('Verify the assertion of user name')

def step_verify_user_name(context):

    try:

        user_name = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH, "//span[@class='ant-typography font-normal text-sm text-[#637381] leading-[22px] whitespace-nowrap css-1ybnqqa']"))

        )

        user_name_text = user_name.text

        logger.info(f"The logged in user is {user_name_text}")

        assert user_name, "User name element not found"
 
    except Exception as e:

        assert False, "Element not found within the given time"
 
 
@step('Verify the assertion of user role')

def step_verify_user_role(context):

    try:

        user_role = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH, "//span[@class='ant-typography ant-dropdown-trigger text-xs text-[#8899A8] !leading-[20px] font-normal whitespace-nowrap flex flex-row items-center cursor-pointer css-1ybnqqa']"))

        )

        user_name_text = user_role.text

        logger.info(f"The logged in user role is {user_name_text}")

        assert user_role, "User role element not found"
 
    except Exception as e:

        assert False, "Element not found within the given time"
 
 
@step('Verify the assertion of users table')

def step_verify_users_table(context):

    try:

        users_table = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH,

                                            "//main[@class='ant-layout-content bg-white rounded-md shadow-brandShadow p-3  css-1ybnqqa']"))

        )
 
        assert users_table, "Users table element not found"
 
    except Exception as e:

        assert False, "Element not found within the given time"
 
 
@step('Verify the assertion of add user button')

def step_verify_add_user_btn(context):

    try:

        add_user_btn = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH, "//button[@class='ant-btn css-1ybnqqa ant-btn-default app-btn-primary !h-8 hover:!h-8']"))

        )
 
        assert add_user_btn, "User role element not found"
 
    except Exception as e:

        assert False, "Element not found within the given time"
 
 
@step('Verify the assertion of policies footer')

def step_policies_footer(context):

    try:

        policies_footer = WebDriverWait(context.driver, 30).until(

            EC.presence_of_element_located((By.XPATH, "//button[@class='ant-btn css-1ybnqqa ant-btn-default app-btn-primary !h-8 hover:!h-8']"))

        )
 
        assert policies_footer, "User role element not found"
 
    except Exception as e:

        assert False, "Element not found within the given time"
 
 
 
 
