from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# Path to your ChromeDriver executable
driver_path = r"C:\Users\Anuj\AppData\Local\Programs\Python\chromedriver-win64\chromedriver.exe"

# Create a Service object for ChromeDriver
service = ChromeService(executable_path=driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Navigate to the main website
    driver.get("https://www.fitpeo.com/")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click on the "Revenue Calculator" link
    revenue_calculator_button = driver.find_element(By.LINK_TEXT, "Revenue Calculator")  # Adjust locator if necessary
    revenue_calculator_button.click()
    time.sleep(3)  # Wait for the Revenue Calculator page to load

    # Step 3: Scroll down to slider section
    slider_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", slider_section)
    time.sleep(2) 

    
    # Step 4: Adjust the slider to set its value to 820
    slider_thumb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/div/span[1]/span[1]"))  # Replace with the actual ID or locator of the slider
    )
   
    text_field = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/input")  # Replace with the ID of the text field

    # Programmatically update the slider value
    # Update slider using the text field value
    target_value = 820
    text_field.click()
    text_field.send_keys(Keys.CONTROL + "a")  # Select all existing text
    text_field.send_keys(Keys.BACKSPACE)  # Clear the text field
    text_field.send_keys(str(target_value))  # Enter the new value

    driver.execute_script(f"""
        let slider = document.querySelector('input');  // Replace with the correct ID
        slider.value = {target_value};
        slider.dispatchEvent(new Event('input', {{ bubbles: true }}));  // Trigger 'input' event
        slider.dispatchEvent(new Event('change', {{ bubbles: true }}));  // Trigger 'change' event
    """)

    # # Verify updated value
    time.sleep(2)
    updated_value = text_field.get_attribute("value")
    print(f"Updated slider value: {updated_value}")

    if int(updated_value) == target_value:
        print(f"Slider successfully set to {target_value}.")
    else:
        print("Failed to set the slider value.")

    time.sleep(2)

    # Step 5: Update the text field to 560 and ensure slider adjusts
    new_value = 560
    text_field.click()
    text_field.send_keys(Keys.CONTROL + "a")  # Select all existing text
    text_field.send_keys(Keys.BACKSPACE)  # Clear the text field
    text_field.send_keys(str(new_value))  # Enter the new value

    # Trigger change event for the text field
    driver.execute_script(f"""
        let textField = document.querySelector('input');  // Update with the correct selector if necessary
        textField.value = {new_value};
        textField.dispatchEvent(new Event('input', {{ bubbles: true }}));
        textField.dispatchEvent(new Event('change', {{ bubbles: true }}));
    """)

    # Step 6: Verify slider updates accordingly
    time.sleep(2)
    updated_slider_value = text_field.get_attribute("value")
    print(f"Updated text field value: {updated_slider_value}")

    if int(updated_slider_value) == new_value:
        print(f"Text field and slider successfully updated to {new_value}.")
    else:
        print("Failed to update the text field or slider.")

    time.sleep(5)

       # Step 7: Scroll down further and select checkboxes for  CPT-99091, CPT-99453, CPT-99454, and CPT-99474.
       # For CPT-99091
    checkboxes_to_select = ["CPT-99091"]

    for checkbox_label in checkboxes_to_select:
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        if not checkbox.is_selected():
            checkbox.click()
        print(f"Selected checkbox: {checkbox_label}")

    time.sleep(2)

       # Step 7: Select value 57 in CPT-99091
    cpt_99091_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/label/span[2]"))  # Adjust XPath as per actual HTML structure
    )
    
    # Check if it's an input field
    if cpt_99091_field.get_attribute("type") == "number" or "text":
        cpt_99091_field.click()
        print("Successfully entered 57 in CPT-99091.")

        # Trigger 'input' and 'change' events (if necessary)
        driver.execute_script("""
            let inputField = arguments[0];
            inputField.dispatchEvent(new Event('input', { bubbles: true }));
            inputField.dispatchEvent(new Event('change', { bubbles: true }));
        """, cpt_99091_field)

    else:
        print("The CPT-99091 field is not editable.")

    time.sleep(2)


   # For CPT-99453
    checkboxes_to_select = ["CPT-99453"]

    for checkbox_label in checkboxes_to_select:
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        if not checkbox.is_selected():
            checkbox.click()
        print(f"Selected checkbox: {checkbox_label}")

    time.sleep(2)

       # Select value 19.19 in CPT-99453
    cpt_99453_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/label/span[2]"))  # Adjust XPath as per actual HTML structure
    )
    
    # Check if it's an input field
    if cpt_99453_field.get_attribute("type") == "number" or "text":
        cpt_99453_field.click()
        print("Successfully entered 19.19 in CPT-99453.")

        # Trigger 'input' and 'change' events (if necessary)
        driver.execute_script("""
            let inputField = arguments[0];
            inputField.dispatchEvent(new Event('input', { bubbles: true }));
            inputField.dispatchEvent(new Event('change', { bubbles: true }));
        """, cpt_99453_field)

    else:
        print("The CPT-99453 field is not editable.")

    time.sleep(2)


     # For CPT-99454
    checkboxes_to_select = ["CPT-99454"]

    for checkbox_label in checkboxes_to_select:
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[3]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        if not checkbox.is_selected():
            checkbox.click()
        print(f"Selected checkbox: {checkbox_label}")

    time.sleep(2)

       # Select value 63 in CPT-99454
    cpt_99454_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[3]/label/span[2]"))  # Adjust XPath as per actual HTML structure
    )
    
    # Check if it's an input field
    if cpt_99454_field.get_attribute("type") == "number" or "text":
        cpt_99454_field.click()
        print("Successfully entered 63 in CPT-99454.")

        # Trigger 'input' and 'change' events (if necessary)
        driver.execute_script("""
            let inputField = arguments[0];
            inputField.dispatchEvent(new Event('input', { bubbles: true }));
            inputField.dispatchEvent(new Event('change', { bubbles: true }));
        """, cpt_99454_field)

    else:
        print("The CPT-99454 field is not editable.")

    time.sleep(2)


    # For CPT-99474
    checkboxes_to_select = ["CPT-99474"]

    for checkbox_label in checkboxes_to_select:
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[8]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        if not checkbox.is_selected():
            checkbox.click()
        print(f"Selected checkbox: {checkbox_label}")

    time.sleep(2)

       #  Select value 15 in CPT-99474
    cpt_99474_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[8]/label/span[2]"))  # Adjust XPath as per actual HTML structure
    )
    
    # Check if it's an input field
    if cpt_99474_field.get_attribute("type") == "number" or "text":
        cpt_99474_field.click()
        print("Successfully entered 15 in CPT-99474.")

        # Trigger 'input' and 'change' events (if necessary)
        driver.execute_script("""
            let inputField = arguments[0];
            inputField.dispatchEvent(new Event('input', { bubbles: true }));
            inputField.dispatchEvent(new Event('change', { bubbles: true }));
        """, cpt_99474_field)

    else:
        print("The CPT-99474 field is not editable.")

    time.sleep(2)

       # Step 8 & Step 9: Locate the header displaying the Total Recurring Reimbursement
    reimbursement_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/div/div[3]/p[2]"))
    )

    # Extract the text from the header
    displayed_value = reimbursement_header.text
    print(f"Displayed Value: {displayed_value}")

    # Extract the numeric part and clean the text
    numeric_value = displayed_value.split("$")[-1].replace(",", "").strip()  # Remove '$' and commas

    # Validate the numeric value
    expected_value = 110700  # Expected value for comparison
    if int(numeric_value) == expected_value:
        print("Validation Passed: Total Recurring Reimbursement for all Patients Per Month matches the expected value of $110,700.")
    else:
        print(f"Validation Failed: Expected $110,700 but found ${numeric_value}.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


finally:
    # Close the browser
    driver.quit()
  
 ### Step 5 & Step 6 are not showing in recording of working project because it is not matching with reimbursement for all patients.
