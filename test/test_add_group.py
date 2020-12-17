__author__ = 'Igor Nikolaev'

from model.group import Group


def test_add_group(app):
    group = Group(name="my group")
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)