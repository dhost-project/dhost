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

### Function names

| Name             | Description                       |
| ---------------- | --------------------------------- |
| `list`           | `GET` List objects.               |
| `create`         | `POST` Create object.             |
| `retrieve`       | `GET` Retrieve object.            |
| `update`         | `PUT` Update an object.           |
| `partial_update` | `PATCH` Partial update an object. |
| `destroy`        | `DEL` Destroy an object.          |
