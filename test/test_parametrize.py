import pytest
from selene import browser

from pages.github_pages import open_main_page, search_sign_in_web, search_sign_in_mobil

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

window_sizes = [(1980, 1080),
                (819, 400),
                (1700, 1300),
                (653, 280)
                ]

url = 'https://github.com'

desktop_params = pytest.mark.parametrize('browser_setup', [window_sizes[0], window_sizes[2]],
                                         ids=['desktop', 'desktop'],
                                         indirect=True)
mobile_params = pytest.mark.parametrize('browser_setup', [window_sizes[1], window_sizes[3]], ids=['mobile', 'mobile'],
                                        indirect=True)


@pytest.fixture(params=window_sizes, ids=['desktop', 'mobile', 'desktop', 'mobile'])
def browser_setup(request):
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    browser.config.base_url = url
    yield request.node.callspec.id
    browser.quit()


@desktop_params
def test_sign_up_feature_desktop(browser_setup):
    open_main_page()
    search_sign_in_web()


@mobile_params
def test_sign_up_feature_mobile(browser_setup):
    open_main_page()
    search_sign_in_mobil()
