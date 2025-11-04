# Windows Quick Start Guide

## 🎯 For Windows Users

This guide helps you get started with the LangGraph Cross-Chain Framework on Windows.

## ✅ Installation

### Step 1: Install the Package

```powershell
# Make sure you're in the crosschain directory
cd C:\Users\YourUser\path\to\crosschain

# Install in editable mode
pip install -e .
```

### Step 2: Install Test Dependencies (Optional)

```powershell
# For running tests
pip install pytest pytest-cov pytest-asyncio
```

**Output you should see:**
```
Successfully installed langgraph-crosschain-0.1.0 ...
```

## 🚀 Running Examples

### Working Examples (Start Here!)

#### 1. Shared State Example (RECOMMENDED) ⭐
**This one works perfectly on Windows!**

```powershell
python examples\shared_state_example.py
```

**Expected Output:**
```
======================================================================
Shared State Coordination Example
======================================================================

Registered chains: {'processor', 'producer', 'consumer'}

----------------------------------------------------------------------
STEP 1: Producer produces data
----------------------------------------------------------------------
Producer: Producing data...
Producer: Stored data in shared state: {...}

... [more output] ...

✓ Producer: Completed successfully
✓ Consumer: Completed successfully
✓ Processor: Completed successfully

Shared state coordination successful!
```

#### 2. Simple Working Example ⭐

```powershell
python examples\simple_working_example.py
```

This demonstrates fire-and-forget message passing between chains.

## ⚠️ Known Issues on Windows

### Issue 1: pytest Coverage Error

**Error:**
```
pytest: error: unrecognized arguments: --cov=langgraph_crosschain
```

**Solution:**
```powershell
# Install pytest-cov
pip install pytest-cov

# Then run tests
pytest
```

### Issue 2: Path Separators

Windows uses `\` but Python accepts both `/` and `\`.

**Both work:**
```powershell
python examples\shared_state_example.py    # Windows style
python examples/shared_state_example.py     # Unix style (also works)
```

### Issue 3: Virtual Environment

**Recommended:** Use a virtual environment

```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

# Install package
pip install -e .
```

## 📝 Quick Test

Run this to verify installation:

```powershell
python -c "from langgraph_crosschain import ChainRegistry; print('✓ Installation successful!')"
```

## 🧪 Running Tests

```powershell
# Make sure pytest-cov is installed
pip install pytest pytest-cov pytest-asyncio

# Run all tests
pytest

# Run specific test file
pytest tests\test_chain_registry.py

# Run with verbose output
pytest -v

# Run without coverage (if you don't have pytest-cov)
pytest --no-cov
```

## 💡 What to Try

1. **Start with Shared State Example** - It's the most reliable
   ```powershell
   python examples\shared_state_example.py
   ```

2. **Try Simple Working Example** - Shows message passing
   ```powershell
   python examples\simple_working_example.py
   ```

3. **Run the tests** - Verify everything works
   ```powershell
   pytest -v
   ```

4. **Build your own** - Use the examples as templates

## 📚 Next Steps

- Read `EXAMPLES_GUIDE.md` for detailed explanations
- Read `IMPLEMENTATION_GUIDE.md` for complete API reference
- Check `tests/` for more usage examples

## 🆘 Troubleshooting

### Problem: ModuleNotFoundError

```
ModuleNotFoundError: No module named 'langgraph_crosschain'
```

**Solution:**
```powershell
pip install -e .
```

### Problem: Import errors for langgraph

```
ModuleNotFoundError: No module named 'langgraph'
```

**Solution:**
```powershell
pip install -e .  # This installs all dependencies
```

### Problem: Examples don't run

**Solution:**
Make sure you're in the project root directory:
```powershell
# Check you're in the right place
dir pyproject.toml  # Should show the file

# Run example
python examples\shared_state_example.py
```

## ✅ Verification Checklist

Before asking for help:

- [ ] Installed package: `pip install -e .`
- [ ] Can import: `python -c "import langgraph_crosschain"`
- [ ] Examples directory exists: `dir examples`
- [ ] Using Python 3.9 or higher: `python --version`
- [ ] All dependencies installed

## 🎓 Learning Path for Windows Users

1. **Verify installation** - Run the import test above
2. **Run shared_state_example.py** - See it work!
3. **Read the example code** - Understand what's happening
4. **Run simple_working_example.py** - Try message passing
5. **Run tests** - `pytest -v`
6. **Build something** - Use examples as templates

## 📧 Getting Help

If you're stuck:

1. Check this guide first
2. Read `EXAMPLES_GUIDE.md`
3. Read `IMPLEMENTATION_GUIDE.md`
4. Check the test files in `tests/` for examples
5. Open an issue on GitHub

## 🎉 Success!

If you can run the examples and see output, you're ready to go!

**Example Success Output:**
```
✓ Producer: Completed successfully
✓ Consumer: Completed successfully
✓ Processor: Completed successfully

Shared state coordination successful!
```

Happy coding on Windows! 🚀
