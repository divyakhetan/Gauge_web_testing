from step_impl.utils.driver import Driver
from getgauge.python import step
from getgauge.python import step, before_scenario, Messages
import time
from selenium.webdriver.common.keys import Keys


vowels = ["a", "e", "i", "o", "u"]


def number_of_vowels(word):
    return len([elem for elem in list(word) if elem in vowels])


# --------------------------
# Gauge step implementations
# --------------------------


@step("Navigate to <url>.") 
def assert_navigate_to(url):
    # assert (url == "https://www.google.com/")
    # Driver.driver.set_page_load_timeout("10")
    Driver.driver.get(url)
    time.sleep(20)
    Driver.close()

@step("Login to <url>.") 
def assert_login_to(url):
    Driver.driver.get(url)
    Driver.driver.find_element_by_name("email").send_keys("divyakhetan1209@gmail.com")
    Driver.driver.find_element_by_name("pass").send_keys("shreyakhetan1")
    Driver.driver.find_element_by_id("u_0_b").click()
    time.sleep(4)
    Driver.driver.close()

@step("Search in <url>.") 
def assert_search_to(url):
    Driver.driver.get(url)
    Driver.driver.find_element_by_name("email").send_keys("divyakhetan1209@gmail.com")
    Driver.driver.find_element_by_name("pass").send_keys("shreyakhetan1")
    Driver.driver.find_element_by_id("u_0_b").click()
    Driver.driver.find_element_by_name("q").send_keys("Prafful Javare")
    Driver.driver.find_element_by_class_name("_3ixn").click()
    # Driver.driver.find_element_by_css_selector("[aria-label= 'Search']").click()
    time.sleep(4)
    Driver.driver.close()


@step("Message in <url>.") 
def assert_msg_to(url):
    Driver.driver.get(url)
    Driver.driver.find_element_by_name("email").send_keys("divyakhetan1209@gmail.com")
    Driver.driver.find_element_by_name("pass").send_keys("shreyakhetan1")
    Driver.driver.find_element_by_id("u_0_b").click()
    Driver.driver.find_element_by_class_name("_7jby").click()
    Driver.driver.find_element_by_class_name("_55lr").click()
    # Driver.driver.find_element_by_class_name("_552h").send_keys("Automated")
    # Driver.driver.find_element_by_css_selector("[aria-label= 'Search']").click()
    time.sleep(4)
    Driver.driver.close()


@step("Add to Story in <url>.") 
def assert_story_in(url):
    Driver.driver.get(url)
    Driver.driver.find_element_by_name("email").send_keys("divyakhetan1209@gmail.com")
    Driver.driver.find_element_by_name("pass").send_keys("shreyakhetan1")
    Driver.driver.find_element_by_id("u_0_b").click()
    Driver.driver.find_element_by_class_name("_7h4p").click()
    time.sleep(4)
    Driver.driver.close()

@step("See Profile in <url>.") 
def assert_profile_in(url):
    Driver.driver.get(url)
    Driver.driver.find_element_by_name("email").send_keys("divyakhetan1209@gmail.com")
    Driver.driver.find_element_by_name("pass").send_keys("shreyakhetan1")
    Driver.driver.find_element_by_id("u_0_b").click()
    Driver.driver.find_element_by_class_name("_1k67").click()
    Driver.driver.find_element_by_class_name("fbTimelineProfilePicSelector").click()
    
    time.sleep(4)
    Driver.driver.close()

@step("Notifications in <url>.") 
def assert_notif_in(url):
    Driver.driver.get(url)
    Driver.driver.find_element_by_name("email").send_keys("divyakhetan1209@gmail.com")
    Driver.driver.find_element_by_name("pass").send_keys("shreyakhetan1")
    Driver.driver.find_element_by_id("u_0_b").click()
    Driver.driver.find_element_by_id("fbNotificationsJewel").click()
 
    
    time.sleep(4)
    Driver.driver.close()


@step("The word <word> has <number> vowels.")
def assert_no_of_vowels_in(word, number):
    assert str(number) == str(number_of_vowels(word))


@step("Vowels in English language are <vowels>.")
def assert_default_vowels(given_vowels):
    Messages.write_message("Given vowels are {0}".format(given_vowels))
    assert given_vowels == "".join(vowels)


@step("Almost all words have vowels <table>")
def assert_words_vowel_count(table):
    actual = [str(number_of_vowels(word)) for word in table.get_column_values_with_name("Word")]
    expected = [str(count) for count in table.get_column_values_with_name("Vowel Count")]
    assert expected == actual


# ---------------
# Execution Hooks
# ---------------

@before_scenario()
def before_scenario_hook():
    assert "".join(vowels) == "aeiou"
