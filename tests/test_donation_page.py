THANK_YOU_MESSAGE = "Vielen Dank für deine Spende!"
CONFIRMATION_AMOUNT = "Ich spende: 6,00 €"


class TestDonationPage:
    def test_successful_five_euro_donation(self, donation_page, customer):
        donation_page.click_accept_cookies_button()

        confirmation = donation_page.fill_form_with_valid_data_and_submit(customer, 5)
        assert confirmation.amount == CONFIRMATION_AMOUNT

        payment = confirmation.proceed()
        assert payment.thank_you_message == THANK_YOU_MESSAGE

    def test_payment_methods_dimension_for_mobile_ui(self, mobile_donation_page):
        label_width = mobile_donation_page.get_width_of_payment_label()
        payment_method_width = mobile_donation_page.get_width_of_payment_methods()
        assert payment_method_width == label_width
