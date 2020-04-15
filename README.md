Publishing Projects

django app to collect a database of publishing projects systemwide at UC

Designed to be installed inside of https://github.org/ucldc/avram

#
These commands need to be run from the "host" django app

common django commands
```
python manage.py migrate
python manage.py createsuperuser
```

special django commands to initial load data from the original spreadsheet
```
python manage.py unit_ids
python manage.py publications
```

## avram

This is the avram dev server command

```
python manage.py runserver --settings=collection_registry.test_settings
```
