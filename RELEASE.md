# Release Guide for @tiangong-lca/tidas-sdk

This guide provides step-by-step instructions for releasing the TIDAS TypeScript SDK to npm.

## Prerequisites

- Node.js and npm installed
- npm account with access to publish packages
- Access to the `@tiangong-lca` organization on npm (or permission to create it)

## Pre-release Checklist

Before publishing, ensure all these items are completed:

- [ ] All tests pass: `npm test`
- [ ] Code lints successfully: `npm run lint`
- [ ] TypeScript compilation succeeds: `npm run typecheck`
- [ ] Build generates clean dist files: `npm run build`
- [ ] Documentation is up to date
- [ ] CHANGELOG.md is updated (if exists)

## Release Steps

### 1. Setup npm authentication

```bash
# Login to npm (first time only)
npm login

# Verify you're logged in
npm whoami
```

### 2. Prepare the release

```bash
# Ensure you're on the main branch
git checkout main
git pull origin main

# Update submodule to latest version
git submodule update --init --recursive
git submodule update --remote

# Regenerate types and schemas from updated submodule
npm run generate-types
npm run generate-schemas

# Clean install dependencies
npm ci

# Run full build and checks
npm run build
npm run lint
npm run typecheck
npm test
```

### 3. Update version

Choose the appropriate version bump:

```bash
# For bug fixes (0.1.0 → 0.1.1)
npm version patch

# For new features (0.1.0 → 0.2.0)
npm version minor

# For breaking changes (0.1.0 → 1.0.0)
npm version major
```

This will:

- Update the version in `package.json`
- Create a git commit with the new version
- Create a git tag

### 4. Publish to npm

```bash
# Publish the package (scoped packages need --access public)
npm publish --access public
```

### 5. Push changes to repository

```bash
# Push the version commit and tag
git push origin main --tags
```

### 6. Create GitHub release (optional)

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Select the version tag you just created
4. Add release notes describing changes
5. Publish the release

## Automated Release Scripts

For convenience, you can add these scripts to your `package.json`:

```json
{
  "scripts": {
    "prepublishOnly": "npm run build && npm run lint && npm run typecheck",
    "release:patch": "npm version patch && npm publish --access public && git push origin main --tags",
    "release:minor": "npm version minor && npm publish --access public && git push origin main --tags",
    "release:major": "npm version major && npm publish --access public && git push origin main --tags"
  }
}
```

Then you can simply run:

```bash
npm run release:patch   # for patch releases
npm run release:minor   # for minor releases
npm run release:major   # for major releases
```

## Package Information

- **Package name**: `@tiangong-lca/tidas-sdk`
- **Scope**: `@tiangong-lca`
- **Registry**: npm public registry
- **Access**: Public

## Installation for Users

Once published, users can install the package with:

```bash
npm install @tiangong-lca/tidas-sdk
```

Or with yarn:

```bash
yarn add @tiangong-lca/tidas-sdk
```

## Package Contents

The published package includes:

- `dist/` - Compiled JavaScript and TypeScript declaration files
- `README.md` - Package documentation
- `LICENSE` - MIT license file
- `package.json` - Package metadata

## Troubleshooting

### Permission denied errors

- Ensure you're logged in: `npm whoami`
- Check if you have access to the `@tiangong-lca` organization
- Contact the organization admin for access

### Build errors before publish

- Run `npm run clean` then `npm run build`
- Check for TypeScript errors: `npm run typecheck`
- Fix linting issues: `npm run lint:fix`

### Version conflicts

- Check existing versions: `npm view @tiangong-lca/tidas-sdk versions --json`
- Ensure you're incrementing from the latest version

## Best Practices

1. **Always test before publishing** - Run the full test suite
2. **Use semantic versioning** - Follow semver guidelines for version bumps
3. **Document changes** - Update README and/or CHANGELOG
4. **Clean builds** - Always build from a clean state
5. **Backup important releases** - Tag important releases in git
6. **Monitor after publish** - Check that the package installs correctly

## Support

For issues with the release process, check:

- [npm documentation](https://docs.npmjs.com/)
- [Semantic Versioning](https://semver.org/)
- Project issues in the GitHub repository
