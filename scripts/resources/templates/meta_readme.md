## MCDReforged Plugin Catalogue Meta

The branch for custom MCDR plugin managers to fetch data from

### File structure

```bash
repos_root/
+-- my_plugin/        # A plugin with id "my_plugin"
|   +-- meta.json     # Json object: MetaInfo
|   +-- plugin.json   # Json object: FormattedPluginInfo
|   +-- release.json  # Json object: ReleaseSummary
|
+-- another_plugin/   # Another plugin with id "another_plugin"
|   +-- meta.json
|   +-- plugin.json
|   +-- release.json
|
+-- ...               # more directory for more plugins
|
+-- plugins.json      # Json object: PluginMetaSummary
+-- authors.json      # Json object: AuthorSummary
```

### Object definition

#### PluginMetaSummary

The Summary of the plugin catalogue meta

```json5
{
  "plugin_amount": 100,  // the amount of the plugins
  // A map of (string -> string) that maps plugin id -> plugin's MetaInfo
  // A quick way to get an overview of the meta repository
  "plugins": {
    "my_plugin": {/* MetaInfo */}
  }  
}
```

#### AuthorSummary

A collection of all authors of plugins

Authors are collected from `plugin_info.json` and categorized by their names

```json5
{
  "amount": 2,  // the amount of authors
  "authors": {
    "Fallen_Breath": {
      "name": "Fallen_Breath",
      "link": "https://github.com/Fallen-Breath"
    },
    "SomeoneElse": {
      "name": "SomeoneElse",
      "link": "https://github.com/SomeoneElse"
    }
  }
}
```

#### MetaInfo

Necessary information for a plugin

For `MetaInfo` object in `meta.json`, the information is fetched from the **latest commit** of its repository

For `MetaInfo` object in `ReleaseSummary` object, the information is fetched from the **corresponding tag** of its repository

```json5
{
  "schema_version": 2,

  // Basic information
  "id": "my_plugin",  // id of the plugin
  "name": "MyPlugin",  // name of the plugin
  "version": "1.2.0",  // version of the plugin
  "repository": "https://github.com/Myself/MyPlugin",  // plugin's GitHub repository url
  "authors": ["MyName"],  // a list of string, names of plugin's authors
  
  // A map of (string -> string) that maps plugin id -> version requirement
  // Plugin's mcdr plugin requirements
  // Reference: https://mcdreforged.readthedocs.io/en/latest/plugin_dev/metadata.html#dependencies
  "dependencies": {
    "mcdreforged": ">=2.2.0"
  },
  
  // A list of string, plugin's python requirements
  // i.g. lines in the requirements.txt files
  "requirements": [
    "mcdreforged>=2.2.0"
  ],
  
  // A map of (string -> string) that maps language -> description
  // The translated description of the plugin 
  "description": {
    "en_us": "My lovely plugin",  // "en_us" is the default language, that always exists
    "zh_cn": "我那可爱的插件"
  }
}
```

#### ReleaseSummary

The release summary of the plugin, which contains necessary information of all releases

```json5
{
  "schema_version": 6,
  "id": "my_plugin",  // The id of the plugin that this ReleaseSummary belongs to
  
  // The latest version of the plugin
  // Actually its value equals to the "parsed_version" field of the first release
  "latest_version": "1.2.0",
  
  // A list of ReleaseInfo object, the releases information
  "releases": [
    {/* ReleaseInfo */},
    {/* ReleaseInfo */}
  ]
}
```


#### ReleaseInfo

Information of a GitHub release

```json5
{
  "url": "https://github.com/Myself/MyPlugin/releases/tag/v1.2.0",  // url to the release
  "name": "MyPlugin v1.2.0",  // name of the release
  "tag_name": "v1.2.0",  // tag of the release
  "created_at": "2022-10-05T09:20:00Z",  // release creation time, in %Y-%m-%dT%H:%M:%SZ format
  
  // A list of AssetInfo object, storing all assets with ".mcdr" or ".pyz" file extension
  // Notes that all matching asset in the releases will be stored here. Usually you can just take the 1st asset
  // The plugin category will take the 1st MCDR plugin file as the plugin file of this release
  "assets": [  
    {/* AssetInfo */},
    {/* AssetInfo */}
  ],
  
  "description": "My new plugin release, Wow!",  // the description of the GitHub release
  "prerelease": false, // if it's a pre-release
  // A parsed semver like version string of this release
  // Reference: https://mcdreforged.readthedocs.io/en/latest/plugin_dev/metadata.html#version
  "parsed_version": "1.2.0",
  
  // The MetaInfo parsed from the repository of the given tag.
  // If the MetaInfo fetching has failed, the value will be a string of the error message,
  // e.g. "Failed to decode json from response! status_code 404: b'404: Not Found'"
  "meta": {/* MetaInfo */}  // MetaInfo or string
}
```

#### AssetInfo

Information of an asset in GitHub release

```json5
{
  "name": "MyPlugin-v1.2.0.mcdr",  // name of the asset
  "size": 12735,  // size of the asset, in bytes
  "download_count": 1457,  // download count of the asset
  "created_at": "2022-10-03T04:13:26Z",  // asset creation time, in %Y-%m-%dT%H:%M:%SZ format
  "browser_download_url": "https://github.com/Myself/MyPlugin/releases/download/v1.2.0/MyPlugin-v1.2.0.mcdr"  // the url to download this asset
}
```

#### FormattedPluginInfo

A formatted version of `plugin_info.json`

```json5
{
  "schema_version": 1,
  "id": "my_plugin",
  "repository": "https://github.com/Myself/MyPlugin",  // plugin's GitHub repository url

  "branch": "master",  // git branch for the plugin
  "related_path": ".",  // related path in the repository. see https://mcdreforged.readthedocs.io/en/latest/plugin_dev/plugin_catalogue.html#related-path
  "labels": ["management"],  // a list of string, labels of the plugin

  "introduction": {
    "en_us": "Use `!!stats` to see the value / rank, or build a scoreboard from given statistic type and name\n",
    "zh_cn": "使用 `!!stats` 并输入统计信息的类别和名称，来查询统计信息的值/排名，或者显示对应的计分板\n"
  }
}
```
