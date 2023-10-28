import requests
from bs4 import BeautifulSoup

response_0 = requests.get('https://www.pixiv.net')
soup_login = BeautifulSoup(response_0.text)
print(soup_login.find('form'))
"""
<form action="https://accounts.pixiv.net/pigya/start" class="sns-login-form" method="POST">
    <input name="tt" type="hidden" value="14947237d642e4c50e8b40ff6a019ff2" />
    <input name="mode" type="hidden" value="signin" />
    <input name="provider" type="hidden" value="apple" />
    <input name="lang" type="hidden" value="ja" />
    <input name="source" type="hidden" value="pc" />
    <input name="view_type" type="hidden" value="page" />
    <button class="btn-item js-click-trackable compact index btn-apple" data-action="step1" data-category="signup_page_pc" data-label="apple" type="submit">Appleで続ける</button>
</form>
"""