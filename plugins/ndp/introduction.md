# No Danger Player Project MCDR Client (NDP-MCDR) - Multi-Server Joint Ban System
[中文](https://github.com/No-Danger-Player-Project/NDP-MCDR/blob/main/README_CN.md)|English

## Project Overview
​**No Danger Player Project MCDR Client (NDP-MCDR)​**​ is an open-source cross-server ban synchronization plugin designed to maintain real-time ban list synchronization across multiple servers, preventing malicious players from accessing any connected server. Centralized ban management significantly enhances server network security and administrative efficiency.

## Core Features
​**Real-time Ban Synchronization**​
- Immediate propagation of bans to all NDP-enabled servers when a player is banned on any member server
- Mandatory binding of ​**IP addresses**​ and ​**player usernames**​ to prevent ban evasion through alternate accounts or proxies

## Workflow
Player joins Server A → Plugin verifies local/central ban list → Denies access if banned → Synchronizes ban to Servers B/C/D...

## Quick Start
​**Installation**​
- Download the appropriate MCDR version to your server's `plugins` folder
- Restart server to generate `ndp_config.json` configuration file

​**Commands**​
- `!!ndp help` - Display help information
- `!!ndp ban <player> <reason>` - Request player ban
- `!!ndp pardon <player>` - Request player unban
- `!!ndp sync` - Synchronize ban data
- `!!ndp status` - Check system status
