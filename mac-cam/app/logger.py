#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import sys
import settings


class Logger(logging.getLoggerClass()):

    def __init__(self):
        logging.getLoggerClass().__init__(self, None)
        logging_level = logging.getLevelName(settings.LOG_LEVEL)

        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

        self.file_handler = RotatingFileHandler(settings.LOG_NAME,
                                                maxBytes=settings.LOG_MAX_BYTES,
                                                backupCount=settings.LOG_BACKUP_COUNT)
        self.file_handler.setLevel(logging_level)
        self.file_handler.setFormatter(formatter)

        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setLevel(logging_level)
        self.console_handler.setFormatter(formatter)

        self.addHandler(self.file_handler)
        self.addHandler(self.console_handler)


LOGGER = Logger()
