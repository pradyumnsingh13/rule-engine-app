# Rule Engine Application

This project implements a simple rule engine using an Abstract Syntax Tree (AST) in Python. The engine determines user eligibility based on various attributes such as age, department, income, and experience. The application allows for dynamic rule creation, combination, and evaluation.

## Features
- **Rule Definition**: Create rules using conditional expressions.
- **Rule Combination**: Combine multiple rules efficiently to form complex eligibility criteria.
- **Evaluation**: Evaluate JSON data against defined rules to determine user eligibility.

## Project Structure
rule_engine_app/ │ 
├── app.py # Main application script to run the rule engine 
├── rule_engine.py # Contains the implementation of the rule engine logic 
├── README.md # Project documentation 
└── .gitignore # Files to be ignored by Git

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- Basic knowledge of Python and command-line interface.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pradyumnsingh13/rule-engine-app.git
**Navigate to the project**
cd rule-engine-app
**Run the application**
python app.py

**Here is an example of how to use the rule engine:**
data = {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}

# You can define rules as strings
rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"

# Create the AST from the rule string
ast = create_rule(rule_string)

# Evaluate the rule against the data
result = evaluate_rule(ast, data)

print(f"Eligibility Result: {result}")  # Outputs: Eligibility Result: True

**Error Handling**
The application includes basic error handling for:

Invalid rule strings or formats.
Unsupported operators in conditions.

**Future Enhancements**
Support for user-defined functions within rules.
Integration with a database for rule storage and management.
User interface for easier rule creation and management.

**License**
This project is licensed under the MIT License.

Author
Pradyumn Pratap Singh



