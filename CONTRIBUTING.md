**English** | [中文](CONTRIBUTING_cn.md)

# Contributing Guidelines

We are truly honored and grateful for your willingness to contribute to this project.

To ensure that your efforts integrate smoothly into the project and benefit the entire community, we have created this guide to help you better understand our standards and processes.

We encourage you to read the following information carefully to help you work efficiently and ensure that your contributions meet our requirements and guidelines.
 
_Italic contents are **suggestions**_, while the rest are **requirements**, both serving as references for your development process and for catalogue maintainers when reviewing PRs. Pay particular attention to **bolded ones**.

We hope this guide can be a great starting point for you!

## Adding or modifying plugin?

### Is your plugin suitable for the catalogue?

Do not submit plugins in a hurry. Before creating and submitting new plugins, consider the following questions:

- **Is your plugin packaged? —— Solo or directory plugin is not acceptable**;
- _Is there already a plugin with really similar functionality? —— Unnecessarily reinventing wheels is not desirable_;
- _Is your code necessary to provide as an MCDR plugin? Would it be more suitable for PyPI? —— Consider the use purpose and make sure it is necessary_;
- _Is the plugin commonly applicable? Can new users have reasons to use your plugin? —— Do not submit self-use only or completely useless plugins_;
- _Is your project ready for public testing (beta)? —— If it is still in an early stage, wait until it is ready. We recommend to ensure that the plugin has an available release when submitting_.

### Attention to copyrights

Users submitting plugins to the plugin catalogue should be in one of the following capacities:
- Author, maintainer, or collaborator of the plugin;
- An uploader who has explicit permission from someone above in writing.

If your plugin references or uses codes from other projects:
- If the codes is open source, follow their open source license;
- If the codes is proprietary, make sure you have the right to use them, and follow their agreement.

**We strongly recommend that you [use an open source licence](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) to protect rights of yours and others**. Operations performed by catalogue and MCDR on your repos should compatible with all OSI-approved licences.

**Otherwise, please understand and acknowledge that**:
- **By submitting your plugin, you grant anyone, over and above the proprietary agreement (or license, if any): the right to use, copy, and distribute your plugin and its source code direct or indirectly.**;
- **Your submission PR may take longer to process**.

### Uniqueness and compatibility

- Plugin name and ID should not be **too similar** to other plugins;  
  _As a reference, a quantification standard is: the [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between the lowercase name and ID of your plugin and other's should not be less than 3_
- Explicitly declare required plugins and/or Python packages in corresponding fields  
  _Mind if your plugin uses specific interfaces in new versions of MCDR, declare the MCDR version as necessary_;
- Make sure that your plugin works properly on target platforms.

### Write plugin information correctly

**Create or edit `plugin_info.json` as described in [documentation](https://docs.mcdreforged.com/en/latest/plugin_dev/plugin_catalogue.html).**

- _Check the `label` field is appropriate by referring to existing plugins and the documentation_;
- _The plugin README should be placed in `related_path` and named `README.md` (case insensitive)_.
- **Plugin ID must be consistent at all places**;
- **`description` and `introduction` fields should provide in correct language, at least provide in `en_us`**;

### Introduce your plugin properly

A good and detailed introduction is one of the conditions for becoming an excellent plugin.

- In the README or documentation, explain the plugin's functions, features, usage, etc. in detail;
- In the `description`, briefly summarise what the plugin does in one sentence;
- Introduce the plugin's features in the `introduction`, or direct reference it to the README file.

### One PR for one thing

- When adding plugins, please submit multiple plugins in separate PRs;
- When modifying plugins, changes to the same fields in multiple plugins by the same author can be combined in one PR;
- When deleting plugins, multiple plugins of the same author can be combined in one PR.

### Wait patiently after submitting

After submitting a PR, catalogue maintainers will review your plugin asap. They will base their response on the results of automatic checks, this guide, and their personal judgment. If they can not make a decision, your PR may be assigned to a higher-level maintainer. During this process, you can choose whether or not to accept their suggestions (if any). Those suggestions may help your plugin merge more smoothly into the catalogue.

### Be careful when releasing

**Refer to the [documentation](https://docs.mcdreforged.com/en/latest/plugin_dev/plugin_catalogue.html#release) when releasing plugin versions.**

- **The Release must be tagged in correctly**, otherwise the catalogue will not be able to get that version;
- Upload the packaged plugin (`.mcdr` or `.pyz`) as an asset.

## Contributing to scripts or workflows?

- It is recommended to create an Issue first, describing the problem or request, and then create the PR associated with it;
- All changes should be merged into the `master` branch.

_This text was originally written in `zh_cn`. Feel free to reach out if you have any questions._
