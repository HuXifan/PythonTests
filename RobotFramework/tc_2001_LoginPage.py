"""
       Test for AAT GUI

       ============================================================================================
       Revision Histroy
       ============================================================================================
       Date         Name        What
       --------------------------------------------------------------------------------------------
       2019/2/28     eshrdpk      First Version
       2019/4/2      EZYANMI      update
"""
import time
from framework.bamboo.case import TestCase


class TC_2001_LoginPage(TestCase):
    def setUp(self):
        if self.main_page.is_login():
            self.main_page.switch_to_page('Logout')
        self.main_page.wait_to_page('Logout')

    def tearDown(self):
        pass

    def tc_2001_001_Login_page_layout(self):
        self.value.assertTrue(self.main_page.isexpected_logintitle('AAT LOGIN'))
        self.value.assertTrue(self.main_page.isexpected_logoname('Ericsson Automated Acceptance Tests'))
        self.main_page.click_logo_picture()
        self.main_page.click_logo_name()
        self.main_page.click_login_page_name()

    def tc_2001_002_correct_user_password(self):
        self.main_page.login()
        self.main_page.wait_to_page('Home')

    def tc_2001_003_error_message_incorrect_password(self):
        self.main_page.login(pwd='invalidpwd')
        msg = self.main_page.get_login_message()
        self.value.assertEqual(msg, u'Incorrect Password!')

    def tc_2001_004_error_message_user_not_exist(self):
        self.main_page.login(user=u"invalidusr")
        msg = self.main_page.get_login_message()
        self.value.assertEqual(msg, u"User Doesn't Exist!")

    def tc_2001_005_error_message_enter_password(self):
        self.main_page.login(pwd=u"")
        msg = self.main_page.get_login_message()
        self.value.assertEqual(msg, u"Please enter password.")

    def tc_2001_006_error_message_invalid_user_password(self):
        self.main_page.login(user=u"")
        msg = self.main_page.get_login_message()
        self.value.assertEqual(msg, u"Please enter username.")

    def tc_2001_007_error_message_invalid_user_password(self):
        self.main_page.login(user=u"", pwd=u"")
        msg = self.main_page.get_login_message()
        self.value.assertEqual(msg, u"Please enter username and password.")

    def tc_2001_008_login_button_torture_test(self):
        self.main_page.login()
        self.main_page.click_login_button()
        self.main_page.wait_to_page('Home')

    def tc_2001_009_Main_page_layout(self):
        self.main_page.login()
        self.main_page.wait_to_page('Home')
        self.value.assertTrue(self.main_page.isexpected_logoname('Ericsson Automated Acceptance Tests'))

    def tc_2001_010__Main_page_adapter(self):
        self.main_page.login()
        self.main_page.wait_to_page('Home')
        time.sleep(5)
        self.main_page.switch_to_page('Build')

    def tc_2001_011_Check_name_logo_on_Login_page(self):
        self.main_page.click_logo_picture()
        self.main_page.wait_to_page('Logout')
        self.main_page.click_logo_name()
        self.main_page.wait_to_page('Logout')

    def tc_2001_012_Check_name_logo_on_other_page(self):
        self.main_page.login()
        self.main_page.wait_to_page('Home')
        for page in ['Build', 'Execute', 'Configure', 'Results']:
            self.main_page.switch_to_page(page)
            self.main_page.click_logo_picture()
            self.main_page.wait_to_page('Home')
        for page in ['Build', 'Execute', 'Configure', 'Results']:
            self.main_page.switch_to_page(page)
            self.main_page.click_logo_name()
            self.main_page.wait_to_page('Home')

    def tc_2001_013_Check_every_button_on_system_bar(self):
        for page in ['Home', 'Build', 'Execute', 'Configure', 'Results', 'Settings']:
            self.main_page.login_to_page('function test', page)
            self.main_page.switch_to_page('Logout')
            new_page = self.main_page.get_current_page()
            self.value.assertEqual(new_page, 'Logout')

    def tc_2001_014_Check_bread_crumb_button_on_system_bar(self):
        self.main_page.login_to_page('function test', 'Build')
        crumbs = self.main_page.get_bread_crumbs()
        self.value.assertEqual(u'AAT', crumbs[0].text)
        self.value.assertEqual(u'Function Test Test Service For Quicktest', crumbs[1].text)
        self.value.assertEqual(u'Build', crumbs[2].text)
        self.main_page.click(crumbs[0])
        self.main_page.wait_to_page('Home')

        for page in [u'Execute', u'Configure', u'Results']:
            self.main_page.switch_to_page(page)
            crumbs = self.main_page.get_bread_crumbs()
            self.value.assertEqual(u'AAT', crumbs[0].text)
            self.value.assertEqual(u'Function Test Test Service For Quicktest', crumbs[1].text)
            self.value.assertEqual(page, crumbs[2].text)
            self.main_page.click(crumbs[0])
            self.main_page.wait_to_page('Home')
            self.main_page.switch_to_page(page)
            crumbs = self.main_page.get_bread_crumbs()
            self.main_page.click(crumbs[1])
            self.main_page.wait_to_page('Build')

        for page in [u'Settings']:
            self.main_page.switch_to_page(page)
            crumbs = self.main_page.get_bread_crumbs()
            self.value.assertEqual(u'AAT', crumbs[0].text)
            self.value.assertEqual(page, crumbs[1].text)
            self.main_page.click(crumbs[0])
            self.main_page.wait_to_page('Home')

    def tc_2001_015_forward_cannot_login_when_logout_status(self):
        self.main_page.login()
        self.main_page.wait_to_page('Home')
        self.main_page.back()
        time.sleep(5)
        # add a step to check now it is logout
        self.main_page.forward()
        time.sleep(5)

    def tc_2001_016_backward_cannot_login_when_logout_status(self):
        self.main_page.login()
        self.main_page.wait_to_page('Home')
        self.main_page.switch_to_page('Build')
        self.main_page.switch_to_page('Logout')
        self.main_page.back()
        time.sleep(5)
        logging_status = self.main_page.is_login()
        self.value.assertEqual(logging_status, False)

    def tc_2001_017_Check_refresh_button_of_browser(self):
        for page in [u'Home', u'Build', u'Execute', u'Configure', u'Results', u'Settings', 'Logout']:
            self.main_page.login_to_page('function test', page)
            self.main_page.refresh()
            self.main_page.wait_to_page('Logout')
            logging_status = self.main_page.is_login()
            self.value.assertEqual(logging_status, False)
