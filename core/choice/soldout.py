from selenium.common.exceptions import NoSuchElementException


class soldout_color_testing:
    """
    Test if the product is soldout or no. If the product is soldout, return to the homepage of shop/all.
    """
    def soldout_control(driver):
        """
        soldout_control : driver -> True or False
        soldout_control(driver) Test if the product is sold out or no. Return True if the product is already available, false if not.
        """
        try:
            driver.find_element_by_xpath("//input[@value='ajouter']")
            return False

        except NoSuchElementException:
            return True

    def select_color(driver, break_condition, incrementation, process_loop_break_condition):
        """
        select_color : driver * Int * Int-> None
        select_color(driver, shoe_size) Select item's color. Return None.
        """
        is_soldout = soldout_color_testing.soldout_control(driver)

        if is_soldout is False:
            process_loop_break_condition = 0
            return process_loop_break_condition

        else:
            while break_condition == 0:
                try:
                    driver.find_elements_by_xpath("//*[@id='details']/ul/li[{}]/a[1]".format(incrementation))[0].click()
                    is_soldout = soldout_color_testing.soldout_control(driver)

                    if is_soldout is False:
                        break_condition = 1
                        process_loop_break_condition = 0
                        return process_loop_break_condition

                    else:
                        incrementation += 1
                        
                except Exception:
                    break_condition = 1
                    process_loop_break_condition = 1

            return process_loop_break_condition
