from fontTools.misc.py23 import *
import logging
from fontTools.misc.loggingTools import configLogger

log = logging.getLogger(__name__)

version = __version__ = "4.4.3"

__all__ = ["version", "log", "configLogger"]
