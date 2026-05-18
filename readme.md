## MCDReforged Plugin Catalogue Meta

The branch for custom MCDR plugin managers to fetch data from

### File structure

```bash
repos_root/
+-- my_plugin/           # A plugin with id "my_plugin"
|   +-- meta.json        # Json object: MetaInfo
|   +-- plugin.json      # Json object: PluginInfo
|   +-- release.json     # Json object: ReleaseSummary
|   +-- repository.json  # Json object: RepositoryInfo
|   +-- all.json         # Json object: AllOfAPlugin
|   +-- all.json.gz      # A gz-compressed "all.json"
|
+-- another_plugin/   # Another plugin with id "another_plugin"
|   +-- meta.json
|   +-- ...
|
+-- ...               # more directory for more plugins
|
+-- everything.json           # Json object: Everything
+-- everything.json.gz        # A gz-compressed "everything.json"
+-- everything.json.xz        # A xz-compressed "everything.json"
+-- everything_slim.json      # Json object: Everything (slim)
+-- everything_slim.json.gz   # A gz-compressed "everything_slim.json"
+-- everything_slim.json.xz   # A xz-compressed "everything_slim.json"
+-- authors.json              # Json object: AuthorSummary
+-- authors.json.gz           # A gz-compressed "authors.json"
+-- plugins.json              # Json object: PluginMetaSummary
+-- plugins.json.gz           # A gz-compressed "plugins.json"
```

