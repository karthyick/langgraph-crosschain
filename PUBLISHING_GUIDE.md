# 📦 Publishing to PyPI - Complete Guide

## Pre-Publishing Checklist

- [x] Project structure is correct
- [x] pyproject.toml configured
- [x] README.md with documentation
- [x] LICENSE file (MIT)
- [x] Tests passing
- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] Package name available on PyPI
- [ ] Test on TestPyPI first
- [ ] Final review complete

## Step 1: Update Package Metadata

### Update pyproject.toml

```toml
[project]
name = "langgraph-crosschain"  # Must be unique on PyPI
version = "0.1.0"  # Follow semantic versioning
description = "Cross-chain node communication framework for LangGraph"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [
    {name = "Karthick Raja M", email = "your.email@example.com"}
]
keywords = ["langgraph", "langchain", "cross-chain", "agents", "ai", "llm", "multi-agent"]
classifiers = [
    "Development Status :: 4 - Beta",  # Update from Alpha to Beta when ready
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]

[project.urls]
Homepage = "https://github.com/karthyick/langgraph-crosschain"
Documentation = "https://langgraph-crosschain.readthedocs.io"
Repository = "https://github.com/karthyick/langgraph-crosschain"
"Bug Tracker" = "https://github.com/karthyick/langgraph-crosschain/issues"
```

## Step 2: Create PyPI Accounts

### 2.1 Register on TestPyPI (for testing)
1. Go to https://test.pypi.org/account/register/
2. Create an account
3. Verify your email

### 2.2 Register on PyPI (for production)
1. Go to https://pypi.org/account/register/
2. Create an account
3. Verify your email

### 2.3 Generate API Tokens
1. Go to Account Settings → API tokens
2. Create a new API token
3. Save it securely (you'll need it for publishing)

## Step 3: Prepare Your Package

### 3.1 Install Build Tools

```bash
pip install --upgrade pip setuptools wheel twine build
```

### 3.2 Run Tests

```bash
pytest tests/
```

### 3.3 Check Package Structure

```bash
tree -I '__pycache__|*.egg-info|.git' -L 2
```

## Step 4: Build Your Package

### 4.1 Clean Previous Builds

```bash
rm -rf dist/ build/ *.egg-info/
```

### 4.2 Build the Package

```bash
python -m build
```

This creates:
- `dist/langgraph_crosschain-0.1.0.tar.gz` (source distribution)
- `dist/langgraph_crosschain-0.1.0-py3-none-any.whl` (wheel distribution)

## Step 5: Test on TestPyPI First

### 5.1 Upload to TestPyPI

```bash
twine upload --repository testpypi dist/*
```

When prompted:
- Username: `__token__`
- Password: Your TestPyPI API token

### 5.2 Test Installation

```bash
# Create a test virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ langgraph-crosschain

# Test import
python -c "from langgraph_crosschain import ChainRegistry; print('Success!')"
```

## Step 6: Publish to PyPI

### 6.1 Final Checks

```bash
# Check distribution
twine check dist/*

# Verify all files are included
tar -tzf dist/langgraph-crosschain-*.tar.gz | head -20
```

### 6.2 Upload to PyPI

```bash
twine upload dist/*
```

When prompted:
- Username: `__token__`
- Password: Your PyPI API token

## Step 7: Verify Installation

```bash
# Install from PyPI
pip install langgraph-crosschain

# Verify
python -c "from langgraph_crosschain import ChainRegistry, CrossChainNode; print('Package successfully installed!')"
```

## Step 8: Post-Publishing Tasks

### 8.1 Create GitHub Release

```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

Then create a release on GitHub with release notes.

### 8.2 Update Documentation

Add installation instructions to README:

```markdown
## Installation

```bash
pip install langgraph-crosschain
```
```

### 8.3 Announce Your Package

1. **LangChain Discord/Slack**: Share in the community
2. **Twitter/LinkedIn**: Announce the release
3. **Dev.to/Medium**: Write an article
4. **Reddit**: r/MachineLearning, r/Python
5. **GitHub**: Add topics for discoverability

## Automation: GitHub Actions for Publishing

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    
    - name: Build package
      run: python -m build
    
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: |
        twine upload dist/*
```

## Alternative: Using Poetry

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Configure Poetry

```bash
poetry config pypi-token.pypi your-api-token
```

### Build and Publish

```bash
poetry build
poetry publish
```

## Common Issues and Solutions

### Issue 1: Package Name Already Taken
**Solution**: Choose a unique name like:
- `langgraph-crosschain-framework`
- `crosschain-langgraph`
- `langgraph-xchain`

### Issue 2: Missing Files in Distribution
**Solution**: Update `MANIFEST.in`:

```
include README.md
include LICENSE
include CHANGELOG.md
recursive-include langgraph_crosschain *.py
recursive-include tests *.py
recursive-include examples *.py
```

### Issue 3: Version Conflicts
**Solution**: Use version ranges in dependencies:

```toml
dependencies = [
    "langgraph>=0.2.0,<1.0.0",
    "langchain>=0.1.0,<1.0.0",
    "pydantic>=2.0.0,<3.0.0",
]
```

## Security Best Practices

1. **Never commit tokens**: Use environment variables
2. **Use 2FA**: Enable on PyPI account
3. **Sign releases**: Use GPG signing
4. **Scan for secrets**: Use tools like `gitleaks`

## Maintenance After Publishing

### Version Updates

```bash
# Patch version (bug fixes): 0.1.0 → 0.1.1
# Minor version (new features): 0.1.0 → 0.2.0
# Major version (breaking changes): 0.1.0 → 1.0.0
```

### Update Process

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Run tests
4. Build and upload new version
5. Create GitHub release

## Success Metrics

- PyPI downloads: `pip install pypistats && pypistats recent langgraph-crosschain`
- GitHub stars and forks
- Community feedback
- Issue reports and PRs

## Next Steps

1. ✅ Set up ReadTheDocs for documentation
2. ✅ Add badges to README (PyPI version, downloads, license)
3. ✅ Create example notebooks
4. ✅ Write blog post about the framework
5. ✅ Submit to awesome-langchain list
