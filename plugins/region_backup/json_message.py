import re

from mcdreforged.api.rtext import *

color_and_style_dict = {
    "§k": [RStyle.obfuscated, "style"],
    "§1": [RColor.dark_blue, "color"],
    "§l": [RStyle.bold, "style"],
    "§m": [RStyle.strikethrough, "style"],
    "§n": [RStyle.underlined, "style"],
    "§o": [RStyle.italic, "style"],
    "§0": [RColor.black, "color"],
    "§2": [RColor.dark_green, "color"],
    "§3": [RColor.dark_aqua, "color"],
    "§4": [RColor.dark_red, "color"],
    "§5": [RColor.dark_purple, "color"],
    "§6": [RColor.gold, "color"],
    "§7": [RColor.gray, "color"],
    "§8": [RColor.dark_gray, "color"],
    "§9": [RColor.blue, "color"],
    "§a": [RColor.green, "color"],
    "§b": [RColor.aqua, "color"],
    "§c": [RColor.red, "color"],
    "§d": [RColor.light_purple, "color"],
    "§e": [RColor.yellow, "color"],
    "§f": [RColor.white, "color"],
    "§r": [RColor.reset, "color"]

}

action_dict = {
    "ou": RAction.open_url,
    "rc": RAction.run_command,
    "sc": RAction.suggest_command,
    "cc": RAction.copy_to_clipboard,
    "of": RAction.open_file,
    "open_url": RAction.open_url,
    "run_command": RAction.run_command,
    "suggest_command": RAction.suggest_command,
    "copy_to_clipboard": RAction.copy_to_clipboard,
    "open_file": RAction.open_file
}


class Message:

    @staticmethod
    def apply_styles(obj, style_lst):
        if style_lst:
            obj.set_styles(style_lst)

    @staticmethod
    def apply_color_and_style_dict(node, obj, color_and_style_dict):
        key = node.strip()
        if key in color_and_style_dict:
            value, node_type = color_and_style_dict[key]
            if node_type == "color":
                obj.set_color(value)
            elif node_type == "style":
                style_lst = [value]
                Message.apply_styles(obj, style_lst)

    @staticmethod
    def apply_action_dict(node, obj, action_dict):
        key, value = node.split("=", maxsplit=1)[0].strip(), node.split("=", maxsplit=1)[1]
        if key in action_dict:
            obj.set_click_event(action_dict[key], value)
        elif key in ["st", "show_text"]:
            obj.set_hover_text(value)

    @staticmethod
    def add_obj_list(code, text, obj_list, flag):
        for i, (code_line, text_line) in enumerate(zip(code, text)):
            obj = RText(text_line + "\n") if i == len(code) - 1 and flag > 1 else RText(text_line)
            style_lst = []
            for node in code_line.split("<>"):
                if node.strip():
                    Message.apply_color_and_style_dict(node, obj, color_and_style_dict)
                    Message.apply_action_dict(node, obj, action_dict)
            Message.apply_styles(obj, style_lst)
            obj_list.append(obj)

    @classmethod
    def get_json_str(cls, text, prefix="#"):
        if text:
            obj_list = RTextList()
            lines = text.splitlines()
            for index, msg in enumerate(lines):
                flag = len(lines) - index
                code = re.findall(f"{prefix}(.*?){prefix}", msg, re.S)
                text = [i for i in re.split(f"{prefix}.*?{prefix}", msg, re.S) if i]

                if len(text) == len(code):
                    Message.add_obj_list(code, text, obj_list, flag)

                elif len(text) - len(code) == 1 and len(code) > 0:
                    obj = RText(text[0])
                    obj_list.append(obj)
                    text.pop(0)

                    Message.add_obj_list(code, text, obj_list, flag)

                else:
                    obj = RText(msg + '\n') if flag > 1 else RText(msg)
                    obj_list.append(obj)

            return obj_list
