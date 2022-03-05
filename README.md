
# Rolsia

This repository contains the [Rolsia.com](https://rolsia.com) app written in [Django](https://www.djangoproject.com/).

## Running

### Locally
- Set up a local development environment, edit `local_settings_example.py` accordingly and rename it to `local_settings.py`.
- Create virtual environment, run `pipenv install` to install dependencies.

### Production

The app runs on a VPS. Configuration can be found in another repository.

## Test data

Running `python manage.py setup_test_data` will set up the database with fake data and also create a superuser `tester` with `tester` password.

It is sometimes useful to run after flushing the database with `python manage.py flush`.

## Localizations

### Adding a localization

1. Add a new record to `LANGUAGES` in `settings.py`.
2. Run `python manage.py makemessages -l lang_code`, where `lang_code` is the language code, i.e. `cs`.
3. Translate `locale/{lang_code}/LC_MESSAGES/django.po`
4. Run `python manage.py compilemessages -l lang_code`

### Updating localizations

1. Run `python manage.py makemessages --all`.
2. Localize files in `locale` folder.
3. Run `python manage.py compilemessages`.
