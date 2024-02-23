from contextlib import contextmanager


class ExceptionCapturer(object):
    def __init__(self):
        self.captured_exceptions = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.captured_exceptions.append(exc_val)

        self.raise_exceptions()
        return False

    @contextmanager
    def capture(self):
        try:
            yield
        except Exception as e:
            self.captured_exceptions.append(e)

    def raise_exceptions(self):
        if self.captured_exceptions:
            raise ExceptionGroup(
                "ExceptionCapturer captured multiple exceptions",
                self.captured_exceptions,
            )
