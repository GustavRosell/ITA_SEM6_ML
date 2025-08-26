# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure
This is a 15-week ML course organized by weekly modules. Each week follows this structure:
- `exercises/` - Progressive exercise files, often in subdirectories (exc01/, exc02/, etc.)
- `resources/` - PDFs, lecture notes, datasets, reference materials  
- `assignments/` - Homework and project submissions

Current modules:
- `01_Intro/` - Python basics, lists, GUI programming with Tkinter
- `02_Linear_Regression/` - NumPy, matplotlib, linear regression implementations
- `03_Logistic_Regression/` - (Structure ready)
- `04_Neural_Networks/` - (Structure ready)

## Development Environment
- **Python Environment**: Use the existing `.venv` virtual environment
  ```bash
  source .venv/bin/activate
  ```
- **Python Version**: 3.13.7
- **Key Dependencies**: numpy, matplotlib, jupyter, tkinter (built-in)
- **Jupyter Notebooks**: Used for some exercises (particularly in week 2+)
  ```bash
  jupyter notebook  # or jupyter lab
  ```

## Code Style & Philosophy - IMPORTANT!
**Follow the minimal, Danish-friendly approach established in the codebase:**

### **Mathematical Notation - European Style**
- **ALWAYS use European notation**: `y = a + b*x` where `a` = intercept, `b` = slope
- **NEVER use American textbook notation**: `theta0`, `theta1` - this confuses Danish students
- **Variable naming**: `beste_a`, `beste_b`, `parametre`, `kostfunktion`

### **Code Simplicity - Teacher's Style**
- **Keep exercises minimal**: 15-40 lines maximum per file
- **Focus on core functionality**: No verbose docstrings or academic explanations
- **Remove unnecessary complexity**: No try/except blocks unless truly needed
- **Match teacher examples**: Follow the simple, direct style from exercise_examples/

### **Danish Language Integration**
- **Comments in Danish**: `# Generer data`, `# Find bedste parametre`, `# Vis resultat`
- **Variable names in Danish**: `datapunkter`, `kostfunktion`, `støj`, `læringsrate`
- **Print messages in Danish**: `"Bedste parametre: a = ..."`, `"Fundne resultater"`
- **Plot labels in Danish**: `"Datapunkter"`, `"Tilpasset linje"`

### **Implementation Patterns**
- **Linear Regression**: Data generation → Algorithm → Single plot with results
- **Synthetic data pattern**: `X = 2 * np.random.rand(100, 1); y = 4 + 3 * X + np.random.randn(100, 1)`
- **Normal equation**: `params = np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)`
- **European parameter extraction**: `a = params[0, 0]; b = params[1, 0]`
- **Single matplotlib.pyplot.show()**: One plot per exercise, no multiple sequential plots

## Code Architecture & Patterns
- **Exercise Progression**: Build incrementally, each exercise teaches one core concept
- **Mathematical Focus**: Implement algorithms from scratch using NumPy, avoid sklearn unless needed
- **Minimal Documentation**: Brief Danish comments explaining what code does, not theory
- **Visual Results**: Every exercise should show a plot demonstrating the concept
- **Practical Learning**: Focus on doing and understanding through implementation

## Course Goals
- Complete all exercises with minimal, clean code
- Understand ML concepts through hands-on implementation  
- Use familiar European mathematical notation
- Build practical programming skills in Danish-friendly environment
- Focus on core algorithms rather than high-level library usage