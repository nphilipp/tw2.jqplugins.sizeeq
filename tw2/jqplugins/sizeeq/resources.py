# -*- coding: utf-8 -*-
#
# tw2.jqplugins.sizeeq.resources
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

from tw2.core import JSLink

__all__ = ('sizeeq_js',)


class SizeEQLink(JSLink):

    modname = 'tw2.jqplugins.sizeeq'
    filename = "static/sizeeq.js"


sizeeq_js = SizeEQLink()
