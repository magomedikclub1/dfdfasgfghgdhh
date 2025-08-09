import sys
from aiologger import Logger
from aiologger.handlers.streams import AsyncStreamHandler
from aiologger.formatters.base import Formatter


class Log:
    _logger = None

    @classmethod
    def get_logger(cls, name="main"):
        if cls._logger is None:
            handler = AsyncStreamHandler(stream=sys.stdout)
            handler.formatter = Formatter(
                fmt="%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%d.%m.%Y_%H:%M:%S"
            )

            logger = Logger(name=name, handlers=[])
            logger.handlers.append(handler)

            cls._logger = logger

        return cls._logger
