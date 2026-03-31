# TIDAS SDKs

A comprehensive multi-language SDK project for TIDAS (TianGong Life Cycle Assessment data format), providing implementations for working with ILCD/TIDAS data across multiple programming languages.

## 🚀 Quick Start

### TypeScript SDK (Recommended)

```bash
npm install @tiangong-lca/tidas-sdk
```

### Python Tools

```bash
pip install tidas-tools
```

### Python SDK (Development)

```bash
# Development version - install from source
cd sdks/python && uv sync
```

## 📦 Available Packages

### @tiangong-lca/tidas-sdk (TypeScript)

- **Status**: ✅ Production Ready
- **Features**: Type-safe data manipulation, validation, XML conversion, directory tools, schema generation
- **Installation**: `npm install @tiangong-lca/tidas-sdk`
- **Location**: `sdks/typescript/`

### tidas-tools (Python)

- **Status**: ✅ Production Ready
- **Features**: Database/export utilities, legacy Python conversion workflow, upstream schemas/assets
- **Installation**: `pip install tidas-tools`
- **Repository**: external upstream package (`tiangong-lca/tidas-tools`)

### tidas-sdk (Python, Development)

- **Status**: 🚧 In Development
- **Features**: Pydantic-based data models, validation, utilities
- **Installation**: Development only (from source)
- **Location**: `sdks/python/`

## 🏗️ Project Structure

```
tidas-sdk/
├── sdks/
│   ├── typescript/           # TypeScript SDK (production)
│   └── python/              # Python SDK (development)
└── scripts/                 # Build utilities
```

## 📚 Documentation

- **Repository Workflow**: [AGENTS.md](./AGENTS.md)
- **Release Setup**: [docs/release-setup.md](./docs/release-setup.md)
- **Upstream Automation Design**: [docs/upstream-automation.md](./docs/upstream-automation.md)
- **TypeScript Release Guide**: [sdks/typescript/RELEASE.md](./sdks/typescript/RELEASE.md)
- **Python Release Guide**: [sdks/python/RELEASE.md](./sdks/python/RELEASE.md)

## 🛠️ Development

### Prerequisites

- **TypeScript SDK**: Node.js 24+, npm
- **Python SDK/Tools**: Python 3.8+, uv (recommended)

### Setup

#### TypeScript SDK

```bash
cd sdks/typescript
npm install
npm run build
npm test
```

#### Python SDK

```bash
cd sdks/python
uv sync
uv run pytest
uv run mypy .
```

#### Refresh Upstream TIDAS Sources

```bash
./scripts/ci/generate-typescript-sdk.sh
./scripts/ci/generate-python-sdk.sh
```

Both generation scripts resolve `tidas-tools` in this order:

1. `TIDAS_TOOLS_PATH`
2. a sibling checkout at `../tidas-tools`
3. a temporary clone of `tiangong-lca/tidas-tools`

For the TypeScript package, this refresh also syncs the packaged runtime conversion assets copied from `tidas-tools/src/tidas_tools/{tidas,eilcd}`.

### Release Workflow

Normal releases are tag-driven and published by GitHub Actions:

- TypeScript package: create `typescript-vX.Y.Z` on the merged release commit
- Python package: create `python-vX.Y.Z` on the merged release commit

If you want `tidas-tools` changes to automatically regenerate and release these packages, see [docs/upstream-automation.md](./docs/upstream-automation.md).

Use these local verification commands before opening a release PR:

```bash
./scripts/ci/verify-typescript-package.sh
./scripts/ci/verify-python-package.sh
```

## 🎯 Current Status

### ✅ Completed

- TypeScript SDK with full TIDAS schema support
- Data validation using Zod schemas
- XML conversion and directory tooling for the non-export `tidas-tools` workflow
- Property access and manipulation utilities
- Python tools for data conversion and validation
- Comprehensive type generation from JSON schemas

### 🚧 In Development

- Python SDK implementation with Pydantic models
- Test coverage improvements
- Additional language implementations (Java planned)

### 📋 Roadmap

#### Short Term

- Complete Python SDK development
- Improve test coverage across all packages
- Enhanced documentation and examples

#### Long Term

- Java SDK implementation
- Performance optimizations
- Additional utility tools

## 🤝 Contributing

We welcome contributions! Please see [AGENTS.md](./AGENTS.md) for:

- Code style standards
- Testing requirements
- Development workflow
- Getting started instructions

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

## 🔗 Links

- **npm Package**: [@tiangong-lca/tidas-sdk](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk)
- **PyPI Package**: [tidas-tools](https://pypi.org/project/tidas-tools/)
- **Upstream Schemas/Tools**: [github.com/tiangong-lca/tidas-tools](https://github.com/tiangong-lca/tidas-tools)
- **Repository**: [github.com/tiangong-lca/tidas-sdk](https://github.com/tiangong-lca/tidas-sdk)

## 📞 Support

For questions, issues, or contributions:

- Open an issue on GitHub
- Check existing documentation
- Review the repository workflow in [AGENTS.md](./AGENTS.md)
