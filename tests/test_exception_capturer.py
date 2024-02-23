import unittest

import exception_capturer


class ExceptionCapturerTests(unittest.TestCase):
    def assertEqualExceptionGroupMessages(
        self, exception_group: ExceptionGroup, expected_messages: list
    ):
        exceptions = exception_group.exceptions
        actual_messages = [str(e) for e in exceptions]
        self.assertEqual(expected_messages, actual_messages)

    def test_capture(self):
        with self.assertRaises(ExceptionGroup) as context:
            with exception_capturer.ExceptionCapturer() as ec:
                for value in ["one", "2", "three"]:
                    with ec.capture():
                        int(value)

        self.assertEqualExceptionGroupMessages(
            context.exception,
            [
                "invalid literal for int() with base 10: 'one'",
                "invalid literal for int() with base 10: 'three'",
            ],
        )

    def test_no_capture(self):
        with self.assertRaises(ExceptionGroup) as context:
            with exception_capturer.ExceptionCapturer():
                int("four")
        self.assertEqualExceptionGroupMessages(
            context.exception,
            [
                "invalid literal for int() with base 10: 'four'",
            ],
        )

    def test_combined(self):
        with self.assertRaises(ExceptionGroup) as context:
            with exception_capturer.ExceptionCapturer() as ec:
                for value in ["one", "2", "three"]:
                    with ec.capture():
                        int(value)
                int("four")

        self.assertEqualExceptionGroupMessages(
            context.exception,
            [
                "invalid literal for int() with base 10: 'one'",
                "invalid literal for int() with base 10: 'three'",
                "invalid literal for int() with base 10: 'four'",
            ],
        )
