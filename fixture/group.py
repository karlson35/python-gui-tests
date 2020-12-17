__author__ = 'Igor Nikolaev'

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        group_list = []
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        # group_list = [node.text() for node in root.children()]
        for node in enumerate(root.children()):
            group_list.append(Group(name=node[1].text(), id=node[0]))
        self.close_group_editor()
        return group_list

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group.name)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def delete_group_by_id(self, id):
        # self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        root.children()[id].click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group_window = self.app.application.window(title="Delete group")
        self.delete_group_window.wait("visible")
        self.delete_group_window.window(auto_id="uxDeleteAllRadioButton").click()
        self.delete_group_window.window(auto_id="uxOKAddressButton").click()
        # self.close_group_editor()

    def close_group_editor(self):
        self.group_editor.close()

    def delete_group(self, group):
        self.open_group_editor()
        self.delete_group_by_id(group.id)
        self.close_group_editor()