"""
## Statistic Util Module

モジュールあるのに使えないアホ向けの関数群や
あるとちょっと便利なもの軍です。

:copyright: (C) 2022 TEAM Nekozouneko
:license: GNU GPLv3, ./LICENSEや`__license__`を見よう
"""

from .Config import config
from .Console import console
from .Logging import log, LogLevel

__author__ = "Taitaitatata"
__copyright__ = "Copyright 2022 TEAM Nekozouneko"
__license__ = "GNU General Public License v3"
__repository__ = "https://github.com/TEAMNekozouneko/StatisticBot"
__title__ = "Statistic Util"
__version__ = "1.0.1"

def getVersion():
    return __version__

def getCopyright():
    return __copyright__