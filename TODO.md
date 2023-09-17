# TODO ideas

- `devi add <template_name> <dir> [--edit]`

  For editing the template config file, we could use the `EDITOR`
  environment variable, or a flag like `--edit <editor>`.

- When creating a template, add variable `--current-dir` so that the
  destination directory is the current directory.

- In the name property, put variables to replace, like:
  - `{name}` (for the name of the template)
  - `{date}` (for the current date in the format `YYYY-MM-DD`)
  - `{time}` (for the current time in the format `HH:MM:SS`)
  - `{pid}` (for the current process id)
  - `{i}` (for the index of the file)

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

## Improve implementation of `change_dir`

`change_dir` functionality is tricky to implement since it requires to change the
`cwd` of the parent process (the shell). As far as I know, there is
[no standard or cross-platform way](https://stackoverflow.com/questions/2375003/how-do-i-set-the-working-directory-of-the-parent-process)
to achieve this.

Here are some workarounds that I think would work:

- Save the path of the proyect to the clipboard, so the user can paste it.
- Make a shell function like `devi-teleport` to evaluate it in the
  parent process like `devi create my_template && devi-teleport`.
- Make a temporary shell script in somewhere to evaluate in the parent.
  An alias for `devi` will look like this: `devi $@ &&`
  `source $DEVI_HOME/devi-teleport.sh`.

Update: see `devi/commands/create.py` for the current implementation. It uses
the [ioctl](https://docs.python.org/3/library/fcntl.html#fcntl.ioctl) system
call to inject input to the parent process (as if the user had manually typed
`cd /my/destination`)

Reference: https://unix.stackexchange.com/a/217390/565072
