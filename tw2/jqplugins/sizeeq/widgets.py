# -*- coding: utf-8 -*-
#
# tw2.jqplugins.sizeeq.widgets
#
# Copyright © 2016 Nils Philippsen <nils@tiptoe.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import absolute_import, unicode_literals

from tw2.core import Param, Widget, js_function
from tw2.jquery import jquery_js

from .resources import sizeeq_js

__all__ = ('SizeEQInstaller',)


class SizeEQInstaller(Widget):

    resources = [jquery_js, sizeeq_js]

    template = ""

    selector = Param("Selector for elements to be managed.")

    eq_width = Param("Whether to equalize element widths.", default=True)

    eq_height = Param("Whether to equalize element heights.", default=True)

    def prepare(self):
        super(SizeEQInstaller, self).prepare()

        call = js_function('install_sizeeq')(self.selector, self.eq_width,
                                             self.eq_height)
        self.add_call(call)

    def generate_output(self, displays_on):
        return ""
