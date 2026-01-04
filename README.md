# empanada-napari Documentation

This repository contains the source text and configuration for the [empanada-napari](https://github.com/volume-em/empanada-napari) documentation.

The site is built using **Sphinx** and hosted on **ReadTheDocs**.

## 🚀 Beginner's Guide to Building Locally

If you are new to Python or documentation, follow these step-by-step instructions to preview changes on your own computer.

### 1. Prerequisites

Ensure you have **Python 3.10** or newer installed.
- [Download Python here](https://www.python.org/downloads/)

### 2. Set up your environment

It is best practice to use a "virtual environment" to install dependencies. This keeps your project isolated from other Python software on your system.

Open your terminal (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows) and navigate to the project folder:

```bash
cd path/to/empanada-napari-docs
```

Run the following commands:

```bash
# 1. Create a virtual environment named 'venv'
python -m venv venv

# 2. Activate the virtual environment
# On macOS / Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```
*(You should see `(venv)` appear at the start of your command line, indicating the environment is active.)*

### 3. Install dependencies

Install the software required to build the documentation (like Sphinx and the theme).

```bash
pip install -r docs/requirements.txt
```

### 4. Build and Preview

There are two ways to view the documentation:

#### Option A: Live Preview (Recommended)
Use this utility to start a local server. It will automatically rebuild the docs and refresh your browser whenever you modify and save a file.

```bash
# Navigate to the documentation source directory
cd docs

# Start the auto-build server
# Syntax: sphinx-autobuild [source_dir] [output_dir]
sphinx-autobuild . _build/html
```

Click the link shown in the terminal (usually `http://127.0.0.1:8000`) to view the documentation. Press `Ctrl+C` to stop the server.

#### Option B: Standard Build
Use this if you just want to generate the files once without running a server.

```bash
cd docs
make html
```

You can then find the generated HTML files in `docs/_build/html/`. Open `index.html` in your web browser to view them.

## 📦 Deployment / Hosting

The documentation is hosted on **ReadTheDocs**.

Deployment is **automated**:
1. Make your edits and verify them locally using the steps above.
2. Commit your changes and **push** them to the GitHub repository.
3. ReadTheDocs will verify the `.readthedocs.yaml` file, install dependencies, and publish the new version automatically.

No manual server configuration is required for hosting.