| What you want                                                                                     | Where to get                               |
|---------------------------------------------------------------------------------------------------|--------------------------------------------|
| Everything possible in the meta repository                                                        | [`everything.json`](#Everything)           |
| Everything in the meta repository, but don't need those textual introduction / description things | [`everything_slim.json`](#slim-everything) |
| Summary of all plugins, i.e. what plugins does the meta repository have                           | [`plugins.json`](#PluginMetaSummary)       |
| Summary of plugin authors                                                                         | [`authors.json`](#AuthorSummary)           |
| Information of a specified plugin                                                                 | `<plugin_id>/xxx.json`                     |

### Object definition

#### Everything

Everything in the meta repository, including:

- [AuthorSummary](#AuthorSummary)
- [MetaInfo](#MetaInfo), [PluginInfo](#PluginInfo) and [ReleaseSummary](#ReleaseSummary) of all plugins

If you want to grab the whole repository, fetch this and that's it

```json5
// Everything
{
  "timestamp": 1705680000,  // the unix timestamp in seconds, when this data is created
  "authors": {/* AuthorSummary */},
  // A map of plugin id -> AllOfAPlugin
  "plugins": {
    "my_plugin": {/* AllOfAPlugin */},
    // ...
  }
}
```

```json5
// AllOfAPlugin
{
  "meta": {/* MetaInfo */},              // same with the "<plugin_id>/meta.json" file, null if fetch failed
  "plugin": {/* PluginInfo */},          // same with the "<plugin_id>/plugin.json" file
  "release": {/* ReleaseSummary */},     // same with the "<plugin_id>/release.json" file, null if fetch failed
  "repository": {/* RepositoryInfo */}   // same with the "<plugin_id>/repository.json" file, null if fetch failed
}
```

##### slim everything

A slim version of the [Everything](#everything) object that remove all textural introduction / description stuffs, including:

- `/plugins/*/plugin/introduction`
- `/plugins/*/repository/readme`
- `/plugins/*/release/releases/*/description`

Its syntax is the same as [Everything](#everything)

It's useful because of its smaller size for plugin managers / installers since they might not need these textual stuffs

#### PluginMetaSummary

A collection of `MetaInfo` and `PluginInfo` of all plugins

A quick way to get an overview of the `meta` repository

See the [MetaInfo](#MetaInfo) section for more information

If you also want to get the [ReleaseInfo](#ReleaseInfo), use [`everything.json`](#Everything) instead

```json5
{
  "plugin_amount": 100,  // the amount of the plugins
  // A map of plugin id -> MetaInfo
  "plugins": {
    "my_plugin": {/* MetaInfo */},
    // ...
  },
  // A map of plugin id -> PluginInfo
  "plugin_info": {
    "my_plugin": {/* PluginInfo */},
    // ...
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
    },
    // ...
  }
}
```

#### MetaInfo

Necessary information for a plugin

For `MetaInfo` object in `meta.json` and `PluginMetaSummary` object, the information is fetched from the **latest commit** from its repository.
For these object, it's recommended to only use the `name` and the `description` field, since other fields might be unstable

For `MetaInfo` object in `ReleaseInfo` object, the information is fetched from the packed plugin file asset of the release

```json5
{
  "schema_version": 4,

  // Basic information
  "id": "my_plugin",  // id of the plugin
  "name": "MyPlugin",  // name of the plugin
  "version": "1.2.0",  // version of the plugin
  "link": "https://home.myself.me",  // plugin's main page, from mcdreforged.plugin.json. Might not be a GitHub url. Might be null if it doesn't exist
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

#### PluginInfo

A formatted version of `plugin_info.json` from the master branch of the PluginCatalogue

```json5
{
  "schema_version": 1,
  "id": "my_plugin",
  "authors": ["MyName"],  // a list of string, names of plugin's authors
  
  "repository": "https://github.com/Myself/MyPlugin",  // plugin's GitHub repository url
  "branch": "master",  // git branch for the plugin
  "related_path": ".",  // related path in the repository. see https://mcdreforged.readthedocs.io/en/latest/plugin_dev/plugin_catalogue.html#related-path
  "labels": ["management"],  // a list of string, labels of the plugin

  "introduction": {
    "en_us": "My lovely plugin\n\n## Usage\n\n1. Install",
    "zh_cn": "我那可爱的插件\n\n## 使用方法\n\n1. 安装"
  },
  "introduction_urls": {
    "en_us": "https://raw.githubusercontent.com/Myself/MyPlugin/master/docs/introduction.md",
    "zh_cn": "https://raw.githubusercontent.com/Myself/MyPlugin/master/docs/introduction-zh_cn.md"
  }
}
```

#### ReleaseSummary

The release summary of the plugin, which contains necessary information of all releases

```json5
{
  "schema_version": 8,
  "id": "my_plugin",  // The id of the plugin that this ReleaseSummary belongs to
  
  // The latest version of the plugin. Nullable
  // Notes that it might not be the version of the most recent release
  "latest_version": "1.2.0",
    
  // The index of the latest version in the releases field. Nullable
  // Index starts from 0. use `releases[latest_version_index]` to get the ReleaseInfo of the latest release
  "latest_version_index": 0,
  
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
  
  "description": "My new plugin release, Wow!",  // the body of the GitHub release. Might be null
  "prerelease": false, // if it's a pre-release
  
  // An AssetInfo object storing the valid asset of the release,
  // A valid asset is an asset that contains a packed plugin file, which
  // 1. Has its file name ending with ".mcdr" or ".pyz"
  // 2. Is a valid zip file, contains "mcdreforged.plugin.json" and optional "requirements.txt" json at the zip root
  // If there are multiple packed plugin file assets, the first one is used, and the latter ones will be ignored
  "asset": {/* AssetInfo */},
  
  // The MetaInfo parsed from the packed plugin asset file
  "meta": {/* MetaInfo */}
}
```

#### AssetInfo

Information of an asset in GitHub release

```json5
{
  "id": 123450123,  // GitHub asset ID
  "name": "MyPlugin-v1.2.0.mcdr",  // name of the asset
  "size": 12735,  // size of the asset, in bytes
  "download_count": 1457,  // download count of the asset
  "created_at": "2022-10-03T04:13:26Z",  // asset creation time, in %Y-%m-%dT%H:%M:%SZ format
  "browser_download_url": "https://github.com/Myself/MyPlugin/releases/download/v1.2.0/MyPlugin-v1.2.0.mcdr",  // the url to download this asset
  "hash_md5": "14758f1afd44c09b7992073ccf00b43d",  // md5 hash digest of the asset
  "hash_sha256": "aec070645fe53ee3b3763059376134f058cc337247c978add178b6ccdfb0019f"  // sha256 hash digest of the asset
}
```

#### RepositoryInfo

Basic information of a GitHub repository

```json5
{
  "url": "https://github.com/Myself/MyPlugin",
  "name": "MyPlugin",  // Repository name
  "full_name": "Myself/MyPlugin",  // Username + repository name pair
  "description": "My lovely plugin",  // Repository description. Might be null if it's unset
  "archived": false,
  "stargazers_count": 987,
  "watchers_count": 65,
  "forks_count": 321,
  
  // README content of the repository
  // The script will firstly try to fetch the readme from the given repository related path (see `PluginInfo.related_path`)
  // If fails, it will then try to fetch from the repository root
  // If it still fails, the value will be null
  "readme": "## Readme for my lovely plugin",
  // URL of the readme url. null if failed to get the readme  
  "readme_url": "https://raw.githubusercontent.com/Myself/MyPlugin/master/README.md"
}
```
