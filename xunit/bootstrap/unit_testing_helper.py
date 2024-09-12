import logging

logging.basicConfig(level=logging.INFO,)

class TestUtils:
    test_case_count: int = 0


    @staticmethod
    def assert_raises(expected_exception, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except expected_exception as e:
            print(f"Passed: {expected_exception.__name__} was raised. Message: {str(e)}")
            return True
        except Exception as e:
            print(f"Failed: An unexpected exception {e.__class__.__name__} was raised. Message: {str(e)}")
            raise AssertionError("from AssertRaises unexpected exception")
        else:
            print(f"Failed: {expected_exception.__name__} was not raised")
            raise AssertionError("from AssertRaises unrecognisable exception ")

    @staticmethod
    def warning_message(message: str):
        if TestUtils.test_case_count < 1:
            logging.warning(message)
            TestUtils.test_case_count = TestUtils.test_case_count + 1



"""
Example usage of TestUtils.assert_raises static method.

Classes:
    SetupFailedException: Custom exception class for testing purposes.

Functions:
    test_broken_setup: Function that raises SetupFailedException.
    main: Entry point for running the example test.

Example:
    >>> from your_module_name import TestUtils    # Ensure you replace 'your_module_name' with the actual module name
    >>> class SetupFailedException(Exception):
    >>>     pass
    >>> 
    >>> def test_broken_setup():
    >>>     raise SetupFailedException("Setup failed")
    >>> 
    >>> def main():
    >>>     # Test for SetupFailedException using the TestUtils assert_raises static method
    >>>     TestUtils.assert_raises(SetupFailedException, test_broken_setup)
    >>> 
    >>> if __name__ == "__main__":
    >>>     main()
"""