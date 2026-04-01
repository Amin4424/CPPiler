# CPPiler

A C++ compiler implementation built with Python for educational purposes, developed as a project for the **Data Structures and Algorithms** course at **Iran University of Science and Technology (IUST)**.

## About This Project

This project was created as part of the Data Structures and Algorithms curriculum to demonstrate fundamental compiler design principles and implement key algorithms used in programming language processing. It showcases practical applications of concepts taught in the course, including:

- Tree data structures for parse tree representation
- Stack-based algorithms for parsing
- Hash tables for token management
- Graph algorithms for grammar analysis (FIRST and FOLLOW sets)
- Complexity analysis of compiler algorithms

## What is CPPiler?

CPPiler is an educational C++ parser and compiler that performs lexical analysis, tokenization, and syntax parsing on a restricted subset of C++ code. It demonstrates the complete compilation pipeline from source code to parse tree visualization, making it an excellent learning tool for understanding how compilers work.

### Key Features

- **Lexical Analysis**: Tokenizes C++ source code into meaningful tokens (keywords, identifiers, numbers, symbols, strings)
- **Syntax Validation**: Checks for basic syntax errors like missing semicolons and type mismatches
- **LL(1) Parser**: Implements a non-predictive parser using an LL(1) parse table
- **Parse Tree Visualization**: Generates and displays parse trees showing the syntactic structure of code
- **Interactive CLI**: User-friendly menu interface for exploring different compiler stages
- **Grammar Analysis**: Computes FIRST and FOLLOW sets for context-free grammar

## Supported C++ Subset

CPPiler supports a limited but meaningful subset of C++ syntax:

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    float y = 3.14;
    int sum = x + y * 2;

    while(x != 0) {
        cin >> x;
        cout << "Value: " << x;
    }

    return 0;
}
```

**Supported constructs:**
- `#include` directives
- `using namespace std;`
- `int main()` function
- Variable declarations: `int`, `float`
- Arithmetic operations: `+`, `-`, `*`
- Comparison operators: `==`, `!=`, `>=`, `<=`
- Input: `cin >> variable`
- Output: `cout << value`
- `while` loops
- `return 0;` statement

## How It's Implemented

CPPiler follows a classic compiler architecture with the following components:

### 1. Lexical Analysis (`lexer.py`)
- Uses regex-based pattern matching to break source code into tokens
- Recognizes 6 token types: reserved words, identifiers, numbers, symbols, strings, and whitespace
- **Time Complexity**: O(m × n) where m is input length and n is the number of patterns

### 2. Grammar Definition (`constants.py`)
- Defines a context-free grammar (CFG) with 19 non-terminals
- Contains a pre-computed LL(1) parse table (22 rows × 26 columns)
- Maps grammar symbols to table indices for efficient parsing

### 3. FIRST Set Calculator (`get_first.py`)
- Recursively computes FIRST sets for all non-terminals
- Essential for constructing the LL(1) parser
- **Time Complexity**: O(N × M × L) where N is non-terminals count, M is productions per non-terminal, and L is average production length

### 4. FOLLOW Set Calculator (`get_follow.py`)
- Computes FOLLOW sets for non-terminals
- Handles epsilon (ε) productions correctly
- Uses visited tracking to avoid infinite loops
- **Time Complexity**: O(N × P × L) where N is non-terminals count, P is productions count, and L is average production length

### 5. Tokenization Interface (`tokenize_code.py`)
- Reads C++ source files and tokenizes them
- Performs basic syntax validation
- Displays tokenized output to the user

### 6. Token Classification (`token_table.py`)
- Organizes tokens by type into a formatted table
- Uses SHA256 hashing for token representation
- **Time Complexity**: O(n) where n is the number of tokens

### 7. Parse Table Display (`parse_table.py`)
- Visualizes the LL(1) parse table
- Shows all possible grammar derivations
- **Time Complexity**: O(n) where n is table size

### 8. Parser & Parse Tree Generator (`nonpredective.py`)
- Implements stack-based LL(1) parsing algorithm
- Generates parse trees using the `anytree` library
- Visualizes the syntactic structure of the code
- **Time Complexity**: O(n + t + r × c) where n is input length, t is tokens count, r is rows, and c is columns in parse table

### 9. Interactive Menu (`main.py`)
- Provides a user-friendly CLI using the Rich library
- Allows users to explore different compilation stages
- Options: Tokenize, Token Table, Parse Table, Parse Tree, Exit

## Architecture Overview

```
Source Code (.cpp)
        ↓
    Lexer (lexer.py)
        ↓
    Tokens
        ↓
    Parser (nonpredective.py)
        ↓
    Parse Tree
        ↓
    Visualization
```

## Installation & Usage

### Prerequisites
- Python 3.x
- Required libraries: `rich`, `anytree`

### Install Dependencies
```bash
pip install rich anytree
```

### Running CPPiler
```bash
python main.py
```

### Menu Options
1. **Tokenize**: View all tokens extracted from your C++ code
2. **Token Table**: See tokens organized by type (keywords, identifiers, numbers, etc.)
3. **Parse Table**: Display the LL(1) parse table used for syntax analysis
4. **Parse Tree**: Generate and visualize the parse tree for your code
5. **Exit**: Close the application

## Technologies Used

- **Python 3**: Main implementation language
- **Rich**: Terminal formatting and beautiful console output
- **anytree**: Tree data structure for parse tree representation
- **re**: Regular expressions for lexical analysis
- **hashlib**: SHA256 hashing for token display

## Learning Outcomes

This project demonstrates:
- How compilers process source code from text to structured data
- Implementation of fundamental algorithms from Data Structures and Algorithms course
- Practical application of trees, stacks, and hash tables
- Understanding of formal languages and automata theory
- Complexity analysis and algorithm optimization

## Limitations

- Supports only a restricted subset of C++
- No semantic analysis or code generation
- Limited error recovery mechanisms
- Pre-built parse table (not dynamically generated)

## Future Extensions

Potential improvements for learning:
- Support for more C++ constructs (functions, arrays, classes)
- Dynamic parse table generation from grammar
- Better error messages and recovery
- Semantic analysis phase
- Intermediate code generation
- Optimization techniques

## Academic Context

**Course**: Data Structures and Algorithms
**Institution**: Iran University of Science and Technology (IUST)
**Purpose**: Educational demonstration of compiler concepts and algorithms

## License

This is an educational project developed for academic purposes.

---

**Note**: This compiler is designed for learning purposes and demonstrates fundamental compiler concepts. It is not intended for production use or compiling real-world C++ applications.
