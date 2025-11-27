\# Fuck 32k Plugin  

&nbsp; 

A MCDReforged plugin that detects and removes items with illegal enchantments (above level 10).  

&nbsp; 

\## Features  

&nbsp; 

\- Automatically checks players' inventories for illegal enchantments  

\- Configurable check interval (default: 5 minutes)  

\- Whitelist system to exclude specific players  

\- Manual check command for individual players  

\- Real-time monitoring on player join and kill events  

&nbsp; 

\## Commands  

&nbsp; 

\- `!!f32` - Show help  

\- `!!f32 add <player>` - Add player to whitelist (Owner only)  

\- `!!f32 rm <player>` - Remove player from whitelist (Owner only)  

\- `!!f32 ls` - List whitelisted players (Owner only)  

\- `!!f32 checker <player>` - Check specific player's items  

\- `!!f32 time <seconds>` - Set check interval (Owner only, min 10s)  

&nbsp; 

\## Configuration  

&nbsp; 

The plugin automatically creates a `config.json` file with:  

\- `whitelist`: List of exempted players  

\- `check\_interval`: Check interval in seconds

