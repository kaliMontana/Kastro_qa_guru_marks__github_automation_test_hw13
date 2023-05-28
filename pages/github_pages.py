import allure
from selene import browser, be, by
from selene.support.shared.jquery_style import s


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Click on sign-up')
def search_sign_in_web():
    s('.HeaderMenu-link--sign-up').should(be.visible).click()


@allure.step('Click on sign-up')
def search_sign_in_mobil():
    s("[aria-label='Toggle navigation'] .Button-content").should(be.visible).click()
    s(by.text('Sign in')).should(be.visible).click()
