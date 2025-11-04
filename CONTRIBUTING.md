# Contributing to LangGraph Cross-Chain Communication Framework

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

By participating in this project, you agree to:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Prioritize the community's best interests

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/langgraph-crosschain.git
   cd langgraph-crosschain
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/original-org/langgraph-crosschain.git
   ```

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pip
- git

### Install Development Dependencies

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Verify Installation

```bash
# Run tests
pytest

# Check code formatting
black --check langgraph_crosschain tests

# Run linter
ruff check langgraph_crosschain tests

# Type checking
mypy langgraph_crosschain
```

## Making Changes

### Create a Branch

Create a branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or modifications

### Development Workflow

1. **Make your changes** in focused, logical commits
2. **Write tests** for new functionality
3. **Update documentation** as needed
4. **Run tests** to ensure everything passes
5. **Format code** with Black
6. **Check with linter** using Ruff
7. **Type check** with mypy

### Commit Messages

Write clear, descriptive commit messages:

```
Add cross-chain event streaming support

- Implement EventStream class for real-time events
- Add subscribe/unsubscribe methods
- Include tests for event propagation
- Update documentation with usage examples
```

Format:
- First line: Brief summary (50 chars or less)
- Blank line
- Detailed description with bullet points if needed

## Submitting Changes

### Before Submitting

- [ ] All tests pass
- [ ] Code is formatted with Black
- [ ] No linting errors from Ruff
- [ ] Type checking passes with mypy
- [ ] Documentation is updated
- [ ] CHANGELOG is updated (if applicable)

### Create a Pull Request

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description explaining what and why
   - Link to related issues (if any)
   - Screenshots/examples (if applicable)

3. **Wait for review** and address feedback

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested the changes

## Checklist
- [ ] Tests pass locally
- [ ] Code formatted with Black
- [ ] No linting errors
- [ ] Documentation updated
- [ ] CHANGELOG updated
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with these specifics:

- **Line length**: 100 characters
- **Formatting**: Black (automatic)
- **Linting**: Ruff
- **Type hints**: Required for public APIs
- **Docstrings**: Google style

### Example Code Style

```python
from typing import Dict, Any, Optional


class MyClass:
    """Brief description of the class.

    More detailed description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Example:
        >>> instance = MyClass("value")
        >>> result = instance.method()
    """

    def __init__(self, param1: str, param2: Optional[int] = None) -> None:
        """Initialize MyClass."""
        self.param1 = param1
        self.param2 = param2

    def method(self, data: Dict[str, Any]) -> str:
        """Brief description of method.

        Args:
            data: Dictionary of input data

        Returns:
            Processed result as string

        Raises:
            ValueError: If data is invalid
        """
        if not data:
            raise ValueError("Data cannot be empty")

        return f"Processed: {data}"
```

## Testing

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Use descriptive test names
- Test both success and failure cases
- Aim for high coverage (>90%)

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_chain_registry.py

# Run with coverage
pytest --cov=langgraph_crosschain --cov-report=html

# Run specific test
pytest tests/test_chain_registry.py::TestChainRegistry::test_register_chain
```

### Test Structure

```python
import pytest


class TestFeature:
    """Test suite for Feature."""

    def setup_method(self):
        """Set up test fixtures."""
        # Setup code here

    def test_basic_functionality(self):
        """Test basic functionality works as expected."""
        # Test code here
        assert result == expected

    def test_error_handling(self):
        """Test that errors are handled correctly."""
        with pytest.raises(ValueError, match="expected error"):
            # Code that should raise error
            pass
```

## Documentation

### Docstring Format

Use Google-style docstrings:

```python
def function(arg1: str, arg2: int = 0) -> bool:
    """Brief description.

    Longer description if needed.

    Args:
        arg1: Description of arg1
        arg2: Description of arg2 (default: 0)

    Returns:
        True if successful, False otherwise

    Raises:
        ValueError: If arg1 is empty
        TypeError: If arg2 is not an integer

    Example:
        >>> result = function("test", 5)
        >>> print(result)
        True
    """
```

### Updating Documentation

- Update README.md for user-facing changes
- Update docstrings for API changes
- Add examples for new features
- Update CHANGELOG.md

## Questions?

If you have questions:

1. Check existing issues and discussions
2. Search the documentation
3. Open a new issue with the "question" label
4. Join our community discussions

## Recognition

Contributors will be:
- Listed in the project's contributors
- Acknowledged in release notes
- Celebrated in our community

Thank you for contributing! 🎉
