from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_home_page_title():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    assert "Refactoring" in driver.title
    driver.quit()


def test_footer_presence():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed()
    driver.quit()


def test_footer_links():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    footer_links = driver.find_elements(By.CSS_SELECTOR, "footer a")
    assert len(footer_links) > 5
    driver.quit()


def test_login_page_redirect():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    login_link = driver.find_element(By.LINK_TEXT, "Sign in")
    login_link.click()
    assert "login" in driver.current_url
    driver.quit()


def test_login_page_title():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/login")
    assert "Sign" in driver.title
    driver.quit()


def test_login_input_presence():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/login")
    login_input = driver.find_element(By.NAME, "email")
    assert login_input.is_displayed()
    driver.quit()


def test_password_input_presence():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/login")
    password_input = driver.find_element(By.NAME, "password")
    assert password_input.is_displayed()
    driver.quit()


def test_login_button_presence():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/login")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert login_button.is_displayed()
    driver.quit()


def test_unsuccessful_login():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/login")
    driver.find_element(By.NAME, "email").send_keys("wrong@email.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[2]/div/div/div[1]/div/div[2]/h3"))
    )
    assert "whoops!" in error_message.text.lower()
    driver.quit()


def test_password_reset_link():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/login")
    reset_link = driver.find_element(By.LINK_TEXT, "Forgot password?")
    reset_link.click()
    assert "reset" in driver.current_url
    driver.quit()


def test_shop_now_button():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru")
    store_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/nav/div/div/a"))
    )
    assert store_link.is_displayed()
    driver.quit()


def test_navigate_to_design_patterns():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru")
    design_patterns_link = driver.find_element(By.LINK_TEXT, "Design Patterns")
    design_patterns_link.click()
    assert "Design Patterns" in driver.title
    driver.quit()


def test_navigate_to_singleton():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/catalog")
    design_patterns_link = driver.find_element(By.LINK_TEXT, "Singleton")
    design_patterns_link.click()
    assert "Singleton" in driver.title
    driver.quit()


def test_navigate_to_proxy():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/catalog")
    design_patterns_link = driver.find_element(By.LINK_TEXT, "Proxy")
    design_patterns_link.click()
    assert "Proxy" in driver.title
    driver.quit()


def test_navigate_to_state():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/catalog")
    design_patterns_link = driver.find_element(By.LINK_TEXT, "State")
    design_patterns_link.click()
    assert "State" in driver.title
    driver.quit()


def test_navigate_to_abstract_factory_from_factory_method():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/factory-method")
    design_patterns_link = driver.find_element(By.LINK_TEXT, "Abstract Factory")
    design_patterns_link.click()
    assert "Abstract Factory" in driver.title
    driver.quit()


def test_navigate_to_creational_from_factory_method():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/factory-method")
    design_patterns_link = driver.find_element(By.LINK_TEXT, "Creational Patterns")
    design_patterns_link.click()
    assert "Creational Design Patterns" in driver.title
    driver.quit()


def test_navigate_to_python_example_from_factory_method():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/factory-method")
    design_patterns_link = driver.find_element(By.XPATH, "/html/body/div/main/div/div/article/div[12]/p/a[6]")
    design_patterns_link.click()
    assert "Factory Method in Python" in driver.title
    driver.quit()


def test_navigate_to_cpp_example_from_factory_method():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/factory-method")
    design_patterns_link = driver.find_element(By.XPATH, "/html/body/div/main/div/div/article/div[12]/p/a[2]")
    design_patterns_link.click()
    assert "Factory Method in C++" in driver.title
    driver.quit()


def test_code_examples_display_on_article_page():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/singleton/python/example")
    code_examples = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "code"))
    )
    assert len(code_examples) > 0
    driver.quit()


# NEW TEST CASES
def test_language_switch_to_spain():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    driver.find_element(By.CSS_SELECTOR, "button[id=dropdownLanguage]").click()
    driver.find_element(By.LINK_TEXT, "Español").click()
    WebDriverWait(driver, 5).until(EC.url_contains("/es"))
    assert "/es" in driver.current_url
    driver.quit()


def test_about_us_page_accessible():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    about_link = driver.find_element(By.LINK_TEXT, "About us")
    about_link.click()
    WebDriverWait(driver, 5).until(EC.title_contains("About"))
    assert "About" in driver.title
    driver.quit()


def test_subscribe_button():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    subscribe_button = driver.find_element(By.CSS_SELECTOR, "button[name=subscribe]")
    assert subscribe_button.is_displayed()
    driver.quit()


def test_navigation_menu_presence():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    nav_menu = driver.find_element(By.TAG_NAME, "nav")
    assert nav_menu.is_displayed()
    driver.quit()


def test_fb_banner_presence():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    fb_banner = driver.find_element(By.XPATH, "/html/body/div/main/div/div[2]/div[2]/div[2]")
    assert fb_banner.is_displayed()
    driver.quit()


def test_github_link():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    driver.find_element(By.XPATH, "/html/body/div/footer/div[1]/div/div/div[2]/ul/li[3]/a/i").click()
    WebDriverWait(driver, 5).until(EC.url_contains("github"))
    assert "https://github.com/RefactoringGuru" in driver.current_url
    driver.quit()


def test_contact_link_presense():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    contact_link = driver.find_element(By.LINK_TEXT, "Contact us")
    assert contact_link.is_displayed()
    driver.quit()


def test_contact_link_from_preseance():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    driver.find_element(By.XPATH, "/html/body/div[1]/footer/div[1]/div/div/div[1]/ul/li[6]/a").click()
    contact_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div')))
    assert contact_form.is_displayed()
    driver.quit()


def test_return_home():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/design-patterns/")
    driver.find_element(By.CLASS_NAME, "menu-brand").click()
    WebDriverWait(driver, 5).until(EC.url_contains("https://refactoring.guru"))
    assert "https://refactoring.guru/" == driver.current_url
    driver.quit()


def test_illustrations_author_page_link():
    driver = webdriver.Chrome()
    driver.get("https://refactoring.guru/")
    driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/div/div[1]/div[1]/a[2]/span").click()
    WebDriverWait(driver, 5).until(EC.url_contains("zhart"))
    assert "https://zhart.us/" == driver.current_url
    driver.quit()
