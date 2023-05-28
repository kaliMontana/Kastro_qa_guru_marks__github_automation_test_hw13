import pytest
from selene import browser

from pages.github_pages import open_main_page, search_sign_in_web, search_sign_in_mobil

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

window_size_web = [(1980, 1080),
                   (1700, 1300)
                   ]
window_size_mobil = [(819, 400),
                     (653, 280)
                     ]

url = 'https://github.com'


@pytest.fixture(params=window_size_web)
def browser_setup_web(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    browser.config.base_url = url
    yield
    browser.quit()


@pytest.fixture(params=window_size_mobil)
def browser_setup_mobile(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    browser.config.base_url = url
    yield
    browser.quit()


def test_sign_up_feature_web(browser_setup_web):
    open_main_page()
    search_sign_in_web()


def test_sign_up_feature_mobile(browser_setup_mobile):
    open_main_page()
    search_sign_in_mobil()
