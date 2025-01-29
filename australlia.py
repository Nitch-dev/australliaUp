# from playwright.sync_api import sync_playwright
import smtplib
from email.message import EmailMessage
from selenium import webdriver

def takeSS(driver, filename="1.png"):
    try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(driver.get_window_size()['width'], total_height)
        driver.save_screenshot(filename)
        print(f"Full-page screenshot saved as {filename}")
    except Exception as e:
        print(f"Error taking full-page screenshot: {e}")


driver = webdriver.Chrome()
driver.get("http://playwright.dev")
takeSS(driver,"1.png")
takeSS(driver,"2.png")
takeSS(driver,"3.png")

sender_email = "hassan.rahmani922@gmail.com"
sender_password = "hwmr amim tfqr gebi "
receiver_email = "hassan.rahmani922@gmail.com"  # Use a different email for testing
message = "HEllO"

msg = EmailMessage()
msg['Subject'] = "Website Pictures"
msg ['From'] = sender_email
msg['To'] = receiver_email
msg.set_content("Hi, See the Pictures Below:")
images = ["1.png","2.png","3.png"]
for img in images:
    with open(img,'rb') as f:
        file_data = f.read()
        fname = f.name
    msg.add_attachment(file_data, maintype='image',subtype='png',filename=fname)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(sender_email,sender_password)

    smtp.send_message(msg)