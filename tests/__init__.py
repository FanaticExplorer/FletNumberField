import unittest
from unittest.mock import Mock
import flet as ft

# Assuming NumberField is imported from your module
from src.numberfield_flet import NumberField


class TestNumberField(unittest.TestCase):

    def test_initialization_default(self):
        # Test default initialization
        field = NumberField()
        self.assertEqual(field.input_type, "int")
        self.assertEqual(field.keyboard_type, ft.KeyboardType.NUMBER)

    def test_initialization_custom(self):
        # Test custom initialization
        field = NumberField(input_type="float")
        self.assertEqual(field.input_type, "float")
        self.assertEqual(field.keyboard_type, ft.KeyboardType.NUMBER)

    def test_invalid_input_type(self):
        # Test invalid input type raises ValueError
        with self.assertRaises(ValueError):
            # noinspection PyTypeChecker
            NumberField(input_type="string")

    def test_valid_int_input(self):
        # Test valid integer input
        field = NumberField(input_type="int")
        event = Mock()
        event.control.value = "123"
        field._custom_on_change(event)
        self.assertEqual(event.control.value, 123)

    def test_valid_float_input(self):
        # Test valid float input
        field = NumberField(input_type="float")
        event = Mock()
        event.control.value = "123.45"
        field._custom_on_change(event)
        self.assertEqual(event.control.value, 123.45)

    def test_invalid_int_input(self):
        # Test invalid integer input
        field = NumberField(input_type="int")
        field.last_value = 0
        event = Mock()
        event.control.value = "abc"
        field._custom_on_change(event)
        self.assertEqual(event.control.value, 0)

    def test_invalid_float_input(self):
        # Test invalid float input
        field = NumberField(input_type="float")
        field.last_value = 0.0
        event = Mock()
        event.control.value = "abc"
        field._custom_on_change(event)
        self.assertEqual(event.control.value, 0.0)

    def test_on_change_callback(self):
        # Test user-defined on_change callback
        mock_callback = Mock()
        field = NumberField(on_change=mock_callback, input_type="int")
        event = Mock()
        event.control.value = "123"
        field._custom_on_change(event)
        self.assertTrue(mock_callback.called)
        self.assertEqual(event.control.value, 123)


if __name__ == "__main__":
    unittest.main()
