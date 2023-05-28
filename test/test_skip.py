import pytest
from selene import browser

from pages.github_pages import open_main_page, search_sign_in_web, search_sign_in_mobil

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

window_sizes = [(1980, 1080),
                (819, 400),
                (1700, 1300),
                (653, 280)
                ]

url = 'https://github.com'


@pytest.fixture(params=window_sizes, ids=['desktop', 'mobile', 'desktop', 'mobile'])
def browser_setup(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    browser.config.base_url = url
    yield request.node.callspec.id
    browser.quit()


# General test
def test_sign_up_feature(browser_setup):
    test_sign_up_feature_desktop(browser_setup)
    test_sign_up_feature_mobile(browser_setup)


def test_sign_up_feature_desktop(browser_setup):
    if 'mobile' in browser_setup:
        pytest.skip(reason='Test not for desktop')
    open_main_page()
    search_sign_in_web()


def test_sign_up_feature_mobile(browser_setup):
    if 'desktop' in browser_setup:
        pytest.skip(reason='Test not for mobile')
    open_main_page()
    search_sign_in_mobil()
