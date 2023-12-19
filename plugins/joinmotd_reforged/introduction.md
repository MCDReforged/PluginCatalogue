# 📝 Join MOTD Reforged

Yet another Join MOTD plugin for MCDR.

![Built for MCDR 2.10+](./-BUILT%20FOR%20MCDR%202.10+-57728b.svg)

## 📜 Features

Show an MOTD containing an welcome message, how long the server has been opened and a sub-server list when a player joins the server.

## 📖 Commands

- `!!motd`: Show the MOTD and the sub-server list.
- `!!motd reload`: Reload the configuration file.
- `!!server`: Show the sub-server list.

## ⚙️ Requirements

- Python 3.9 or above (lower versions may work, but not tested)
- MCDReforged 2.10.0 or above
- NBTLib 2.0.0 or above
- [DayCount NBT](https://github.com/alex3236/daycount-NBT) 2.2.1 or compatible version

## 📥 Installation

> [!IMPORTANT]
> This plugin shall **ONLY** be installed on a backend server (i.e. the server connected through the proxy server like BungeeCord or Velocity)
> and **SHALL NOT** be installed on a proxy server.

1. Install NBTLib via pip:

    ```shell
    pip install nbtlib
    ```
   
2. Download and place [DayCount NBT](https://github.com/alex3236/daycount-NBT) plugin to MCDR plugins folder.
3. Download and place this plugin to MCDR plugins folder.
4. Configure this plugin in `config/joinmotd_reforged/config.json` according to the guide below.

## 📖 Configuration

```json5
{
    "server_name": "Minecraft Server", // The name of the server group.
    "current_server_name": "Survival Server", // The name of the current connected server.
    "server_list": [
        {
            // The name of a server in the server group. The name is the one used after the `/server` command.
            // This is configured via proxy server configuration.
            "name": "survival",
            // The description of the server with the name above.
            "description": "Survival Server"
        },
        {
            // Same principle as above.
            "name": "creative",
            "description": "Creative Server"
        },
        {
            // Same principle as above.
            "name": "mirror",
            "description": "Mirror Server"
        }
        // This list can be extended to suit your needs.
    ],
    "permission": {
        "motd": 0,    // The permission level required to execute `!!motd` command.
        "server": 0,  // The permission level required to execute `!!server` command.
        "reload": 3   // The permission level required to execute `!!motd reload` command.
    }
}
```
