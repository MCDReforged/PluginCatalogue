import os
import time
import shutil
import datetime
import codecs
import json

from mcdreforged.api.all import *
from region_backup.json_message import Message
from region_backup.config import rb_info, rb_config

Prefix = '!!rb'
# 默认的插件配置文件
cfg = rb_config.get_default().serialize()
# 默认的备份总文件夹
backup_path = "./rb_multi"
# 默认的备份文件夹位置
slot_path = "./rb_multi/slot{0}"
# 默认的服务端存档位置
world_path = "./server/world"
# 地狱，末地世界区域文件位置
dim_dict = {"the_nether": "DIM-1", "the_end": "DIM1"}
# 全局分享列表
data_list = []
# 用户
user = None
# 备份状态符
backup_state = None
# 槽位默认数量
slot = 5
# 回档状态符
back_state = None
# 回档槽位
back_slot = None

help_msg = '''
------ {1} {2} ------
一个以区域为单位的§a备份回档§a插件
§3作者：FRUITS_CANDY
§d【格式说明】
#sc=!!rb<>st=点击运行指令#§7{0} §a§l[▷] §e显示帮助信息
#sc=!!rb make<>st=点击运行指令#§7{0} make §b<区块半径> <注释> §a§l[▷] §e以玩家所在区块为中心，备份边长为2倍半径+1的区块所在区域
#sc=!!rb pos_make<>st=点击运行指令#§7{0} pos_make §b<x1坐标> <z1坐标> <x2坐标> <z2坐标> <维度:0主世界,-1地狱,1末地> <注释> §a§l[▷] §e给定两个坐标点，备份以两坐标点对应的区域坐标为顶点形成的矩形区域
#sc=!!rb back<>st=点击运行指令#§7{0} back §b<槽位> §a§l[▷] §e回档指定槽位所对应的区域
#sc=!!rb del<>st=点击运行指令#§7{0} del §b<槽位> §a§l[▷] §e删除某槽位
#sc=!!rb confirm<>st=点击运行指令#§7{0} confirm §a§l[▷] §e再次确认是否回档
#sc=!!rb abort<>st=点击运行指令#§7{0} abort §a§l[▷] §e在任何时候键入此指令可中断回档
#sc=!!rb list<>st=点击运行指令#§7{0} list §a§l[▷] §e显示各槽位的存档信息
#sc=!!rb reload<>st=点击运行指令#§7{0} reload §a§l[▷] §e重载插件
'''.format(Prefix, "Region BackUp", "1.0.0")


def print_help_msg(source: CommandSource):
    source.reply(Message.get_json_str(help_msg))


