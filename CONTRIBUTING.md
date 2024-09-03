**English** | [中文](CONTRIBUTING_cn.md)

# Contribution Guidelines

We are truly honored and grateful for your willingness to contribute to this project.

To ensure that your efforts integrate smoothly into the project and benefit the entire community, we have created this guide to help you better understand our standards and processes.

We encourage you to read the following information carefully to help you work efficiently and ensure that your contributions meet our requirements and guidelines.
 
Sections marked with an `*` are **suggestions**, while the rest are **requirements**, both serving as references for your development process and for catalogue maintainers when reviewing PRs.

We hope this guide can be a great starting point for you!

## Adding or modifying plugin?

### *Is your plugin suitable for the catalogue?

Do not submit plugins in a hurry. Before creating and submitting new plugins, consider the following questions:

- Is there already a plugin with really similar functionality? —— Unnecessarily reinventing wheels is not desirable;
- Is your code necessary to provide as an MCDR plugin? Would it be more suitable for PyPI? —— Consider the use purpose and make sure it is necessary;
- Is the plugin commonly applicable? Can new users have reasons to use your plugin? —— Do not submit self-use only or completely useless plugins;
- Is your project ready for public testing (beta)? —— If it is still in an early stage, wait until it is ready.

### Make sure you have permissions

Users submitting plugins to the plugin catalogue should be in one of the following capacities:
- Author, maintainer, or collaborator of the plugin;
- An uploader who has explicit permission from someone above in writing.

If your plugin references or uses codes from other projects:
- If the codes is open source, follow their open source license;
- If the codes is proprietary, make sure you have the right to use them, and follow their agreement.

### Uniqueness and compatibility

- Plugin name and ID should not be **too similar** to other plugins;
- Explicitly declare required plugins and/or Python packages in corresponding fields (also declare MCDR version if needed);
- Make sure that your plugin works properly on target platforms.

### Write plugin information correctly

- Create or edit `plugin_info.json` as described in [documentation](https://docs.mcdreforged.com/en/latest/plugin_dev/plugin_catalogue.html);
- Take care to check the `label` field is appropriate by referring to existing plugins;
- Plugin ID must be consistent at all places;
- `description` and `introduction` fields should provide at least in `en_us`;
- The plugin README should be placed in `related_path` and named `README.md` (case insensitive), bilingual version is recommended but not required.

### Introduce your plugin properly

A good and detailed introduction is one of the conditions for becoming an excellent plugin.

- In the README or documentation, explain the plugin's functions, features, usage, etc. in detail;
- In the `description`, briefly summarise what the plugin does in one sentence;
- Introduce the plugin's features in the `introduction`, or direct reference it to the README file.

### One PR for one thing

- When adding plugins, please submit multiple plugins in separate PRs;
- When modifying plugins, changes to the same fields in multiple plugins by the same author can be combined in one PR;
- When deleting plugins, multiple plugins of the same author can be combined in one PR.

## Contributing to scripts or workflows?

- It is recommended to create an Issue first, describing the problem or request, and then create the PR associated with it;
- All changes should be merged into the `master` branch.
