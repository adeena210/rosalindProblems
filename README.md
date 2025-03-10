# Rosalind Bioinformatics Problems

This repository contains my solutions to problems from [Rosalind](http://rosalind.info), a platform for learning bioinformatics through problem-solving.

## About This Project

I'm working through the Rosalind bioinformatics problem set in order to dip my toes into bioinformatics as well as brush up on my Python skills. This repository documents my progress and serves as a reference for common bioinformatics algorithms and techniques.

Each solution includes:
- Link to the original problem
- My solution code (primarily in Python)
- Performance considerations where relevant

## Featured Solutions

### [DNA Base Counting](https://github.com/adeena210/rosalindProblems/blob/main/stronghold/counting_dna.ipynb)

Three different implementations with performance benchmarks:

1. **Naive Approach** - Using a simple for loop with conditionals
2. **Built-in Methods** - Using Python's string count() method
3. **Counter Approach** - Using Python's collections.Counter

### [Reverse Complement](https://github.com/adeena210/rosalindProblems/blob/main/stronghold/reverse_complement_dna.ipynb)

Three different implementations with performance and memory usage benchmarks:

1. **Naive Approach** - Using string slicing and concatenation in a loop
2. **List Comprehension** - Using a list to store complemented bases before joining
3. **Generator Approach** - Using a generator expression with reversed iteration

## Problem Categories

### Bioinformatics Stronghold
The main collection of problems covering core bioinformatics concepts:

- DNA/RNA string operations
- Sequence alignment and comparison
## Directory Structure

```
.
├── stronghold/           # Bioinformatics Stronghold problems
└── data/                 # Example datasets for testing
```

## Learning Journey

This repository represents my ongoing learning in bioinformatics and computational biology. I'm approaching these problems not just as programming exercises but as opportunities to understand the underlying biological concepts and their computational applications.

As I progress, I'll be implementing more advanced solutions with a focus on:
- Algorithmic efficiency
- Clean, well-documented code
- Biological relevance and interpretation
- Application of software engineering best practices


## License

This project is licensed under the MIT License - see the LICENSE file for details.
