from unittest import TestCase
from nose.tools import eq_
#from sieve.operators import assert_eq_xml

from tw2.jqplugins.sizeeq import SizeEQInstaller


class TestWidgets(TestCase):

    def test_widget(self):
        test = SizeEQInstaller()
        eq_(test.display(selector="div.sizeeq", eq_width=False), "")
