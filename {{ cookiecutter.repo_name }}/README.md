# {{cookiecutter.project_name}}

{{cookiecutter.description}}
{% if cookiecutter.open_source_license != 'No license file' %}

## License

{{cookiecutter.project_name}} is licensed under the [{% if cookiecutter.open_source_license == 'Apache-2.0' %}Apache License, Version 2.0{% elif cookiecutter.open_source_license == 'MIT' %}MIT License{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GNU General Public License{% endif %}](./LICENSE).
{% endif %}
