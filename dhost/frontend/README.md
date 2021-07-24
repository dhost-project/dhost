# DHost dashboard

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits. You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.

See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder. It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes. Your app is ready to be deployed!

When the app is built this allow Django to serve it from the `build` folder, the `index.html` is used has a template.

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn prettier`

Format the code with prettier, you can also run `yarn prettier-check` to disable the modification of files.

### `yarn lint`

Lint the code with eslint.

## Dev guidelines

### Folders

- `api` all API calls components.
- `components` all generic components.
- `contexts` all contexts.
- `locale` i18n translations.
- `pages` pages or routers.

### Guidelines

- When adding features write unit tests.
- Limit API calls.
- Use formater `prettier` with: `yarn prettier`.
- Define a function with keyword `function`.
- Limit custom style to a strict minimum, use Bootstrap instead.
- Style must be in the same folder has component or page.
- Use `id` to style a single element, `class` to style multiple elements.

### Function names

| Name             | Description                              |
| ---------------- | ---------------------------------        |
| `List`           | Objects list page/component.             |
| `Add`            | Add a new object page/component.         |
| `Details`        | Object's details page/component.         |
| `Edit`           | Edit object page/component.              |
| `Delete`         | Delete object page/component.            |
| `list`           | API `GET` to list objects.               |
| `create`         | API `POST` to create object.             |
| `retrieve`       | API `GET` to retrieve object.            |
| `update`         | API `PUT` to update an object.           |
| `partial_update` | API `PATCH` to partial update an object. |
| `destroy`        | API `DEL` to destroy an object.          |
