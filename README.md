# Cookiecutter DS

A generic Cookiecutter template for data science projects.


## Usage

Make sure you have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed:

```console
pip install cookiecutter
```

Download and create project structure:

```console
cookiecutter https://github.com/arthurcgusmao/cookiecutter-ds
```

After running the command above, cookiecutter will prompt you for:

1. `project_name`: Name of the project, to be inserted in the README file;
2. `project_repo`: Name of the repository, the directory to be created in your current working directory;
3. `author_name`: Name of author or organization, to be inserted in the LICENSE file;
4. `description`: Brief description of the project, to be inserted in the README file;
5. `open_source_license`: One of Apache-2.0, MIT, GPL-3.0, or none.

The created directory will have the structure below:

```text
project_name/
├── data
├── notebooks
├── src
|   └── __init__.py
├── .gitignore
├── LICENSE
├── Makefile
└── README.md
```


## License

Cookiecutter DS is licensed under the [Apache License, Version 2.0](./LICENSE).


## Acknowledgements

This template has been motivated and partly adapted from [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science).
