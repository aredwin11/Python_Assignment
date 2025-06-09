import unittest
from src.validate_email.util import is_valid_email, filter_mail

class TestEmailValidation(unittest.TestCase):

    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user-name@domain.com"))
        self.assertTrue(is_valid_email("username123@domain.co"))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("user@domain"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("user#domain.com"))

    def test_filter_mail(self):
        emails = [
            "good_email@domain.com",
            "bad_email@domain",
            "another@domain.com",
            "wrong@domain.corporate"
        ]
        expected = ["good_email@domain.com", "another@domain.com"]
        self.assertEqual(filter_mail(emails), expected)

if __name__ == '__main__':
    unittest.main()
