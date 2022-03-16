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

__author__ = "Taitaitatata (TEAM Nekozouneko)"
__copyright__ = "Copyright 2022 TEAM Nekozouneko"
__license__ = "GNU General Public License (GNU GPLv3)"
__repository__ = "https://github.com/TEAMNekozouneko/StasticBot"
__title__ = "Statisitc Util"
__version__ = "1.0.0-rc3"

def getVersion():
    return __version__

def getCopyright():
    return __copyright__