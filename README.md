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
- **Status**: ✅ Production Ready (v0.1.20)
- **Features**: Type-safe data manipulation, validation, schema generation
- **Installation**: `npm install @tiangong-lca/tidas-sdk`
- **Location**: `sdks/typescript/`

### tidas-tools (Python)
- **Status**: ✅ Production Ready
- **Features**: Data format conversion, validation, export utilities
- **Installation**: `pip install tidas-tools`
- **Location**: `tidas-tools/`

### tidas-sdk (Python, Development)
- **Status**: 🚧 In Development (v0.1.0)
- **Features**: Pydantic-based data models, validation, utilities
- **Installation**: Development only (from source)
- **Location**: `sdks/python/`

## 🏗️ Project Structure

```
tidas-sdk/
├── sdks/
│   ├── typescript/           # TypeScript SDK (production)
│   └── python/              # Python SDK (development)
├── tidas-tools/             # Python utilities (production)
├── docs/                    # Project documentation
├── specs/                   # Feature specifications
└── scripts/                 # Build utilities
```

## 📚 Documentation

- **Development Guidelines**: [CLAUDE.md](./CLAUDE.md)
- **Development Progress**: [docs/development-progress.md](./docs/development-progress.md)
- **Requirements & Design**: [docs/requirement-design.md](./docs/requirement-design.md)
- **Technical Design**: [docs/technical-design.md](./docs/technical-design.md)

## 🛠️ Development

### Prerequisites
- **TypeScript SDK**: Node.js 14+, npm
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

#### Tools Package
```bash
cd tidas-tools
uv sync
uv run pytest
```

## 🎯 Current Status

### ✅ Completed
- TypeScript SDK with full TIDAS schema support
- Data validation using Zod schemas
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

We welcome contributions! Please see our development guidelines in [CLAUDE.md](./CLAUDE.md) for:
- Code style standards
- Testing requirements
- Development workflow
- Getting started instructions

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

## 🔗 Links

- **npm Package**: [@tiangong-lca/tidas-sdk](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk)
- **PyPI Package**: [tidas-tools](https://pypi.org/project/tidas-tools/)
- **Repository**: [github.com/tiangong-lca/tidas-sdk](https://github.com/tiangong-lca/tidas-sdk)

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review development progress in [docs/development-progress.md](./docs/development-progress.md)
