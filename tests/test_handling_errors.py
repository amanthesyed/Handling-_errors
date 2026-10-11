"""Unit tests for the cookie distribution function."""

import contextlib
import io
import unittest

from handling_errors import party_planner


class PartyPlannerTests(unittest.TestCase):
    def call_silently(self, cookies: int, people: int):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = party_planner(cookies, people)
        return result, output.getvalue()

    def test_even_distribution(self):
        self.assertEqual(party_planner(12, 4), (3, 0))

    def test_distribution_with_remainder(self):
        self.assertEqual(party_planner(25, 4), (6, 1))

    def test_more_people_than_cookies(self):
        self.assertEqual(party_planner(4, 8), (0, 4))

    def test_zero_people_is_rejected(self):
        result, message = self.call_silently(10, 0)
        self.assertEqual(result, (None, None))
        self.assertIn("greater than zero", message)

    def test_negative_people_is_rejected(self):
        result, message = self.call_silently(10, -2)
        self.assertEqual(result, (None, None))
        self.assertIn("greater than zero", message)

    def test_negative_cookie_count_is_rejected(self):
        result, message = self.call_silently(-1, 3)
        self.assertEqual(result, (None, None))
        self.assertIn("cannot be negative", message)


if __name__ == "__main__":
    unittest.main()
