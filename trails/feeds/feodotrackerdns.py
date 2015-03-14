#!/usr/bin/env python

"""
Copyright (c) 2014-2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content
from core.enums import TRAIL

__type__ = (TRAIL.DNS,)
__url__ = "https://feodotracker.abuse.ch/blocklist/?download=domainblocklist"
__check__ = "Feodo"
__info__ = "feodo"
__reference__ = "feodotracker.abuse.ch"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            retval[TRAIL.DNS][line] = (__info__, __reference__)

    return retval