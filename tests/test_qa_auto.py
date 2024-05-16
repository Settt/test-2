import time

from page_objects.garage_page import GaragePage, AddCarModal
from page_objects.home_page import HomePage


def test_login_as_guest_user(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_guest_login_button()

    garage_page = GaragePage(driver)

    garage_page.assert_guest_message_is_displayed()


def test_login_add_car_as_guest(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_guest_login_button()

    garage_page = GaragePage(driver)

    garage_page.click_add_car_button()

    add_car_modal = AddCarModal(driver)

    car_brand_name = "Ford"
    car_model_name = "Sierra"

    add_car_modal.select_brand(car_brand_name)
    add_car_modal.select_model(car_model_name)
    add_car_modal.set_mileage(50000)
    add_car_modal.click_add_button()

    time.sleep(3)

    garage_page.assert_car_in_list(f"{car_brand_name} {car_model_name}")
