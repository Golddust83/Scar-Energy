from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestScar(TestCase):
    """
    Things to test in this class:

    # Home page loads
    # Product can be found
    # Product can be added to shopping cart
    # Product can be found in shopping cart 
    # Customer gets to the checkout page
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://scar.sandbox.iceberry.se/v.0.3.0/#/")
        self.driver.maximize_window()
                
    def test_load_site(self): 
        """
        Testing that scar is part of the URL
        """
        self.assertIn("scar", self.driver.current_url)

    def test_home_page(self):
        """
        Testing that you get to home when clicking on the SCAR icon
        """
        # Click "View more products" button
        self.products = self.driver.find_element(
            By.XPATH, "/html/body/div/main/div/main/a[2]").click()
        # Click SCAR image
        self.home = self.driver.find_element(
            By.XPATH, "/html/body/div/header/div/a").click()
        # Test that URL now doesn't contain "products"
        self.assertFalse(
            "products" in self.driver.current_url, "Products is not present in the current URL.")

    def test_single_product_page(self): 
        """
        Testing that explicit product exist on product page
        """
        # Click "View more products" button
        self.products = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/div/main/a[2]")).click()
        # Find Scar Salt_Water product
        self.salt_water = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/section/div/main/a[2]/div/div[1]"))
        # Check that Salt water product is displayed on page
        self.assertTrue(self.salt_water.is_displayed(), "Product not found under header.")

    def test_add_shopping_cart(self):
        """
        Testing that you can add a product to shopping cart
        """
        # Click "View more products" button
        self.products = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/div/main/a[2]")).click()
        # Find Scar Salt_Water product
        self.salt_water = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/section/div/main/a[2]/div/div[2]/h2")).click()
        # Click "Add to cart"
        self.add_to_cart = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/div[1]/div/div[2]/div[2]/div/button[2]")).click()
        # Click on shopping cart
        self.shopping_cart = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/header/div/div/a/button")).click()
        # Check that you are now in cart page
        self.assertIn("cart", self.driver.current_url)
        # Check that you have the correct product added
        self.text = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/div/div[1]/div/div/a/div/h2")).text
        self.assertIn("Scar Salt_Water", self.text)
        
    def test_checkout(self):
        """
        Testing that you can proceed to checkout
        """
        # Click "View more products" button
        self.products = self.driver.find_element(
            By.XPATH, "/html/body/div/main/div/main/a[2]").click()
        # Find Scar Salt_Water product
        self.salt_water = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/section/div/main/a[2]/div/div[2]/h2")).click()
        # Click "Add to cart"
        self.add_to_cart = self.driver.find_element(
            By.XPATH, "/html/body/div/main/div[1]/div/div[2]/div[2]/div/button[2]").click()
        # Click on shopping cart
        self.shopping_cart = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/header/div/div/a/button")).click()
        # Click on "Proceed to checkout"
        self.shopping_cart = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(
             By.XPATH, "/html/body/div/main/div/div[2]/div/div/button")).click()
        # Check that you are on checkout page
        self.assertIn("checkout", self.driver.current_url)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    if __name__ == "__main__":
        main()