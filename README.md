# Exception Capturer

The `exception_capturer` module provides a convenient way to capture and aggregate exceptions that occur in blocks of code, allowing them to be raised together as an `ExceptionGroup`. This is particularly useful in scenarios where you want to attempt multiple operations that may fail and handle all the exceptions at once after the operations are completed.

## Installation

```sh
pip install git+https://github.com/bulv1ne/exception_capturer.git
# OR
https://github.com/bulv1ne/exception_capturer/archive/refs/heads/main.zip
```

## Usage

### Basic Usage

The `exception_capturer` module provides a convenient way to manage exceptions in blocks of code where errors are anticipated. By using the `ExceptionCapturer` context manager, you can capture and aggregate exceptions, raising them together after the block's execution. This is particularly useful in scenarios where multiple operations may fail, and you wish to handle all exceptions at once.

#### Using ExceptionCapturer with a capture block

Wrap the code block where exceptions may occur with the `ExceptionCapturer` context manager. This will capture any exceptions thrown within the block without immediately raising them. After exiting the block, if any exceptions were captured, they will be aggregated and raised together as an `ExceptionGroup`.

```python
from exception_capturer import ExceptionCapturer

with ExceptionCapturer() as ec:
    for value in ["one", "2", "three"]:
        with ec.capture():
            int(value)
    # Attempts to convert "four", which is outside the loop and not captured
    int("four")
# If any exceptions occurred within the `with ec.capture():` block,
# an ExceptionGroup will be raised here, containing those exceptions.
```

#### Using ExceptionCapturer to call a function and handle exceptions

`ExceptionCapturer` also provides a method to call a function within the try-except block. This method, `call_function`, attempts to call the specified function with the provided arguments. If the function call raises an exception, it is captured, and `None` is returned; otherwise, the function's result is returned. This approach simplifies exception handling when calling functions that may throw exceptions.

```python
from exception_capturer import ExceptionCapturer

with ExceptionCapturer() as ec:
    for value in ["one", "2", "three"]:
        result = ec.call_function(int, value)
        print(value, result)
# Demonstrates calling the `int` function on each element in the list.
# If an exception occurs, it is captured, and None is returned.
# This allows for easy comparison and assertion without manual try-except blocks.
```

This updated documentation provides comprehensive guidance on utilizing `exception_capturer` for both capturing exceptions in a block and calling functions with automatic exception handling.

### Raising Captured Exceptions Manually

If you prefer to control when the captured exceptions are raised, you can use the `ec.raise_exceptions()` method. This allows you to attempt multiple operations, capture their exceptions, and then programmatically decide when to raise them all together.

```python
from exception_capturer import ExceptionCapturer

ec = ExceptionCapturer()

for value in ["one", "2", "three"]:
    with ec.capture():
        int(value)

# Manually raise all captured exceptions as an ExceptionGroup
ec.raise_exceptions()
```

## Features

- **Exception Aggregation**: Efficiently captures and aggregates multiple exceptions, allowing them to be raised as a single `ExceptionGroup`.
- **Flexible Control**: Provides flexibility in managing exceptions, enabling you to raise all captured exceptions at a point of your choosing.
- **Simplified Error Handling**: Simplifies the process of handling multiple potential error sources, making your code cleaner and more readable.

## Example Use Cases

- Processing batches of data where errors in individual items should not immediately halt the entire process.
- Performing multiple independent operations that may fail, with the intent to handle all errors collectively afterward.
