import logging


def log_decorator(log_level):
    logging.basicConfig(filename='example.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Call the function and return its result
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                # Log an error message with the exception details
                logging.error(str(e))
                raise

        # Add log messages with the specified log level
        if log_level == 'info':
            logging.info(f"{func.__name__} is now being called")
        elif log_level == 'debug':
            logging.debug(f"{func.__name__} is now being called")
        elif log_level == 'error':
            logging.error(f"{func.__name__} is now being called")

        return wrapper

    return decorator
