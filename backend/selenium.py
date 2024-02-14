from selenium import webdriver
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def open_web_browser():
    driver = webdriver.Chrome()
    return driver

def perform_search(driver, query):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.submit()

def navigate_to_website(driver, website_url):
    try:
        print("Navigating to:", website_url)
        driver.get(website_url)
    except Exception as e:
        print("Error navigating to website:", e)

# desired_capabilities = {
#     "app": "C:\\Program Files\\Android\\Android Studio\\bin.exe",
# }
# driver = webdriver.WebDriver(
# command_executor='http://127.0.0.1:4723',
# desired_capabilities=desired_capabilities
# )
# driver.quit()


# Your automation script goes here

# Close the application and WinAppDriver when done

def close_browser(driver):
    driver.quit()

if __name__ == "__main__":
    web_driver = open_web_browser()

    while True:
        voice_command = get_voice_input()

        if not voice_command:
            continue

        # if "search" in voice_command:
        #     search_query = voice_command.replace("search", "").strip()
        #     perform_search(web_driver, search_query)

        elif "open website" in voice_command:
            website_url = voice_command.replace("open website", "https://www.w3schools.com/").strip()
            navigate_to_website(web_driver, website_url)

        elif "close" in voice_command:
            close_browser(web_driver)
            break
