**English** | [中文](CONTRIBUTING_CN.md)

# Contribution Guidelines

First of all, thank you for your interest in contributing!

Before you get started, we have some suggestions to make the process goes smoothly and efficiently.

Those with `*` are **required** and the rest are **suggested**, all serve as references for catalogue maintainers to review PRs.

## Adding or modifying plugin?

### Is your plugin suitable?

Do not submit plugins in a hurry.

Before creating and submitting new plugins, consider following questions:

- Is there already a plugin with really similar functionality? —— Unnecessarily reinventing wheels is not desirable;
- Is your code necessary to provide as a MCDR plugin? Would it be more suitable for PyPI? —— Consider the use purpose and make sure it is necessary;
- Is the plugin general enough? Can new users have reasons to use your plugin? —— Do not submit self-use only or completely useless plugins;
- Is your project ready for public testing (beta)? —— If it is still in an early version, wait until it is stable.

### *Make sure you have permissions

Users submitting plugins to the plugin catalogue should be in one of the following capacities:

- Author, maintainer, or collaborator of the plugin;
- An uploader who has explicit permission from someone above.

If your plugin reference or use codes from other projects:
- If the codes is open source, follow their open source licence;
- If the codes is proprietary, make sure you have the right to use them, and follow their agreement.

### *Uniqueness and compatibility

- Plugin name and ID should not be **too similar** to other plugins;
- Explicitly declare required plugins and/or Python packages in corresponding fields (also declare MCDR version if needed);
- Make sure that your plugin works properly on target platforms.

### *Write plugin information correctly

- Create or edit `plugin_info.json` as described in [documentation](https://mcdreforged.readthedocs.io/en/latest/plugin_dev/plugin_catalogue.html);
- Take care to check the `label` field is appropriate by referring to existing plugins;
- Plugin IDs must be consistent in all fields;
- `description` and `introduction` fields should provide at least in `en_us`;
- The plugin README should be placed in `related_path` and named `README.md` (case insensitive), bilingual version is recommended but not required.

### Introduce your plugin properly

A plugin that lacks an introduction is not welcome.

- In the README or documentation, explain the plugin's functions, features, usage, etc. in detail;
- In the `description`, briefly summarise what the plugin does in one sentence;
- Introduce the plugin's features in the `introduction`, or direct reference it to the README file.


### *One PR for one thing

- When adding plugins, please submit multiple plugins in separate PRs;
- When modifying plugins, changes to the same fields in multiple plugins by the same author can be combined in one PR;
- When deleting plugins, multiple plugins of the same author can be combined in one PR.

## *Contributing to scripts or workflows?

- It is recommended to create an Issue first, describing the problem or request, and then create the PR associated with it;
- All changes should be merged into the `master` branch.
