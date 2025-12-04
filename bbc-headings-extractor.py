"""
BBC Headings Extractor
----------------------
This script extracts all H1, H2, and H3 headings from the BBC homepage
using Selenium WebDriver.

Author: Haram Hussain
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Set your ChromeDriver path ---
# Place chromedriver.exe in the same folder OR give full path
driver = webdriver.Chrome()

# Open website
driver.get("https://www.bbc.com/")

# Lists for storing extracted headings
element_h1 = []
element_h2 = []
element_h3 = []

try:
    # Wait until the page loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # Find heading tags
    h1_tags = driver.find_elements(By.TAG_NAME, "h1")
    h2_tags = driver.find_elements(By.TAG_NAME, "h2")
    h3_tags = driver.find_elements(By.TAG_NAME, "h3")

    print("Tags mil gaye!")

    # Extract text
    element_h1 = [tag.text.strip() for tag in h1_tags]
    element_h2 = [tag.text.strip() for tag in h2_tags]
    element_h3 = [tag.text.strip() for tag in h3_tags]

except Exception as e:
    print("Error:", e)

# Print output
print("\n=== H1 Headings ===")
print(element_h1)

print("\n=== H2 Headings ===")
print(element_h2)

print("\n=== H3 Headings ===")
print(element_h3)

# Save to a file
with open("bbc_headings_output.txt", "w", encoding="utf-8") as file:
    file.write("H1 Headings:\n")
    file.writelines([h + "\n" for h in element_h1])

    file.write("\nH2 Headings:\n")
    file.writelines([h + "\n" for h in element_h2])

    file.write("\nH3 Headings:\n")
    file.writelines([h + "\n" for h in element_h3])

print("\nFile saved as bbc_headings_output.txt")

driver.quit()
