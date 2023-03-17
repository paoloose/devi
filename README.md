<p align="center">
    <h1 align="center">devi</h1>
</p>
<p align="center">
  <code>devi is a cli tool for managing your project templates</code>
</p>

<p align="center">
<img src="https://img.shields.io/badge/pip%20install-devi--cli-blue"/>
<img src="https://shields.io/pypi/v/devi-cli"/>
<img src="https://shields.io/pypi/l/devi-cli"/>
</p>

With `devi` you can create, use, reuse and manage your project templates.

## Usage

<div align="justify">
<div align="center">

```bash
devi <command> [options]
```

</div>
</div>

Available commands:

- `add` - Add a new template to your list
- `create` - Create a new project from a template
- `list` - List available templates
- `rm` - remove a template

`$DEVI_HOME` is the special directory where `devi` stores your templates and
configuration. By default is set to `~/.devi` or `%USERPROFILE%\.devi` on
Windows (see [devi's home](#devis-home)).

---

## Usage

<!-- here might be a showcase video -->

### Add a new template

The `add` command adds a new template to `$DEVI_HOME/templates`.

```bash
devi add <path> [<template_name>]
```
```bash
devi add . my_new_template

# if template_name is not provided, devi will use the directory name
devi add ~/dev/my_template
```

### Create a new project from a template

The `create` command creates a new project from an existing template.

<!-- Aliases: `new`, `n`-->

```bash
devi create <template_name> [<destination>] [--name=<project-name>]

# or with syntactic sugar:
devi create <template_name> as <project_name> in <destination>
```
```bash
# this will create a new dir called "my_template"
devi create my_template .
# don't worry, you can give it a name
devi create my_template . --name=my_project
# equivalent to the following:
devi create my_template as my_project in .
```

Do you want more customization? we catch you!

Both parameters (`project_name` and `destination`) are optional. If not set,
`devi` will use the values defined in the `template.devi.toml` (see
[template config](#template-configuration-file)).

## Viewing and removing your templates

To see the list of available templates, run `devi list`. They are located on
`$DEVI_HOME/templates`.

Don't want a template anymore? Remove it with

```bash
devi rm <template-name> [-y]
```

It will ask you to confirm the deletion, you can skip this with the `-y` flag.

## Devi's home

`$DEVI_HOME` is special, the place where `devi` store its templates and
configuration.

By default is set to `~/.devi/templates`, but you can override it, e.g, for
bash:

```bash
echo "export DEVI_HOME=~/my/custom/devi" >> ~/.bashrc
```

The directory structure of `$DEVI_HOME` is as follows:

```ocaml
$DEVI_HOME
├── config.toml # see Configuration files
└── templates
    ├── my_template # see Template structure
    │   ├── template.devi.toml
    │   ├── file1
    │   └── file2
    └── ...
```

`TODO:` configuration file for devi is not ready yet

### Template configuration file

The `template.devi.toml` file is used to customize the template. This file is
**optional**, and has the following structure:

```toml
# Default values
name = ''
description = ''
destination = '.'
oncreate = ''
change_dir = true
```

- `name` - The name of the project. If not set, `devi` will use the name of the
directory where the template is located.
- `description` - A short description of the template used by `devi list`.
- `destination` - The destination directory where the project will be created
in.
- `oncreate` - A shell command that will be executed after the project has been
created. Relative paths are relative to the project directory.
- `change_dir` - If `true`, `devi` will change the current directory to the
project directory after the project has been created.

All the properties are optional.

After `oncreate` finishes its execution, all the files and directories with the
`*.devi.*` extension will be removed from the project. e.g.:
`whatever.devi.sh`, `my_dir.devi/`, and the `template.devi.toml` itself.

> **Note**
> Currently `change_dir` is not implemented for Windows (see [TODO.md](./TODO.md))

## Installation

```bash
pip install devi-cli
```
> **Note**
> Getting `error: externally-managed-environment` on Debian or other linux
> distros?
>
> See [this](https://github.com/python/cpython/issues/102134#issuecomment-1445428402).

## Development

Requires python `>= 3.7`.

```bash
# In the root project, install an editable version of devi
pip install -e .
# For working on it
alias devi="python3 -m devi"
```
