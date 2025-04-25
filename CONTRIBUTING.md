# Contributing

Thank you for considering contributing to Colorally !  
This document provides guidelines for contributing to the project.

## What Should I Know Before I Get Started?

Colorally is a tool designed to generate color palettes that are distinguishable for:
- People with normal vision
- People with color blindness (protanopia, deuteranopia, tritanopia)
- Grey scale printing

The project is based on the work of Nicolas Burrus's DaltonLens research and Machado et al.'s research on color perception.

## How Can I Contribute?

### Finding Tasks

Check the GitHub Issues section for tasks that need attention.  
Feel free to comment on issues if you need clarification or want to take on a task.

If you find English errors, potential optimizations, or have other improvements in mind, you are welcome to make corrections and submit a pull request with a detailed description of your changes.

### Suggesting Ideas

Open an issue describing your suggestion and how it could benefit the project. Keep it simple and clear.

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Ensure all doctests pass (`./run_tests.sh`)
4. Submit your pull request with a clear description of the changes or the related issue ID

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/pieetie/colorally.git
   cd colorally
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   ./run_tests.sh
   ```

Thank you for your contribution! 🎨