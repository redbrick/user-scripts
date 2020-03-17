"""help topics"""
from .chat import CHAT
from .chfn import CHFN
from .chsh import CHSH
from .email import EMAIL
from .hey import HEY
from .logout import LOGOUT
from .motd import MOTD
from .mud import MUD
from .news import NEWS
from .noforward import NOFORWARD
from .nohelp import NOHELP
from .passwd import PASSWD
from .rbusers import RBUSERS

HELP_TEXT = dict(
    chat=CHAT,
    chfn=CHFN,
    chsh=CHSH,
    email=EMAIL,
    hey=HEY,
    logout=LOGOUT,
    motd=MOTD,
    mud=MUD,
    news=NEWS,
    noforward=NOFORWARD,
    nohelp=NOHELP,
    passwd=PASSWD,
    rbusers=RBUSERS,
)
