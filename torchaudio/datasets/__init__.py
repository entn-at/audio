from .commonvoice import COMMONVOICE
from .librispeech import LIBRISPEECH
from .speechcommands import SPEECHCOMMANDS
from .utils import bg_iterator, diskcache_iterator
from .vctk import VCTK
from .gtzan import GTZAN
from .yesno import YESNO
from .ljspeech import LJSPEECH
from .cmuarctic import CMUARCTIC

__all__ = (
    "COMMONVOICE",
    "LIBRISPEECH",
    "SPEECHCOMMANDS",
    "VCTK",
    "YESNO",
    "LJSPEECH",
    "GTZAN",
    "CMUARCTIC",
    "diskcache_iterator",
    "bg_iterator",
)
