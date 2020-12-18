__author__ = 'Igor Nikolaev'

import pytest

from model.group import Group
from comtypes.client import CreateObject
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

xl = CreateObject("Excel.Application")
xl.Visible = 0
wb = xl.Workbooks.Open(os.path.join(project_dir, "groups.xlsx"))
testdata = list()
for i in range(10):
    testdata.append(Group(id=xl.Range["A%s" % (i + 1)].Value[()], name=xl.Range["B%s" % (i+1)].Value[()]))
xl.Quit()


@pytest.mark.parametrize("group", testdata)
def test_add_group(app, group):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list, key=Group.name) == sorted(new_list, key=Group.name)