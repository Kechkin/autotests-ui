from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    check_registration_button_is_disabled = page.get_by_test_id('registration-page-registration-button')
    expect(check_registration_button_is_disabled).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.wait_for()
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.wait_for()
    username_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.wait_for()
    password_input.fill("password")

    check_registration_button_is_enabled = page.get_by_test_id('registration-page-registration-button')
    expect(check_registration_button_is_enabled).not_to_be_disabled()

    page.wait_for_timeout(5000)
