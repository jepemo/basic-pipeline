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


class Pipe:
    def __init__(self, generator):
        """
        """
        self.generator = generator
        self.steps = []
        self.error_callback = None
        self.abort_on_error = False

    def peek(self):
        def _peek(x):
            print(x)
            return x

        self.steps.append(_peek)
        return self

    def next(self, step):
        self.steps.append(step)
        return self

    def error(self, error_callback, abort_on_error=False):
        self.error_callback = error_callback
        self.abort_on_error = abort_on_error
        return self

    def run(self):
        for x in self.generator:
            result = x
            for step in self.steps:
                result = step(result)

    def get(self):
        result = []

        def _get_result(x):
            result.append(x)
            return x

        self.steps.append(_get_result)
        self.run()
        return result
