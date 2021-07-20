# Contributing to DHost dashboard

## Setup

```bash
yarn install
```

```bash
yarn start
```

To bundle the app and serve it with Django run `build`, this will create a `build` folder containing the index file and all the static resources.

```bash
yarn build
```

## Folders

* `components` all generic components.
* `contexts` all contexts.
* `locale` i18n translations.
* `pages` pages or routers.

## Guidelines

* When adding features write unit tests.
* Limit API calls.
* Use formater `prettier` with: `yarn prettier`.
* Define a function with keyword `function`.
* Limit custom style to a strict minimum, use Bootstrap instead.
* Style must be in the same folder has component or page.

### Function names

| Name             | Description                       |
| ---              | ---                               |
| `list`           | `GET` List objects.               |
| `create`         | `POST` Create object.             |
| `retrieve`       | `GET` Retrieve object.            |
| `update`         | `PUT` Update an object.           |
| `partial_update` | `PATCH` Partial update an object. |
| `destroy`        | `DEL` Destroy an object.          |
