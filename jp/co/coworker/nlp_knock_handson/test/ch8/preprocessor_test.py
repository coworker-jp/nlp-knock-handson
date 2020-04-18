from unittest import TestCase

from jp.co.coworker.nlp_knock_handson.ch8.preprocessor import PreProcessor


class PreProcessorTest(TestCase):
    def test_read_dataset(self):
        input_lines = [
            "+1 I'm happy.",
            "-1 I'm sad",
        ]

        actual = PreProcessor.read_dataset(input_lines)
        expected_texts= [
            "I'm happy.",
            "I'm sad",
        ]
        expected_labels = [
            1,
            -1,
        ]
        expected = (expected_texts, expected_labels)
        self.assertEqual(actual, expected)

    def test_is_stop_word(self):
        preprocessor = PreProcessor()
        actual = preprocessor.is_stop_word('a')
        self.assertTrue(actual)
