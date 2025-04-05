**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## cfgcmd

### Basic Information

- Plugin ID: `cfgcmd`
- Plugin Name: configCommand
- Version: 1.2.6
  - Metadata version: 1.2.6
  - Release version: 1.2.6
- Total downloads: 24
- Authors: [wangyupu](https://github.com/wang-yupu)
- Repository: https://github.com/wang-yupu/configCommand
- Repository plugin page: https://github.com/wang-yupu/configCommand/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Modify config files with MCDR command

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [pyyaml](https://pypi.org/project/pyyaml) |  |
| [toml](https://pypi.org/project/toml) |  |

```
pip install pyyaml toml
```

### Introduction

# configCommand / cfgcmd

[简体中文](https://github.com/wang-yupu/configCommand/tree/main//README.md)

Use MCDR commands modify plugin/mod config in-game!

> ALL TRANSLATED BY GPT-4o

## Permissions

Currently, this plugin allows all permitted players in the configuration (MCDR level 4 permission) to use it. This plugin can modify **any file that the user running the MCDR process has permission to modify** (especially `root`). Therefore, **please manage permissions carefully or run the server inside a container**.

## Commands

- `!!cfg env <path (relative to MCDR root, absolute/relative paths are allowed)> <config file> [optional: reader/writer type]`: Set the target file for modification.
- `!!cfg quit`: Clear the target file for the executor.
- `!!cfg write`: Save changes to the target file.
- `!!cfg reload`: Reload the target file (overwriting all unsaved modifications).
- `!!cfg info`: Display file information.

---  

- `!!cfg set <key> <value>`: Set a key-value pair. Keys separated by `.` are interpreted as a configuration tree path (see examples below). The `key` parameter does not support relative paths like `..`.
- `!!cfg setTyped <key> <type> <value>`: See the "Data Types" section below. If the value cannot be interpreted as the specified type, it defaults to `STRING`.
- `!!cfg rm <key>`: Delete the specified key.
- `!!cfg mv <sourceKey> <destKey>`: Move or rename a key.
- `!!cfg cp <sourceKey> <destKey>`: Copy and paste a key.
- `!!cfg cd <key>`: Since configuration files are tree-structured, this command allows navigation like a filesystem. Not available for the `plain` reader/writer type.
- `!!cfg ls [optional: page]`: List the current object’s content. For `plain` reader/writer type, prints the full text. Each page contains 10 lines.

---  

- `!!cfg lsDir <path>`: List files in a directory relative to the MCDR root.
- `!!cfg rmFile <file>`: Delete a file (**irreversible**).
- `!!cfg touchFile <file>`: Create an **empty** file.

---  

> Running `!!cfg env ...` does not lock the file.  
> Running `!!cfg info` displays the current file information.  
> Running `!!cfg ls` prints the content of the current object pointer.  
> The reader/writer type is determined by the file extension. Files without an extension or with an unknown extension default to the `plain` reader/writer.  
> If the reader/writer type is `plain`, `<key>` refers to a line number.  
> If `<key>` contains spaces and is followed by parameters, enclose it in double quotes. Use `\` for escaping. See [QuotableText](https://docs.mcdreforged.com/en-us/latest/code_references/command.html#mcdreforged.command.builder.nodes.arguments.QuotableText) for details.

### Data Types

`setTyped` allows specifying a value’s data type. The following types are supported, some with special behavior:

- `STRING`: Basic string.
- `INT`: Numeric value, including floating-point numbers (`float`).
- `BOOL`: Boolean value, case-insensitive. Valid inputs: `T`, `True` (true), `F`, `False` (false).
- `LIST`: List.
- `OBJECT`: Equivalent to JavaScript’s `Object`, Python’s `dict`, and YAML’s `mapping`.
- `AUTO`: Equivalent to using the `set` command directly.

#### Special Behavior of `LIST` and `OBJECT`

##### `LIST`

Values are split using a comma (`,`). Use `\` to escape commas if necessary. Items are automatically type-inferred and stored in a list. An empty value creates an empty list.

##### `OBJECT`

Similar to `LIST`, values are split using commas, and key-value pairs are further split by colons (`:`). Use `\` to escape commas if necessary. Items are automatically type-inferred (both keys and values) and stored as an `OBJECT`. An empty value creates an empty `OBJECT`.
> Using `setTyped OBJECT ...` is not recommended due to chat input limitations. It is better suited for creating empty `OBJECT`s.

#### Type Inference

All inferred types follow this logic:

1. If the original value does not exist or is `None` (case-sensitive), start automatic inference; otherwise, use the original type if applicable.
2. Convert the value to uppercase. If it matches [`T`, `TRUE`, `F`, `FALSE`], it is a boolean. Otherwise, proceed.
3. If the value contains non-numeric characters (excluding decimal points, negative signs, and double quotes), it is a string. Otherwise, proceed to step 4.
4. If the value is enclosed in double quotes, remove the quotes and repeat step 5. Otherwise, continue.
5. If the value consists entirely of digits (with optional decimal points and leading signs), it is a number (decimal point placement is determined by the last occurrence). Otherwise, it is a string.

> `LIST` and `OBJECT` do not participate in this inference process, meaning automatic inference never results in `LIST` or `OBJECT`.

### Example

Original configuration file:

```json
1  {
2      "foo": 123,
3      "bar": {
4          "barFoo": "?",
5          "barBar": {
6              "barBarFoo": 456
7          }
8      },
9      "buzz": [
10         "wangyupu","zzfx1166"
11     ]
12 }
```

Commands (in order):

1. `!!cfg env "config/foo/" bar.json`: Open file.
2. `!!cfg set foo 1231`: Change line 2 value to 1231.
3. `!!cfg set bar.barFoo "!"`: Change line 4 value to `"!"`.
4. `!!cfg rm buzz.1`: Remove the second item (0-based index) from the list at line 10.
5. `!!cfg cd bar.barBar`: Move the pointer to the `barBar` object at line 5.
6. `!!cfg set barBarFoo 789`: Change line 6 value to 789.
7. `!!cfg write`: Save changes.
8. `!!cfg quit`: Exit file.

Modified configuration file:

```json
1  {
2      "foo": 1231,
3      "bar": {
4          "barFoo": "!",
5          "barBar": {
6              "barBarFoo": 789
7          }
8      },
9      "buzz": [
10         "wangyupu"
11     ]
12 }
```

## Plugin Configuration

```yaml
ownerPlayer: player_name
cfgCmdPermission: 4
allowModifyConfig: true
allowOutBound: false
enableLog: true
onlyOwnerPlayer: false
```

- `ownerPlayer`: The specified player bypasses all security controls. Leave it empty to enforce permission checks for all players.
- `allowModifyConfig`: Whether to allow modification of **this plugin's (`cfgcmd`) configuration**.
- `allowOutBound`: Whether to allow access outside the `MCDR` root directory. When `false`, access is limited to the `MCDR` directory.
- `enableLog`: Whether to enable logging. Logs are saved in *MCDR root path* `/logs/cfgcmdLogs/<YYYY>-<mm>-<dd>_<COUNT>.log`.
- `onlyOwnerPlayer`: Whether only the specified `ownerPlayer` can use this plugin.

> `allowModifyConfig` defaults to `true` to allow administrators to configure the plugin without backend access. It is recommended to set this to `false` after installation.

## Supported Configuration File Formats

- `json`
- `yaml` (`yml`)
- `toml`
- Plain text

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [cfgcmd-v1.2.6.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.6) | 1.2.6 | 2025/04/05 03:04:34 | 16.35KB | 2 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.2.6/cfgcmd-v1.2.6.mcdr) |
| [cfgcmd-v1.2.5.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.5) | 1.2.5 | 2025/04/02 13:58:44 | 16.35KB | 3 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.2.5/cfgcmd-v1.2.5.mcdr) |
| [cfgcmd-v1.2.4.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.4) | 1.2.4 | 2025/04/02 11:20:09 | 16.35KB | 2 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.2.4/cfgcmd-v1.2.4.mcdr) |
| [cfgcmd-v1.2.3.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.3) | 1.2.3 | 2025/03/30 16:34:22 | 16.25KB | 2 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.2.3/cfgcmd-v1.2.3.mcdr) |
| [cfgcmd-v1.2.0.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.2.0) | 1.2.0 | 2025/03/28 15:50:19 | 15.34KB | 5 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.2.0/cfgcmd-v1.2.0.mcdr) |
| [configCommand-v1.1.0.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.1.0) | 1.1.0 | 2025/03/27 03:11:05 | 12.79KB | 5 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.1.0/configCommand-v1.1.0.mcdr) |
| [configCommand-v1.0.1.mcdr](https://github.com/wang-yupu/configCommand/releases/tag/v1.0.1) | 1.0.1 | 2025/03/26 06:38:16 | 12.58KB | 5 | [Download](https://github.com/wang-yupu/configCommand/releases/download/v1.0.1/configCommand-v1.0.1.mcdr) |

