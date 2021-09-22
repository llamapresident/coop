# Morgan
# WebScraping
# 9/22

from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://www.evit.com/high_school_career_training/hs')
main_content = r.html.find('div.main-content', first=True)
print(main_content.text)