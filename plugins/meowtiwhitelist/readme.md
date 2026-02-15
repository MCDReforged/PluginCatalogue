**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## meowtiwhitelist

### Basic Information

- Plugin ID: `meowtiwhitelist`
- Plugin Name: MeowtiWhitelist
- Version: 2.4.0
  - Metadata version: 2.4.0
  - Release version: 2.4.0
- Total downloads: 410
- Authors: [MliroLirrorsIngenuity](https://github.com/MliroLirrorsIngenuity)
- Repository: https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist
- Repository plugin page: https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: A plugin that can manage the whitelist with multiple Yggdrasil APIs.

### Dependencies

| Plugin ID | Requirement |
| --- | --- |

### Requirements

| Python package | Requirement |
| --- | --- |
| [mcdreforged](https://pypi.org/project/mcdreforged) | \>=2.12.0 |
| [requests](https://pypi.org/project/requests) | \>=2.31.0 |
| [PyYAML](https://pypi.org/project/PyYAML) | \>=6.0.2 |

```
pip install "mcdreforged>=2.12.0" "requests>=2.31.0" "PyYAML>=6.0.2"
```

### Introduction

<div align="center">
  <h1 align="center">MeowtiWhitelist</h1>
  <p align="center">
        A multiple verification service whitelist management plugin based on <a href="https://mcdreforged.com/"><strong>MCDReforged</strong></a>, solving whitelist issues in a multi-verification service environment.
    <br />
    <br />
    <a href="https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/blob/main/README.md">简体中文</a>
    |
    <a href="https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/blob/main/README_EN.md">English (You Are Here.)</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>

- [Features](#features)
- [Usage](#usage)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Configuration & Commands & API](#configuration--commands--api)
- [Before Asking Questions](#before-asking-questions)
- [Contributors](#contributors)
- [Acknowledgements](#acknowledgements)

</details>

## Features

- Resolves UUID conflicts or incorrect UUIDs caused by multiple **Yggdrasil** authentication services.
- Manage whitelists from different **Yggdrasil** sources with simple commands.
- No manual editing of the correct UUID from the corresponding authentication source in `whitelist.json` required (~~Who tf edited `whitelist.json` again?~~)

## Usage

### Requirements

`MCDReforged`>=2.12.0

`requests`>=2.31.0

`PyYAML`>=6.0.2

### Installation

Run the following command in your running MCDReforged instance and follow the prompts to install.

```
!!MCDR plugin install meowtiwhitelist
```

If the server's network environment has difficulty accessing the installation source or for other reasons, you can try the manual installation below.

<details>
  <summary>Manual Installation</summary>


1. Download the latest version of MeowtiWhitelist from [GitHub Releases](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases).
2. Place the plugin into MCDR’s `plugins` folder.
3. Install the [requirements](#requirements).
4. [Start the server with MCDReforged](https://docs.mcdreforged.com/zh-cn/latest/quick_start/first_run.html#run).

</details>

### Configuration & Commands & API
See [Wiki](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/wiki).

## Before Asking Questions

Please confirm:

- You have tried all possible solutions.
- You have searched for answers (like checking [Issues](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/issues)).
- You have provided enough info to help developers find the issue (logs, config files, plugin lists, and version details).
- Explanation of Question Submission Channels
  - **Usage Issues/Configuration Questions/Other Issues** → [Discussions](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/discussions)
  - **Bug/Feature Request** → [Issues](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/issues)

## Contributors
<a href="https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MliroLirrorsIngenuity/MeowtiWhitelist&" alt="Contributors" />
</a>

## Acknowledgements

[Lazy-Bing-Server/MCDR-offline-whitelist-manager](https://github.com/Lazy-Bing-Server/MCDR-offline-whitelist-manager): Provided the base idea.

[CaaMoe/MultiLogin](https://github.com/CaaMoe/MultiLogin): Inspired the configuration approach.

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [MeowtiWhitelist-v2.4.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.4.0) | 2.4.0 | 2025/10/16 19:41:27 | 11.68KB | 52 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.4.0/MeowtiWhitelist-v2.4.0.mcdr) |
| [MeowtiWhitelist-v2.3.1.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.3.1) | 2.3.1 | 2025/10/05 10:34:13 | 11.41KB | 19 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.3.1/MeowtiWhitelist-v2.3.1.mcdr) |
| [MeowtiWhitelist-v2.3.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.3.0) | 2.3.0 | 2025/06/26 16:24:12 | 11.48KB | 80 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.3.0/MeowtiWhitelist-v2.3.0.mcdr) |
| [MeowtiWhitelist-v2.2.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.2.0) | 2.2.0 | 2025/03/22 14:27:05 | 10.12KB | 60 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.2.0/MeowtiWhitelist-v2.2.0.mcdr) |
| [MeowtiWhitelist-v2.1.2.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.1.2) | 2.1.2 | 2025/03/11 15:59:39 | 9.48KB | 36 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.1.2/MeowtiWhitelist-v2.1.2.mcdr) |
| [MeowtiWhitelist-v2.1.1.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.1.1) | 2.1.1 | 2025/03/08 15:03:12 | 9.48KB | 35 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.1.1/MeowtiWhitelist-v2.1.1.mcdr) |
| [MeowtiWhitelist-v2.1.0.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.1.0) | 2.1.0 | 2025/03/06 18:27:06 | 9.46KB | 27 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.1.0/MeowtiWhitelist-v2.1.0.mcdr) |
| [MeowtiWhitelist-v2.0.3.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.0.3) | 2.0.3 | 2025/03/04 18:57:26 | 8.88KB | 32 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.0.3/MeowtiWhitelist-v2.0.3.mcdr) |
| [MeowtiWhitelist-v2.0.2.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.0.2) | 2.0.2 | 2025/03/04 16:27:08 | 8.81KB | 40 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.0.2/MeowtiWhitelist-v2.0.2.mcdr) |
| [MeowtiWhitelist-v2.0.1.mcdr](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/tag/v2.0.1) | 2.0.1 | 2025/03/03 19:08:45 | 8.82KB | 29 | [Download](https://github.com/MliroLirrorsIngenuity/MeowtiWhitelist/releases/download/v2.0.1/MeowtiWhitelist-v2.0.1.mcdr) |

