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
from bpipe.pipe import Pipe


def echo(str_input):
    p = Pipe([str_input])
    l = list(p)
    for e in l:
        print(e)
    return p


def map_to(func):
    p = Pipe(None)
    p.steps.append(func)
    return p


def cat(filename):
    reader = open(filename, 'r')
    return pipe(reader.readlines())
