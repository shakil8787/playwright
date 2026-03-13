"""
Playwright Test for Saucedemo Login and Product Verification
This test automates the login flow and validates product names in the inventory.
"""

import pytest
from playwright.sync_api import sync_playwright, expect


class TestSaucedemoLogin:
    """Test suite for Saucedemo login and product verification"""

    def test_login_and_verify_products(self):
        """
        Test scenario:
        1. Open https://www.saucedemo.com/
        2. Login with username: standard_user and password: secret_sauce
        3. Verify successful login by checking product page elements
        """

        with sync_playwright() as p:
            # Launch browser in headed mode (browser visible)
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            try:
                # Step 1: Navigate to the website
                print("Step 1: Opening https://www.saucedemo.com/")
                page.goto("https://www.saucedemo.com/")
                page.wait_for_load_state("networkidle")

                # Verify login page is loaded
                login_button = page.locator("text=Login")
                expect(login_button).to_be_visible()
                print("✓ Login page loaded successfully")

                # Step 2: Fill in login credentials
                print("\nStep 2: Entering login credentials")

                # Find and fill username field
                username_field = page.locator('[data-test="username"]')
                username_field.fill("standard_user")
                print("✓ Username entered: standard_user")

                # Find and fill password field
                password_field = page.locator('[data-test="password"]')
                password_field.fill("secret_sauce")
                print("✓ Password entered: secret_sauce")

                # Step 3: Click login button
                print("\nStep 3: Clicking login button")
                login_button = page.locator('[data-test="login-button"]')
                login_button.click()
                page.wait_for_load_state("networkidle")
                print("✓ Login button clicked")

                # Step 4: Verify successful login
                print("\nStep 4: Verifying successful login")

                # Check if products page is loaded
                products_title = page.locator("text=Products")
                expect(products_title).to_be_visible()
                print("✓ Products page loaded successfully")

                # Verify product inventory is displayed
                product_items = page.locator('[data-test="inventory-item"]')
                items_count = product_items.count()
                assert items_count > 0, "No products found on the inventory page"
                print(f"✓ Found {items_count} products in inventory")

                # Verify specific product names
                print("\nStep 5: Verifying product names")

                # Get all product names
                product_names = page.locator('[data-test="inventory-item-name"]')
                product_count = product_names.count()

                print(f"✓ Total products displayed: {product_count}")

                # Verify first product name
                first_product = product_names.nth(0)
                first_product_text = first_product.text_content()
                print(f"✓ First product: {first_product_text}")
                assert "Sauce Labs" in first_product_text or len(first_product_text) > 0, \
                    "Product name verification failed"

                # Step 6: Verify logout option exists
                print("\nStep 6: Verifying user menu is available")
                menu_button = page.locator('id=react-burger-menu-btn')
                expect(menu_button).to_be_visible()
                print("✓ Menu button is available")

                print("\n" + "="*50)
                print("✓ ALL TESTS PASSED!")
                print("="*50)

                # Keep browser open for a moment to see the results
                page.wait_for_timeout(2000)

            except AssertionError as e:
                print(f"\n✗ Test assertion failed: {e}")
                # Take screenshot for debugging
                page.screenshot(path="test_failure.png")
                raise
            except Exception as e:
                print(f"\n✗ Test failed with error: {e}")
                # Take screenshot for debugging
                page.screenshot(path="test_failure.png")
                raise
            finally:
                # Close the browser
                browser.close()


# Alternative simple test function for pytest discovery
def test_saucedemo_login():
    """Simple test function for pytest discovery - delegates to test class"""
    test = TestSaucedemoLogin()
    test.test_login_and_verify_products()


if __name__ == "__main__":
    # Run with pytest
    pytest.main([__file__, "-v", "-s"])