@new_thread("rb_make")
def rb_make(source: InfoCommandSource, dic: dict):
    global backup_state, user
    try:
        if not source.get_info().is_player:
            source.reply("§c§l该指令只能由玩家输入!")
            return
        if backup_state is None:
            backup_state = False
            text = dic["r_comment"]
            lst = text.split()

            r = int(lst[0])

            if r < 0:
                source.reply("§c备份半径应为大于等于0的整数!")
                backup_state = None
                return

            source.get_server().broadcast("[RBU] §a备份§f中...请稍等")
            t1 = time.time()
            get_user_info(source)
            while len(data_list) < 4:
                time.sleep(0.01)

            data = data_list.copy()
            data_list.clear()
            backup_pos = get_backup_pos(r, int(data[2][0] // 16), int(data[2][2] // 16))
            data[0] = source.get_info().player
            data[1] = source.get_info().content

            # 保存游戏
            source.get_server().execute("save-off")
            while backup_state != 1:
                time.sleep(0.01)

            source.get_server().execute("save-all flush")
            while backup_state != 2:
                time.sleep(0.01)

            user = None
            valid_pos = search_valid_pos(data[-1], backup_pos)

            rename_slot()

            copy_files(valid_pos, data[-1])

            make_info_file(data=data)

            t2 = time.time()
            source.get_server().broadcast(f"[RBU] §a备份§f完成，耗时§6{(t2 - t1):.2f}§f秒")
            source.get_server().broadcast(
                f"[RBU] 日期: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}; 注释: {text.split(maxsplit=1)[-1] if len(text.split()) > 1 else '§7空'}")

            source.get_server().execute("save-on")
            backup_state = None
            return

    except Exception as e:
        user = None
        backup_state = None
        source.reply(f"备份出错,错误信息:§c{e}")
        source.get_server().execute("save-on")
        return

    source.reply("§c§l备份正在进行,请不要重复备份!")


@new_thread("rb_pos_make")
def rb_pos_make(source: InfoCommandSource, dic: dict):
    global backup_state, user
    try:

        if backup_state is None:
            backup_state = False
            x1, z1, x2, z2 = dic["x1"], dic["z1"], dic["x2"], dic["z2"]

            text = dic["dim_comment"]
            lst = text.split()

            dim = int(lst[0])

            if dim == 0:
                dim = "overworld"

            elif dim == 1:
                dim = "the_end"

            else:
                dim = "the_nether"

            source.get_server().broadcast("[RBU] §a备份§f中...请稍等")
            t1 = time.time()

            backup_pos = get_backup_pos(pos_list=[(int(x1 // 512), int(x2 // 512)), (int(z1 // 512), int(z2 // 512))])
            user = source.get_info().is_user
            # 保存游戏
            source.get_server().execute("save-off")
            while backup_state != 1:
                time.sleep(0.01)

            source.get_server().execute("save-all flush")
            while backup_state != 2:
                time.sleep(0.01)
            user = None
            valid_pos = search_valid_pos(dim, backup_pos)

            if all(not v for v in valid_pos.values()):
                backup_state = None
                source.reply("§c本次备份无效,根据输入的坐标,未找到对应的区域")
                source.get_server().execute("save-on")

            rename_slot()

            copy_files(valid_pos, dim)

            make_info_file(backup_dim=dim,
                           user_=source.get_info().player if source.get_info().player else "from_console",
                           cmd=source.get_info().content,
                           cmt="§7空" if len(text.split()) < 2 else text.split(maxsplit=1)[-1]
                           )

            t2 = time.time()
            source.get_server().broadcast(f"[RBU] §a备份§f完成，耗时§6{(t2 - t1):.2f}§f秒")
            source.get_server().broadcast(
                f"[RBU] 日期: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}; 注释: {text.split(maxsplit=1)[-1] if len(text.split()) > 1 else '§7空'}")

            source.get_server().execute("save-on")
            backup_state = None
            return

    except Exception as e:
        user = None
        backup_state = None
        source.reply(f"备份出错,错误信息:§c{e}")
        source.get_server().execute("save-on")
        return

    source.reply("§c§l备份正在进行,请不要重复备份!")


# 玩家信息类型有如下两种 坐标，即Pos 维度，即Dimension
@new_thread("user_info")
def get_user_info(source):
    global user, data_list

    user = source.get_info().player

    if user:

        source.get_server().execute(f"data get entity {user} Pos")
        source.get_server().execute(f"data get entity {user} Dimension")

        while len(data_list) < 2:
            time.sleep(0.01)

        data_list.append([float(pos.strip('d')) for pos in data_list[0].strip("[]").split(',')])
        data_list.append(data_list[1].replace("minecraft:", "").strip('"'))


@new_thread("rb_back")
def rb_back(source: InfoCommandSource, dic: dict):
    global back_state, back_slot
    # 判断槽位非空
    if not os.path.exists(os.path.join(slot_path.format(dic["slot"]), "info.json")):
        source.reply("§c该槽位无info.json文件,无法回档")
        return

    if not get_file_size([os.path.join(slot_path.format(dic["slot"]), "entities"),
                          os.path.join(slot_path.format(dic["slot"]), "poi"),
                          os.path.join(slot_path.format(dic["slot"]), "region")])[-1]:
        source.reply("§c该槽位无区域文件,无法回档")
        return

    try:

        if back_state is None:

            back_state = 0
            # 等待确认
            with codecs.open(os.path.join(slot_path.format(dic["slot"]), "info.json"), encoding="utf-8-sig") as fp:
                info = json.load(fp)
                t = info["time"]
                cmt = info["comment"]

            source.reply(Message.get_json_str("\n".join([f"[RBU] 准备将存档恢复至槽位§6{dic['slot']}§f，日期 {t}; 注释: {cmt}",
                                                         "[RBU] 使用#sc=!!rb confirm<>st=点击确认#§7!!rb confirm "
                                                         "§f确认§c回档§f，#sc=!!rb abort<>st=点击取消#§7!!qb abort §f取消"])))

            while not back_state:
                time.sleep(0.01)

            if back_state is True:
                source.reply("§a回档已取消")
                back_state = None
                return
            # 提示

            source.get_server().broadcast("§c服务器将于10秒后关闭回档!")
            for stop_time in range(1, 10):
                time.sleep(1)
                if back_state is True:
                    back_state = None
                    source.reply("§a回档已取消")
                    return
                source.get_server().broadcast(Message.get_json_str("\n".join(
                    [f"§a服务器还有{10 - stop_time}秒关闭，输入#sc=!!rb abort<>st=终止回档#§c!!rb abort§f来停止回档到槽位§6{dic['slot']}"])))

            back_slot = dic["slot"]
            # 停止服务器
            source.get_server().stop()
            back_state = None
            return

    except Exception as e:
        back_state = back_slot = None
        source.reply(f"回档出错,错误信息:§c{e}")
        return

    source.reply("§c§l回档正在进行,请不要重复回档!")


def on_server_stop(server: PluginServerInterface, server_return_code: int):
    global back_slot

    try:
        if back_slot:
            if server_return_code != 0:
                server.logger.error("服务端关闭异常,回档终止")
                return

            server.logger.error("正在运行文件替换")
            extra_slot = f"{backup_path}/overwrite"
            if os.path.exists(extra_slot):
                shutil.rmtree(extra_slot)
            os.makedirs(extra_slot)
            os.makedirs(extra_slot + "/entities")
            os.makedirs(extra_slot + "/region")
            os.makedirs(extra_slot + "/poi")

            with codecs.open(os.path.join(slot_path.format(back_slot), "info.json"), encoding="utf-8-sig") as fp:
                info = json.load(fp)
                dim = info["backup_dimension"]
                if dim in dim_dict:
                    path = os.path.join(world_path, dim_dict[dim])

                else:
                    path = world_path

            for backup_file in ["entities", "region", "poi"]:
                if get_file_size([os.path.join(slot_path.format(back_slot), backup_file)])[-1]:
                    lst = os.listdir(os.path.join(slot_path.format(back_slot), backup_file))
                    for i in lst:
                        shutil.copy2(os.path.join(path, backup_file, i), os.path.join(extra_slot, backup_file, i))

                        shutil.copy2(os.path.join(slot_path.format(back_slot), backup_file, i),
                                     os.path.join(path, backup_file, i))

            back_slot = None

            server.start()

    except Exception as e:
        back_slot = None
        server.logger.error(f"回档出错,错误信息:§c{e}")
        return


def rb_del(source: CommandSource, dic: dict):
    try:
        # 获取文件夹地址
        s = slot_path.format(dic['slot'])
        # 删除整个文件夹
        if os.path.exists(s):
            shutil.rmtree(s, ignore_errors=True)
            source.reply(f"§4§l槽位{dic['slot']}删除成功")
            return

        source.reply(f"§4§l槽位{dic['slot']}不存在")

    except Exception as e:
        for i in range(1, slot + 1):
            os.makedirs(slot_path.format(i), exist_ok=True)
        source.reply(f"删除备份时出错,错误信息:§c{e}")
        return


def rb_abort():
    global back_state
    # 当前操作备份信息
    back_state = True


def rb_confirm():
    global back_state
    back_state = 1


def rb_list(source: CommandSource):
    try:
        slot_list = [_slot for _slot in os.listdir(backup_path) if
                     _slot.startswith("slot") and os.path.isdir(backup_path + rf"/{_slot}")]

        if not slot_list:
            source.reply("没有槽位存在")
            return

        slots = sorted(slot_list, key=lambda x: int(x.replace("slot", "")))

        msg_list = ["§d【槽位信息】"]

        total_size = 0

        for i in slots:
            s = i.strip('slot')
            json_path = os.path.join(backup_path, i, "info.json")
            if os.path.exists(json_path):
                with codecs.open(json_path, "r", "utf-8-sig") as fp:

                    info = json.load(fp)

                    if info:
                        t = info["time"]
                        cmt = info["comment"]
                        dim = info['backup_dimension']
                        size = get_file_size([os.path.join(backup_path, i)])
                        total_size += size[-1]

                        msg = f"#st=备份维度:{dim}#[槽位§6{s}§f] #sc=!!rb back {s}<>st=回档至槽位§6{s}#§a[▷] #sc=!!rb " \
                              f"del {s}<>st=删除槽位§6{s}#§c[x] ##§a{size[0]} §f{t} 注释: {cmt}"

                        msg_list.append(msg)
            else:
                msg = f"[槽位§6{s}§f] 空"
                msg_list.append(msg)

        if not total_size:
            msg_list.append("备份占用总空间: 无")

        else:
            msg_list.append(f"备份占用总空间: §a{convert_bytes(total_size)}")

        source.reply(Message.get_json_str("\n".join(msg_list)))

    except Exception as e:
        source.reply(f"显示备份列表出错,错误信息:§c{e}")
        return


def get_file_size(folder_list):
    total_size = 0
    for directory in folder_list:

        for dirpath, dirnames, filenames in os.walk(directory):

            for filename in filenames:

                file_path = os.path.join(dirpath, filename)
                # 确保文件存在
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)

    return convert_bytes(total_size), total_size


def convert_bytes(size_in_bytes):
    """将字节转换为更易读的单位"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f}{x}"
        size_in_bytes /= 1024.0


def rb_reload(source: CommandSource):
    try:
        source.get_server().reload_plugin("region_backup")
        source.reply("§a§l插件已重载")
    except Exception as e:
        source.reply(f"重载插件失败: §c§l{e}")


def on_unload(server: PluginServerInterface):
    global user, back_state, backup_state, back_slot
    user = backup_state = back_state = back_slot = None


def get_backup_pos(r=None, x=None, z=None, pos_list=None):
    backup_pos = []

    if not pos_list:

        return get_backup_pos(pos_list=[((x - r)//32, (x + r)//32), ((z + r)//32, (z - r)//32)])

    left = min(pos_list[0])
    right = max(pos_list[0])
    top = max(pos_list[-1])
    bottom = min(pos_list[-1])

    for x in range(left, right + 1):
        for z in range(bottom, top + 1):
            backup_pos.append((x, z))

    return backup_pos


def check_folder():
    if not os.path.exists("./config/Region_BackUp.json"):
        with codecs.open("./config/Region_BackUp.json", "w", encoding="utf-8-sig") as fp:
            json.dump(cfg, fp, ensure_ascii=False, indent=4)

    os.makedirs(backup_path, exist_ok=True)


def make_info_file(data=None, backup_dim=None, user_=None, cmd=None, cmt=None):
    file_path = os.path.join(slot_path.format(1), "info.json")

    info = rb_info.get_default().serialize()
    info["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info["backup_dimension"] = data[-1] if not backup_dim else backup_dim
    info["user_dimension"] = data[-1] if not backup_dim else "无"
    info["user"] = data[0] if not user_ else user_
    info["user_pos"] = ",".join(str(pos) for pos in data[2]) if not user_ else "无"
    info["command"] = data[1] if not cmd else cmd
    if not cmt:
        if len(data[1].split(maxsplit=2)[-1].split()) > 1:
            info["comment"] = data[1].split(maxsplit=3)[-1]

        else:
            info["comment"] = "§7空"

    else:
        info["comment"] = cmt

    with codecs.open(file_path, "w", encoding="utf-8-sig") as fp:
        json.dump(info, fp, ensure_ascii=False, indent=4)


def rename_slot():
    try:
        shutil.rmtree(slot_path.format(slot), ignore_errors=True)
        if slot > 1:
            for i in range(slot - 1, 0, -1):
                os.rename(slot_path.format(i), slot_path.format(i + 1))

        os.makedirs(slot_path.format(1))

    except:
        for i in range(1, slot + 1):
            os.makedirs(slot_path.format(i), exist_ok=True)


def copy_files(valid_pos, data):
    if data in dim_dict:
        path = os.path.join(world_path, dim_dict[data])

    else:
        path = world_path

    time.sleep(0.1)

    for folder, positions in valid_pos.items():
        # 获取坐标的横纵坐标值
        if not positions:
            continue

        os.makedirs(os.path.join(slot_path.format(1), f"{folder}"), exist_ok=True)
        for pos in positions:
            x, z = pos
            file_path = os.path.join(path, folder, f"r.{x}.{z}.mca")
            shutil.copy2(file_path, os.path.join(slot_path.format(1), folder, f"r.{x}.{z}.mca"))


def search_valid_pos(data, backup_pos):
    valid_pos = {"region": [], "poi": [], "entities": []}

    if data in dim_dict:
        path = os.path.join(world_path, dim_dict[data])

    else:
        path = world_path

    for folder, positions in valid_pos.items():
        for pos in backup_pos:
            x, z = pos
            file = os.path.join(path, folder, f"r.{x}.{z}.mca")

            if os.path.exists(file):
                positions.append(pos)

    return valid_pos


def on_info(server: PluginServerInterface, info: Info):
    global backup_state
    if user:

        if info.content.startswith(f"{user} has the following entity data: ") and info.is_from_server:
            data_list.append(info.content.split(sep="entity data: ")[-1])
            return

        if info.content.startswith("Saved the game") and info.is_from_server:
            backup_state = 2
            return

        if info.content.startswith("Automatic saving is now disabled") and info.is_from_server:
            backup_state = 1
            return


def on_load(server: PluginServerInterface, old):
    global cfg, backup_path, slot_path, world_path, slot

    check_folder()

    for i in range(1, slot + 1):
        os.makedirs(slot_path.format(i), exist_ok=True)

    with codecs.open("./config/Region_BackUp.json", encoding="utf-8-sig") as fp:
        cfg = json.load(fp)

    backup_path = cfg["backup_path"]
    world_path = cfg["world_path"]
    slot_path = backup_path + "/slot{0}"
    slot = cfg["slot"]

    level_dict = cfg["minimum_permission_level"]

    require = Requirements()

    server.register_help_message('!!rb', '查看与区域备份有关的指令')

    builder = SimpleCommandBuilder()

    builder.command("!!rb", print_help_msg)
    builder.command("!!rb make <r_comment>", rb_make)
    builder.command("!!rb pos_make <x1> <z1> <x2> <z2> <dim_comment>", rb_pos_make)
    builder.command("!!rb back <slot>", rb_back)
    builder.command("!!rb confirm", rb_confirm)
    builder.command("!!rb del <slot>", rb_del)
    builder.command("!!rb abort", rb_abort)
    builder.command("!!rb list", rb_list)
    builder.command("!!rb reload", rb_reload)

    builder.arg("r_comment", GreedyText)
    builder.arg("x1", Number)
    builder.arg("z1", Number)
    builder.arg("x2", Number)
    builder.arg("z2", Number)
    builder.arg("dim_comment", GreedyText)
    builder.arg("slot", Integer)

    command_literals = ["make", "pos_make", "back", "confirm", "del", "abort", "list", "reload"]

    for literal in command_literals:
        permission = level_dict[literal]
        builder.literal(literal).requires(require.has_permission(permission),
                                          failure_message_getter=lambda err: "你没有运行该指令的权限")

    builder.register(server)
