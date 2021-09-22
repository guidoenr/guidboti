from datetime import datetime as dt

INFO = "[INFO]{}: {}"
OK = "[OK]{}: {}"
WARNING = "[WARNING]{}: {}"
ERROR = "[ERROR]{}: {}"
CRITICAL = "[CRITICAL]{}: {}"


def log_info(message):
    print(INFO.format(dt.now(), message))


def log_warning(message):
    print(WARNING.format(dt.now(), message))


def log_error(message):
    print(ERROR.format(dt.now(), message))


def log_ok(message):
    print(OK.format(dt.now(), message))


def log_critical(message):
    print(CRITICAL.format(dt.now(), message))
