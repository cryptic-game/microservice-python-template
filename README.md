<!-- change microservice name and links in badge -->
# microservice-python-template [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=cryptic-game_microservice-python-template&metric=coverage)](https://sonarcloud.io/dashboard?id=cryptic-game_microservice-python-template)

A template for new python microservices

## files to change
 - `app.py` (change microservice name and import endpoints from `resources`)
 - `Pipfile` and `Pipfile.lock` for new dependencies only
 - `schemes.py` for user endpoint requirements and responses
 - `models/*` for database models
 - `resources/*` for user and microservice endpoints
 - `tests/*` for unit tests
 - update microservice name and endpoints in `tests/test_app.py` 
 - update microservice name in `.github/workflows/`

## tests
When writing unit tests make sure to `from mock.mock_loader import mock` **before** importing anything from `models` or `resources`.
