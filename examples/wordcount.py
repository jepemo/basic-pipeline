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
import sys; sys.path.append("../")
import re
from bpipe import pipe

TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam elit
ipsum, malesuada lacinia justo id, luctus dignissim nibh. Proin feugiat dapibus
metus non auctor. Sed sodales velit sed pellentesque lacinia. Morbi non elit et
risus interdum interdum. Sed varius turpis a enim volutpat consequat. Donec ut
risus efficitur, maximus elit in, tempor tellus. Proin vitae tellus quis eros
rutrum facilisis."""
TEXT1 = """Hola como, estas hola"""
TEXT2 = """Hola como, eres hola"""

p = pipe([TEXT1], debug=False) \
    .map(lambda t: re.sub("[^0-9a-zA-Z]+", " ", t)) \
    .map(lambda t: t.lower()) \
    .map(lambda t: t.split()) \
    .flatten() \
    #.map(lambda t: t.lower()) \
    #.map(lambda t: "[{0}]".format(t)) \

for e in p:
    print(e)
