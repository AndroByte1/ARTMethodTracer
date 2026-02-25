# ARTMethodTracer

Trace. Inspect. Analyze.

ARTMethodTracer is a dynamic Android Runtime (ART) analysis tool that enables runtime method tracing and return value inspection for Android applications.

It is designed for security research, reverse engineering, and runtime behavior analysis.

---

## Features

- Enumerate loaded classes
- List methods of selected classes
- Hook specific methods
- Capture arguments
- Capture return values
- Real-time execution tracing

---

## Requirements

Python 3.8+

### Required Python Packages

```bash
pip install PyQt5 frida
```

---

## Required Imports

The tool relies on the following Python modules:

```python
import sys
import frida
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
```

---

## Usage

```bash
python main.py
```

(Replace `main.py` with your script filename.)

---

## Use Cases

- Android reverse engineering  
- Runtime behavior inspection  
- Security testing  
- Malware research  
- Bug bounty analysis  

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.
