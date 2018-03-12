#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bpipe - Minimal & Simple Pipeline for Python
#
# Copyright (C) 2017-present Jeremies Pérez Morata
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re
from bpipe import pipe

TEXT = """In a village of La Mancha, the name of which I have no desire to call
to mind, there lived not long since one of those gentlemen that keep a lance in
the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.
"""

p = pipe([TEXT], debug=True) \
    .map(lambda t: re.sub("[^0-9a-zA-Z]+", " ", t)) \
    .map(lambda t: t.lower()) \
    #.map(lambda t: t.split()) \
    #.flatten() \
    #.map(lambda t: t.lower()) \
    #.map(lambda t: "[{0}]".format(t)) \

for e in p:
    print("OUT:", e)
