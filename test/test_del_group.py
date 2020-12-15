__author__ = 'Igor Nikolaev'


def test_del_group(app):
    old_list = app.groups.get_group_list()
    app.groups.delete_first_group()
    new_list = app.groups.get_group_list()
    old_list.append("my group")
    assert sorted(old_list) == sorted(new_list)