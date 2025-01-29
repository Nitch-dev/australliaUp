# from playwright.sync_api import sync_playwright
import smtplib
from email.message import EmailMessage
from selenium import webdriver
import time
from playwright.async_api import async_playwright, Mouse
import asyncio
import pyautogui
async def main():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.freedom.com.au/c/karpenter?page=2&perPage=18&sortCriteria=custom_prd_onsale%20desc")
        

asyncio.run(main())
time.sleep(3)
pyautogui.screenshot("1.png")
print("Page SS done")

sender_email = ""
sender_password = ""
receiver_email = ""  
message = "Hey"

msg = EmailMessage()
msg['Subject'] = "Website Pictures"
msg ['From'] = sender_email
msg['To'] = receiver_email
msg.set_content("Hi, See the Pictures Below:")
images = ["1.png"]
for img in images:
    with open(img,'rb') as f:
        file_data = f.read()
        fname = f.name
    msg.add_attachment(file_data, maintype='image',subtype='png',filename=fname)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(sender_email,sender_password)

    smtp.send_message(msg)