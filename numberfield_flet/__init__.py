from typing import Literal, Callable

import flet as ft


class NumberField(ft.TextField):
    """
    A custom TextField that only accepts numerical input (``int`` or ``float``).

    Args:
        input_type (Literal["int", "float"], optional): The type of numerical input. Defaults to "int".
    """

    def __init__(self,
                 on_change: Callable[[ft.ControlEvent], None] = None,
                 input_type: Literal["int", "float"] = "int",
                 **kwargs):
        super().__init__(**kwargs)

        # Validate input type
        if input_type not in ("int", "float"):
            raise ValueError("Input must be either 'int' or 'float'")

        self.input_type = input_type
        self.keyboard_type = ft.KeyboardType.NUMBER

        # Custom on_change handler
        self.custom_on_change = self._custom_on_change
        self.user_on_change = on_change
        self.last_value = self.value

    def _custom_on_change(self, e):
        try:
            # Convert the input to the specified numerical type
            e.control.value = int(e.control.value) if self.input_type == "int" else float(e.control.value)
        except ValueError:
            # Handle invalid input
            e.control.value = self.last_value
            e.control.update()
        else:
            # Update the last valid value
            self.last_value = e.control.value
            # Call the user-defined on_change function if it exists
            if self.user_on_change:
                self.user_on_change(e)

    def build(self):
        self.on_change = self.custom_on_change
        return super().build()


# Example usage
def user_defined_on_change(e):
    print(f"User-defined on_change event: {e.control.value}")


def main(page: ft.Page):
    page.title = "Number Inputter"
    custom_text_field = NumberField(on_change=user_defined_on_change, input_type="float",
                                    label="Enter a number here: ")
    page.add(custom_text_field)


if __name__ == "__main__":
    ft.app(target=main)
