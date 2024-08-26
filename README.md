# CodeRunner

`CodeRunner` is a Python utility designed to execute Jupyter Notebooks (`.ipynb`) and Python scripts (`.py`) concurrently using multithreading. This tool is particularly useful for running multiple notebooks or scripts in parallel without manual intervention.

## Features

- **Concurrent Execution**: Run multiple Jupyter Notebooks and Python scripts simultaneously.
- **Automatic Detection**: Automatically detects the type of file (either `.ipynb` or `.py`) and processes it accordingly.
- **Error Handling**: Provides clear error messages if any script fails to execute.

## Requirements

Before using `CodeRunner`, ensure you have the following installed:

- Python 3.x
- Jupyter Notebook
- nbformat
- nbconvert

You can install the required Python packages using pip:

```bash
pip install nbformat nbconvert
```

## Usage

To use the `CodeRunner` class, simply initialize it with a list of paths to the Jupyter Notebooks or Python scripts you want to run. The class will handle the rest, running each file in a separate thread.

### Example

```python
from code_runner import CodeRunner

# List of file paths to be executed
paths = [
    "script1.py",
    "notebook1.ipynb",
    "script2.py",
    "notebook2.ipynb"
]

# Initialize and run the CodeRunner
runner = CodeRunner(paths)
```

### Methods

- **`execute_ipynb(ipynb_path)`**: Executes a Jupyter Notebook. This method reads the notebook, runs it, and then saves the output back to the original file.
  
- **`execute_py(py_path)`**: Executes a Python script. It runs the script using the default Python interpreter.

### Error Handling

If a Python script encounters an error during execution, the error will be caught, and an error message will be printed to the console.

## Contributing

Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
