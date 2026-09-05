**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## mirror_mcsmcdr

### Basic Information

- Plugin ID: `mirror_mcsmcdr`
- Plugin Name: MirrorMcsmcdR
- Version: 1.7.0
  - Metadata version: 1.7.0
  - Release version: 1.7.0
- Total downloads: 1242
- Authors: [tanh_Heng](https://github.com/tanhHeng)
- Repository: https://github.com/LazyAlienServer/MirrorMcsmcdR
- Repository plugin page: https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: A mirror server manager MCDR plugin, based on MCSManager.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.6.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [xxhash](https://pypi.org/project/xxhash) | \>=3 |

```
pip install "xxhash>=3"
```

### Introduction

# MirrorMcsmcdR

[![MCDR](https://img.shields.io/badge/MCDR-%E2%89%A52.6.0-blue)](https://github.com/Fallen-Breath/MCDReforged) [![License](https://img.shields.io/github/license/LazyAlienServer/MirrorMcsmcdR)](https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main/./LICENSE) [![Downloads](https://img.shields.io/github/downloads/LazyAlienServer/MirrorMcsmcdR/total)](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases)

[中文](https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main/./README.md) · English

> The most comprehensive [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) mirror server control plugin! Control mirror servers through multiple methods and synchronize additions and deletions based on hashes.

## Features

- **Multiple control and lifecycle methods**:
  - Control mirror servers through [MCSManager](https://github.com/MCSManager/MCSManager) (`MCSM-v9.9.0` `MCSM-v10.2.1+`)
  - Start and stop mirror servers directly through terminal proxies (`Linux` `Windows`), with the new terminal independent from the parent MCDR process
    - Linux uses `screen` to control the mirror server
    - Windows uses a new command prompt to control the mirror server
  - Stop mirror servers through RCON
  - Start mirror servers as child processes inside MCDR through `subprocess`, controlled through standard input and output
  - Send commands through `!!mirror execute <command>`
  - Combine multiple control methods, for example:
    - Start through Windows Terminal and stop through RCON
    - Start and stop through MCDR, then force-terminate through Linux when the mirror process fails
- **Comprehensive control features**: manage multiple mirror servers, inspect status, start, stop, force-terminate, and synchronize
- **Hash-based file synchronization**: synchronize only files that differ from the source server, improving speed and reducing disk I/O
- **Highly customizable configuration**: use YAML and write only changed values when configuring multiple mirror servers

> [!NOTE]
> This plugin does not provide server creation or management functionality. Please use it after creating the mirror server and its MCSManager instance. It also does not provide successful start/stop notifications; consider using a companion plugin such as vchat.

## Dependencies

| Dependency           | Description                                                                             |
| -------------------- | --------------------------------------------------------------------------------------- |
| Python               | `>=3.9`                                                                                 |
| Python package       | `xxhash>=3`                                                                             |
| Linux terminal proxy | [`screen`](https://www.gnu.org/software/screen/) when `proxy_type` is `linux` or `null` |

## Commands

The default command prefix is `!!mirror`.

| Command                               | Description                                             |
| ------------------------------------- | ------------------------------------------------------- |
| `!!mirror` / `!!mirror help`          | Display command help                                    |
| `!!mirror status`                     | Get the mirror server status                            |
| `!!mirror start`                      | Start the mirror server                                 |
| `!!mirror stop`                       | Stop the mirror server                                  |
| `!!mirror kill`                       | Terminate the mirror server                             |
| `!!mirror kill -f`                    | Force-terminate the mirror server (Linux terminal only) |
| `!!mirror sync`                       | Synchronize files                                       |
| `!!mirror confirm`                    | Confirm a pending operation                             |
| `!!mirror reload`                     | Hot-reload the mirror configuration                     |
| `!!mirror history`                    | View synchronization history                            |
| `!!mirror execute <command>`          | Send a command through the subprocess proxy             |
| `!!mirror log`                        | View subprocess console-log status                      |
| `!!mirror log enable|disable|<count>` | Enable, disable, or limit console-log output            |

## Configuration File

> [!TIP]
> This configuration file is long. We recommend reading the [Quick Start](https://github.com/LazyAlienServer/MirrorMcsmcdR/tree/main/./docs/quickstart_en.md) first, then using this document as a reference.

The configuration file supports hot reloading and automatic completion. When a new version adds an option, the plugin automatically fills in its default value in your old configuration file.


```yaml
"!!mirror":
    mcsm: # MCSManager configuration
    terminal: # Configuration for starting the mirror server terminal through the command line
    rcon: # RCON configuration
    sync: # Save synchronization configuration
    command:
        permission: # Command permission configuration
        action: # Command behavior configuration
    display: # Display configuration
```

### Mirror entries and inheritance

The first mirror entry is the base configuration. Later entries inherit its values and only need to contain overrides.

**Example**

Control mirror server 2 through `!!mirror2`, set its instance ID to `abc123`, and change its server name to `Mirror2`.
```yaml
"!!mirror":
    # ...
"!!mirror2":
    mcsm:
        uuid: "abc123"
    display:
        server_name: "Mirror2"
```

Alternatively, thanks to YAML, you can write it in a simpler form:
```yaml
"!!mirror":
    # ...
"!!mirror2":
    mcsm.uuid: "abc123"
    display.server_name: "Mirror2"
```

The parameters not set in `!!mirror2` automatically inherit from the first `!!mirror` entry. For example, an unset `mcsm.url` inherits `"http://127.0.0.1:23333/"` from `!!mirror`.

For a complete example, see [Multi-mirror Server Configuration File Example](#example-of-multi-mirror-server-configuration-file).

<br>

### mcsm: MCSManager Configuration
If you have any questions about this configuration section, please refer to the [MCSManager Documentation](https://docs.mcsmanager.com/#/zh-cn/apis/readme).
```yaml
mcsm:
    enable: false
    url: "http://127.0.0.1:23333/"
    uuid:
    remote_uuid:
    apikey:
```
After enabling MCSM, the terminal and RCON configurations will be disabled.


**enable** `bool`
- Whether to enable MCSM. You need to set this option to `true` after completing the configuration of this section.

**url** `str`
- The access address of the MCSManager panel, that is, the address for requesting the API.

**uuid** `str`
- The ID of the server instance, that is, the UID displayed by the instance.

**remote_uuid** `str`
- The ID of the remote node, that is, the GID displayed by the instance.

**apikey** `str`
- The key required to call the API interface, which can usually be viewed in the user interface.

<br>

### terminal: Configuration for starting the mirror server terminal through the command line
```yaml
terminal:
  enable: false
  launch_path: "./Mirror"
  launch_command: "python -m mcdreforged"
  port:
  terminal_name: "Mirror"
  regex_strict: false
  is_mcdr: true
  proxy_type:
  console_log: false
```
When `proxy_type` is `linux`, the plugin creates a new screen; when it is `windows`, it creates a new command prompt; and when it is `subprocess`, it starts the mirror server as a child process inside MCDR. The screen or terminal created by the Linux/Windows proxies is closed automatically after the mirror server stops.

> [!NOTE]
> If you cannot start the mirror server with this command, try the following steps. `terminal_name` and `launch_command` are the corresponding configuration values.
> 1. Execute `launch_command` under `launch_path` and confirm that it starts the mirror server successfully.
> 2. Linux users should check whether `screen` is installed. Windows users should check whether the `python` command works in the terminal.
> 3. If neither suggestion resolves the problem, execute the complete command for the Linux or Windows proxy in the current MCDR server's root directory and inspect the output.
>    - Linux: `cd "{launch_path}"&&screen -dmS {terminal_name}&&screen -x -S {terminal_name} -p 0 -X stuff "{launch_command}&&exit\n"`
>    - Windows: `cd "{launch_path}"&&start cmd.exe cmd /C python -c "import os;os.system('title {terminal_name}');os.system('{launch_command}')"`

Note: The `linux` proxy controls the mirror server through screen. With the `windows` proxy, `stop` sends `SIGINT` to the process listening on the configured mirror port and `kill` forcefully terminates it with `taskkill`. The `subprocess` proxy controls the mirror server through the child process's standard input and output. The Linux/Windows proxies require a correctly configured `port`; the subprocess proxy does not require `port`. MCSM or RCON can still be used as alternative control methods.

> [!WARNING]
> The `stop` command under the Windows proxy is experimental; use it at your own risk. Configure RCON whenever possible to avoid unnecessary operational overhead.

**enable** `bool`
- Whether to enable the terminal. When MCSM is not enabled and this option is `true`, the mirror server will be started through the selected terminal proxy.

**launch_path** `str`
- The path where the startup command is executed, usually the directory where the mirror server is located.

**launch_command** `str`
- The startup command that needs to be executed. If a simple startup command cannot meet your requirements, you can create a `.bat` (or `.sh`) file and write the startup command in it, then execute the file.

**port** `int | null`
- The mirror server port. The Linux and Windows proxies use it to check the server status and control the process; it is not required by the `subprocess` proxy.

**terminal_name** `str`
- The title of the new command prompt, the name of the new screen, or the prefix used for subprocess proxy log output.

**regex_strict** `bool`
- Whether the Linux or Windows proxies should continue to verify that the process name is `java.exe` after finding the configured port. Generally, there is no need to enable it.

**is_mcdr** `bool`
- Whether the mirror server is started by MCDReforged. Defaults to `true`. For the Linux proxy, `true` makes `stop` and `kill` send MCDR commands to screen; `false` makes `stop` send Minecraft's `stop` command and `kill` perform a force kill. For the subprocess proxy, `true` makes `stop` send `!!MCDR server stop_exit`, while `false` sends Minecraft's `stop` command; `kill` terminates the child process directly. The Windows proxy uses `SIGINT` for `stop` and `taskkill` for `kill`.

> [!IMPORTANT]
> `!!mirror kill -f` and `!!mirror kill --force` are only available for the Linux proxy or Linux/Windows+MCDR. They kill every process listening on the configured port, then close screen; confirm that `port` is correct before using them.

**proxy_type** `str | null`
- The terminal proxy type, replacing the legacy `system` option. Valid values are `linux`, `windows`, and `subprocess`. When set to `null`, the plugin automatically selects `linux` or `windows` based on the current operating system. `subprocess` starts the mirror server as a child process inside MCDR, does not require `port`, and supports sending commands through `!!mirror execute`.

> [!NOTE]
> When using the `subprocess` proxy to start another MCDR instance, set `advanced_console` to `false` in the mirror server MCDR's configuration file.

**console_log** `bool`
- Whether to output the subprocess proxy's mirror server console logs to the MCDR console by default. This option only applies to the `subprocess` proxy.

<br>
### rcon: RCON Configuration
```yaml
rcon:
    enable: false
    address: null
    port: null
    password: null
```
**enable** `bool`
- Whether to enable RCON. When MCSM is not enabled, the plugin will execute the `stop` command and obtain the status of the mirror server through RCON. If both RCON and the terminal are enabled at the same time, the plugin will first check the status of RCON to obtain the status of the mirror server. If RCON is not connected, it will check the status through the port. If the status of RCON does not match the status of the port, a prompt will be given.

**address** `str`
- The connection address of RCON, does not include the port.

**port** `int`
- The connection port of RCON

**password** `str`
- The connection password of RCON

<br>

### sync: Configuration file related to file synchronization
```yaml
sync:
    world:
        - "world"
    source: "./server"
    target:
        - "./Mirror/server"
    ignore_inexistent_target_path: false
    concurrency: 4
    ignore_files:
        - "session.lock"
```

In `sync`, `./` refers to the `MCDReforged` root directory where the server is located.

```
mcdr_root (./)
 ├─ config
 ├─ logs
 ├─ plugins
 ├─ server (./server)
 |   └─ world
 └─ Mirror
     └─ server (./Mirror/server)
         └─ world
```

**world** `list`
- The directory that needs to be synchronized, it needs to be added when there are multiple world files in the archive.

**source** `str`
- The source server directory, which should usually be the [working directory](https://mcdreforged.readthedocs.io/en/latest/configuration.html#working-directory) of MCDR, that is, the default `server` directory. Files are synchronized from `source/world`  to `target/world`

**target** `str, list`
- The target server directory, you can only write a string if there is only one directory, and a list is needed for multiple directories. A copy of the source directory files will be synchronized for each target directory. By default, the MCDR working directory of the mirror server is located in the `Mirror` directory under the current MCDR root directory.

**ignore_inexistent_target_path** `bool`
- If a target server directory does not exist, it will be skipped when set to `false`. When set to `true`, the directory will be created and synchronization will continue.

**concurrency** `int`
- The number of threads performing hash calculations during synchronization.

**ignore_files** `list`
- Files that are not synchronized, if you use the `carpet` mod and the `plus-carpet-addition(PCA)` mod, it is recommended to add `"carpet.conf"` `"pca.conf"`

<br>

### command: Command Configuration

```yaml
command:
    permission: # Command permission configuration
    action: # Command behavior configuration
```

<br>

### permission: Command Permission Configuration
```yaml
permission:
    status: 0
    start: 0
    stop: 2
    kill: 3
    sync: 2
    confirm: 0
    abort: 0
    log: "console"
    execute: "console"
```
`int`
- The minimum MCDR permission level required to execute each command, set to `console` for console available only.

<br>

### action: Command Behavior Configuration
```yaml
action:
    status:
        require_confirm: false
    start:
        require_confirm: false
    stop:
        require_confirm: true
    kill:
        require_confirm: true
    sync:
        ensure_server_closed: true
        auto_server_restart: false
        check_status_interval: 5
        max_attempt_times: 3
        save_world: # Save world configuration
        require_confirm: true
    history:
        require_confirm: false
        max_history_count: 5
    confirm:
        timeout: 30
        cancel_anymsg: true
    abort:
        operator: "everyone"
```

### General Configuration

**require_confirm** `bool`
- When this option is `true`, the command `!!mirror confirm` needs to be entered to confirm the operation after executing the command

### sync Configuration
**ensure_server_closed** `bool`
- When this option is `true`, synchronization will check whether the mirror server has stopped. When this option is `false`, synchronization will be carried out directly regardless of whether the mirror server has stopped or not.

**auto_server_restart** `bool`
- This option only takes effect when `ensure_server_closed` is `true`. When this option is `true`, if the mirror server is not stopped during synchronization, it will attempt to automatically stop the mirror server, perform synchronization, and automatically restart the mirror server after the synchronization is completed.

**check_status_interval** `int`
- This option only takes effect when `auto_server_restart` is in effect. After stopping the mirror server during synchronization, the plugin needs to confirm whether the mirror server has stopped. This option is the time interval for checking the status of the mirror server.

**max_attempt_times** `int`
- This option only takes effect when `auto_server_restart` is in effect. The number of attempts to check the status of the mirror server, after exceeding this number of attempts, it will no longer attempt to check the status of the mirror server, and output `automatic shutdown failed` and the current status information of the mirror server. Equivalent to the timeout time `timeout = check_status_interval * max_attempt_times`

**save_world** Save world configuration *Generally no need to change*
```yaml
save_world:
    turn_off_auto_save: true
    commands:
        save_all_worlds: "save-all flush"
        auto_save_off: "save-off"
        auto_save_on: "save-on"
    saved_world_regex: "^Saved the game$"
    save_world_max_wait_sec: 60
```
**turn_off_auto_save** `bool`
- Turn off auto save when saving the world

**commands** Related commands
- **save_all_worlds** `str`
  + Command to save the world
- **auto_save_off** `str`
  + Command to turn off auto save
- **auto_save_on** `str`
  + Command to turn on auto save

**saved_world_regex** `str`
- Regular expression to match the server "world saved" log

**save_world_max_wait_sec** `int`
- The maximum waiting time (seconds) for saving the world. After the timeout it will skip saving the world and perform synchronization

### history Configuration

**max_history_count** `int`
- The maximum number of synchronization history records to save. Set it to `-1` to remove the limit, or `0` to disable synchronization history. The default is `5`.

### confirm Configuration
Players can only confirm the commands they have executed

**timeout** `int`
- Command that needs confirmation will be canceled after the number of seconds. If the player has not taken any action after executing a command, the command will be canceled automatically.

**cancel_anymsg** `bool`
- If the player sends a message other than the `confirm` command after executing a command, the command operation will be canceled automatically. In addition, if the player executes another command corresponding to the mirror server after executing a command, the previously executed command will be canceled too.

### abort Configuration
~This feature is still under development~

<br>

### display: Display Configuration
```yaml
display:
    server_name: "Mirror"
```
**server_name** `str`
- The name of the "mirror server", used to distinguish between different mirror servers in the display

<br>

### Example of Multi-mirror Server Configuration File

```yaml
"!!mirror":
    mcsm:
        enable: true
        url: "http://127.0.0.1:23333/"
        uuid: "71154??????????0a1a2f4dd90695609"
        remote_uuid: "6e927??????????999f0e66bc404071b"
        apikey: "b8f???????????????????????????ade"
    terminal:
        enable: false
        launch_path: "./Mirror"
        launch_command: "python -m mcdreforged"
        port: null
        terminal_name: "Mirror"
        regex_strict: false
        is_mcdr: true
        proxy_type: null
        console_log: false
    rcon:
        enable: false
        address: null
        port: null
        password: null
    sync:
        world:
            - "world"
        source: "./server"
        target:
            - "./Mirror/server"
        ignore_inexistent_target_path: false
        concurrency: 4
        ignore_files:
            - "session.lock"
    command:
        permission:
            status: 0
            start: 0
            stop: 2
            kill: 3
            sync: 2
            confirm: 0
            abort: 0
        action:
            status:
                require_confirm: false
            start:
                require_confirm: false
            stop:
                require_confirm: true
            kill:
                require_confirm: true
            sync:
                ensure_server_closed: true
                auto_server_restart: true
                check_status_interval: 5
                max_attempt_times: 3
                save_world:
                    turn_off_auto_save: true
                    commands:
                        save_all_worlds: "save-all flush"
                        auto_save_off: "save-off"
                        auto_save_on: "save-on"
                    saved_world_regex: "^Saved the game$"
                    save_world_max_wait_sec: 60
                require_confirm: true
            confirm:
                timeout: 30
                cancel_anymsg: true
            abort:
                operator: "everyone"
    display:
        server_name: "Mirror"
"!!mirror2":
    mcsm:
        uuid: "83011??????????49c1133fc08a41b80"
    sync:
        target:
            - "./Mirror2/server"
    display:
        server_name: "Mirror2"
"!!mirror3":
    mcsm:
        enable: false
    sync:
        target:
            - "./Mirror3/server"
    terminal:
        enable: true
        launch_path: "./Mirror3"
        port: 30002
        terminal_name: "Mirror3"
    rcon:
        enable: true
        address: "127.0.0.1"
        port: 31002
        password: "p@ssw0rd"
```

## Acknowledgements

- Hash comparison idea / [better_backup](https://github.com/z0z0r4/better_backup)
- Configuration file permission configuration idea / [PrimeBackup](https://github.com/TISUnion/PrimeBackup)
- Save world idea / [QuickBackupM](https://github.com/TISUnion/QuickBackupM)

## ToDo

- [x] Command execution confirmation
- [ ] Command execution delay
- [ ] Prohibit synchronization `!!mirror sync enable/disable reason`
- [x] language file
- [ ] Command disable
- [x] RCON support
- [x] Start server through command line without MCSM
- [x] Linux/Windows execute `kill` command through terminal
- [x] Display history synchronization records

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MirrorMcsmcdR-v1.7.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.7.0) | 1.7.0 | 2026/09/04 14:20:12 | 47.34KB | 3 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.7.0/MirrorMcsmcdR-v1.7.0.mcdr) |
| [MirrorMcsmcdR-v1.6.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.6.0) | 1.6.0 | 2026/08/31 15:36:33 | 40.61KB | 5 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.6.0/MirrorMcsmcdR-v1.6.0.mcdr) |
| [MirrorMcsmcdR-v1.5.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.5.0) | 1.5.0 | 2026/08/19 15:50:02 | 36.8KB | 10 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.5.0/MirrorMcsmcdR-v1.5.0.mcdr) |
| [MirrorMcsmcdR-v1.4.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.4.1) | 1.4.1 | 2025/08/23 08:52:40 | 31.28KB | 302 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.4.1/MirrorMcsmcdR-v1.4.1.mcdr) |
| [MirrorMcsmcdR-v1.4.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.4.0) | 1.4.0 | 2025/05/23 17:10:05 | 27.64KB | 129 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.4.0/MirrorMcsmcdR-v1.4.0.mcdr) |
| [MirrorMcsmcdR-v1.3.6.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.6) | 1.3.6 | 2024/08/30 11:48:35 | 25.34KB | 176 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.6/MirrorMcsmcdR-v1.3.6.mcdr) |
| [MirrorMcsmcdR-v1.3.5.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.5) | 1.3.5 | 2024/08/01 11:11:24 | 25.34KB | 82 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.5/MirrorMcsmcdR-v1.3.5.mcdr) |
| [MirrorMcsmcdR-v1.3.4.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.4) | 1.3.4 | 2024/07/25 05:47:10 | 25.29KB | 60 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.4/MirrorMcsmcdR-v1.3.4.mcdr) |
| [MirrorMcsmcdR-v1.3.3.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.3) | 1.3.3 | 2024/07/24 09:16:40 | 25.29KB | 50 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.3/MirrorMcsmcdR-v1.3.3.mcdr) |
| [MirrorMcsmcdR-v1.3.2.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.2) | 1.3.2 | 2024/07/21 11:42:39 | 25.29KB | 53 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.2/MirrorMcsmcdR-v1.3.2.mcdr) |
| [MirrorMcsmcdR-v1.3.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.3.1) | 1.3.1 | 2024/07/02 09:06:19 | 25.25KB | 74 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.3.1/MirrorMcsmcdR-v1.3.1.mcdr) |
| [MirrorMcsmcdR-v1.2.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.2.1) | 1.2.1 | 2024/04/28 06:38:18 | 21.09KB | 96 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.2.1/MirrorMcsmcdR-v1.2.1.mcdr) |
| [MirrorMcsmcdR-v1.2.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.2.0) | 1.2.0 | 2024/04/28 05:46:54 | 21.1KB | 51 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.2.0/MirrorMcsmcdR-v1.2.0.mcdr) |
| [MirrorMcsmcdR-v1.1.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.1.0) | 1.1.0 | 2024/04/07 12:08:27 | 18.97KB | 45 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.1.0/MirrorMcsmcdR-v1.1.0.mcdr) |
| [MirrorMcsmcdR-v1.0.1.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v1.0.1) | 1.0.1 | 2024/04/06 09:05:50 | 18.19KB | 54 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v1.0.1/MirrorMcsmcdR-v1.0.1.mcdr) |
| [MirrorMcsmcdR-v0.1.0.mcdr](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/tag/v0.1.0) | 0.1.0 | 2024/01/06 08:32:34 | 5.5KB | 52 | [Download](https://github.com/LazyAlienServer/MirrorMcsmcdR/releases/download/v0.1.0/MirrorMcsmcdR-v0.1.0.mcdr) |

