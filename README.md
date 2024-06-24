# numberfield_flet

My take of creating a number input field in Flet.

- Supports both float and integer inputs
- Supports user-defined on_change callbacks

## Install it from PyPI

```bash
pip install numberfield-flet
```

## Usage

```py
import flet as ft
from numberfield_flet import NumberField

def user_defined_on_change(e):
    print(f"User-defined on_change event: {e.control.value}")


def main(page: ft.Page):
    page.title = "Number Inputter"
    custom_text_field = NumberField(on_change=user_defined_on_change, input_type="float",
                                    label="Enter a float number here: ")
    page.add(custom_text_field)
```

## Development

[Email me](mailto:andrey.gurtov@gmail.com) if you have any questions!