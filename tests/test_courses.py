from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.wait_for()
        email_input.fill("user.name@gmail.com")

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.wait_for()
        username_input.fill("username")

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.wait_for()
        password_input.fill("password")

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.wait_for()
        registration_button.click()

        context.storage_state(path="browser-state-practice.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state-practice.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        text_courses = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(text_courses).to_have_text('Courses')

        icon_folder = page.get_by_test_id("courses-list-empty-view-icon")
        expect(icon_folder).to_be_visible()

        text_no_results = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(text_no_results).to_have_text('There is no results')

        text_res_pipeline_displayed = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(text_res_pipeline_displayed).to_have_text('Results from the load test pipeline will be displayed here')
