**English** | [中文](readme-zh_cn.md)

\>\>\> [Back to index](/readme.md)

## securercon

### Basic Information

- Plugin ID: `securercon`
- Plugin Name: SecureRCON
- Version: 1.0.3
  - Metadata version: 1.0.3
  - Release version: 1.0.3
- Total downloads: 89
- Authors: [wangyupu](https://github.com/wang-yupu)
- Repository: https://github.com/wang-yupu/SecureRCON
- Repository plugin page: https://github.com/wang-yupu/SecureRCON/tree/main
- Labels: [`Management`](/labels/management/readme.md)
- Description: Encrypt your RCON connection

### Dependencies

| Plugin ID | Requirement |
| --- | --- |
| [mcdreforged](https://github.com/Fallen-Breath/MCDReforged) | \>=2.1.0 |
| [python](/plugins/python/readme.md) | \>=3.10.0 |

### Requirements

| Python package | Requirement |
| --- | --- |
| [cryptography](https://pypi.org/project/cryptography) | \>=44.0.0 |
| [javaproperties](https://pypi.org/project/javaproperties) | \>=0.8.0 |
| [pydantic](https://pypi.org/project/pydantic) | \>=2.10.0 |
| [pyyaml](https://pypi.org/project/pyyaml) | \>=6.0.0 |

```
pip install "cryptography>=44.0.0" "javaproperties>=0.8.0" "pydantic>=2.10.0" "pyyaml>=6.0.0"
```

### Introduction


> Translated by ChatGPT-4o

---

# SecureRCON

An MCDR plugin that encrypts your RCON access and extends RCON functionality.

## Why?

The vanilla RCON protocol transmits data in plain text (including the password and commands), so encrypting RCON is useful. With extended RCON functionality, you can execute MCDR commands and send chat messages.

## Encryption Method and Access Instructions

After installing this plugin, if any ports on your machine are exposed to the internet, please use a firewall (e.g., ufw / firewalled / iptables) to block access. Also, set a strong RCON password. This plugin will automatically read the RCON password and listen on a port (default is 25576). The protocol on this port is compatible with the original RCON, so if you're using a vanilla RCON client, you can still connect using a fixed strong password or a dynamic one.

### SecureMCRCON Python Package

> Run `pip install securemcrcon` to install, then use the `smcrcon` command  
> [Repo](https://github.com/wang-yupu/SecureMCRCON)  
> [PyPI](https://pypi.org/project/securemcrcon/)

A CLI client.

### MCRCON App

> Coming soon (second priority)

<!-- [GitHub](https://github.com/wang-yupu/)
This app will support Windows / macOS (Coming Soon) / Linux (Coming Soon) / Android. It allows encrypted RCON connections and is also a feature-rich graphical RCON client. -->

### Download

> [!IMPORTANT]
> Read the README file in plugin repository before using it.

| File | Version | Upload Time (UTC) | Size | Downloads | Operations |
| --- | --- | --- | --- | --- | --- |
| [SecureRCON-v1.0.3.mcdr](https://github.com/wang-yupu/SecureRCON/releases/tag/v1.0.3) | 1.0.3 | 2025/12/07 07:16:57 | 10.96KB | 17 | [Download](https://github.com/wang-yupu/SecureRCON/releases/download/v1.0.3/SecureRCON-v1.0.3.mcdr) |
| [SecureRCON-v1.0.2.mcdr](https://github.com/wang-yupu/SecureRCON/releases/tag/v1.0.2) | 1.0.2 | 2025/05/23 18:02:10 | 10.91KB | 37 | [Download](https://github.com/wang-yupu/SecureRCON/releases/download/v1.0.2/SecureRCON-v1.0.2.mcdr) |
| [SecureRCON-v1.0.1.mcdr](https://github.com/wang-yupu/SecureRCON/releases/tag/v1.0.1) | 1.0.1 | 2025/05/01 04:48:52 | 11.6KB | 35 | [Download](https://github.com/wang-yupu/SecureRCON/releases/download/v1.0.1/SecureRCON-v1.0.1.mcdr) |

