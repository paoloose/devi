<p align="center">
    <h1 align="center">devi</h1>
</p>

<p align="center">
  <samp>devi is a cli tool for managing your project templates</samp>
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

- `add` - Create a new template
- `create` - Create a new project from a template
- `list` - List available templates

`$DEVI_HOME` is the special directory where `devi` stores its configuration
files and templates. By default is set to `~/.devi` or `%USERPROFILE%\.devi` on
Windows.

The directory structure of `$DEVI_HOME` is as follows:

```ocaml
$DEVI_HOME
├── config.toml # see Configuration files
└── templates
    ├── my_template1 # see Template structure
    │   ├── template.devi.toml
    │   ├── file1
    │   └── file2
    └── ...
```

---

## Commands

### Add a new template

The `add` command creates a new template to `$DEVI_HOME/templates`.

```bash
devi add <path> [<template_name>]
# Both are required, since infering them is somewhat ambiguous

devi add . my_template

devi add ~/dev/my_template
```

### Create a new project from a template

The `create` command creates a new project from an existing template.

Aliases: `new`, `n`, `init`, `i`

```bash
devi create <template_name> [<destination>] [--name=<project-name>] [--dest=<destination>]

# Syntactic sugar:
devi create <template_name> as <project_name> in <destination>
```

If parameters `project_name` or `destination` are not set, `devi` will use
the values defined in the `template.devi.toml`
[template config](#template-configuration-file)).

To see the list of available templates, run `devi list`.

## Template structure

```bash
$DEVI_HOME/templates
├── my_template
│   ├── template.devi.toml
│   ├── files
│   ├── dirs/
│   └── ...
```

### Template configuration file

The `template.devi.toml` file is used to configure the template. This file is
**optional**, and has the following structure:

```toml
# Default values
name = ''
description = ''
destination = '.'
oncreate = ''
change_dir = true # (not implemented yet)
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
`*.devi.*` extension will be removed from the project. i.e.:
`whatever.devi.sh`, `my_dir.devi/`, and the `template.devi.toml` itself.

> Note: the `change_dir` only works on *nix for now

## Development

Requires python `>= 3.7`.

```bash
# In the root project, install an editable version of devi
pip install -e .
# For working on it
alias devi="python3 -m devi"
```
