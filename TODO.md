
# TODO ideas

- `devi add <template_name> <dir> [--edit]`

  For editing the template config file, we could use the `EDITOR`
  environment variable, or a flag like `--edit <editor>`.

- When creating a template, add variable `--current-dir` so that the
  destination directory is the current directory.

- In the name property, put variables to replace, like:
  - `{{name}}` (for the name of the template)
  - `{{date}}` (for the current date in the format `YYYY-MM-DD`)
  - `{{time}}` (for the current time in the format `HH:MM:SS`)
  - `{{pid}}` (for the current process id)
  - `{{i}}` (for the index of the file)

## Interactive variables feature

If the `template.devi.toml` file has the `interactive` property set to
`true`, then the user will be prompted for the values of the variables
in the template.

```sh
devi create C++

✔️ Name of the project: test
✔️ Type of project:
  - [ ] Library
  - [ ] Executable
✔️ Repository URL: https://github.com/username/test
```

Or define them after the command:

```sh
devi create C++ [--name <test> | --type <library> | --repo <url>]
```
