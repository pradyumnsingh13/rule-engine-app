from rule_engine import create_rule, evaluate_rule

def main():
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    
    # Create the AST from the rule string
    ast1 = create_rule(rule1)
    
    # Test data
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(ast1, data)
    print(f"Eligibility Result: {result}")  # Should print either True or False based on the rule and data

if __name__ == "__main__":
    main()
