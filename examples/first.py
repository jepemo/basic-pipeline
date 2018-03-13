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
from bpipe import Pipe, flat_map, pipe

#print(list(pipe(range(0, 5), debug=True).map(lambda x: x ** 2)))

param = [[1, 2,], [3, 4]]
result = [2, 3, 4, 5]
trans = lambda x: x+1
p1 = Pipe(param, debug=True).flat_map(trans)
#p2 = Pipe(param) | flat_map(trans)
r1 = list(p1)
#r2 = list(p2)

print(r1)
