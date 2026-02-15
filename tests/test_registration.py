
def test_successful_registration(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    chromium_page_with_state.wait_for_timeout(5000)
