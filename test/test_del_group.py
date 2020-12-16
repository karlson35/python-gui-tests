__author__ = 'Igor Nikolaev'

import random


def test_del_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    random_group = random.choice(app.groups.get_group_list())
    app.groups.delete_group(random_group)
    new_list = app.groups.get_group_list()
    old_list.remove(random_group)
    assert sorted(old_list) == sorted(new_list)