English | [Español](README-es.md)
# Region File Manager (RFM)

This is a plugin for [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) that allows you to manage region files on a Minecraft server.

## Description

The Region File Manager (RFM) plugin is a useful tool for managing regions in your Minecraft world. It allows you to perform tasks such as saving, restoring, deleting, and listing regions with ease.

## Commands

The RFM plugin adds the following commands:

- `!!rfm save <x> <z> <dim> <name>`: Save a region to a new folder.
- `!!rfm restore <name>`: Restore the specified region.
- `!!rfm remove <x> <z> <dim>`: Remove the specified region file from the world.
- `!!rfm list`: Show a list of saved regions.
- `!!rfm del <name>`: Delete a region from the list.
- `!!rfm abort`: Abort a currently running restoration operation.

## Configuration

You can configure the plugin's behavior in the `config.json` file with the following options:

- **prefix**: Defines the prefix for the plugin's commands.
- **recognized_cmds**: List of recognized commands by the plugin.
- **regions_path_over**: Path to the regions in the main world (Overworld).
- **regions_path_nether**: Path to the regions in the Nether.
- **regions_path_end**: Path to the regions in the End.
- **dst_path**: Path where the regions are saved.
- **dst_path_over**: Path for Overworld regions.
- **dst_path_nether**: Path for Nether regions.
- **dst_path_end**: Path for End regions.
- **minimum_permission_level**: Minimum permission level required to use the plugin.

Make sure that the paths are correct based on your Minecraft server's structure.
It should still work without modifying anything.

### Default configuration:

```json
{
    "prefix": "!!rfm",
    "recognized_cmds": [
        "save",
        "restore",
        "remove",
        "list",
        "del",
        "abort"
    ],
    "regions_path_over": "./server/world/region/",
    "regions_path_nether": "./server/world/DIM-1/region/",
    "regions_path_end": "./server/world/DIM1/region/",
    "dst_path": "./regions_folder/",
    "dst_path_over": "./regions_folder/overworld/",
    "dst_path_nether": "./regions_folder/nether/",
    "dst_path_end": "./regions_folder/end/",
    "minimum_permission_level": 3
}