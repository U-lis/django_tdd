import os
from selenium import webdriver
os.environ["PATH"] += ":/home/ulismoon/bin/geckodriver"

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title
