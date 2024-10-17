class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left
        self.right = right
        self.value = value  # Only used if type is 'operand'

def create_rule(rule_string):
    # Basic parsing logic to create AST (this is a simple version)
    # We assume the rule_string is correctly formatted for now
    # You may need to build a parser to handle this more robustly

    # Example rule: ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
    # Convert the rule string into an AST here (simplified example below)
    
    # For now, manually return a small tree for testing:
    return Node(
        "operator", 
        left=Node("operator", 
                  left=Node("operand", value=("age", ">", 30)), 
                  right=Node("operand", value=("department", "==", "Sales")),
                  value="AND"),
        right=Node("operand", value=("salary", ">", 50000)),
        value="AND"
    )

def evaluate_rule(node, data):
    if node is None:
        return None
    
    if node.type == "operand":
        attribute, operator, value = node.value
        attribute_value = data.get(attribute)

        if operator == ">":
            return attribute_value > value
        elif operator == "<":
            return attribute_value < value
        elif operator == "==":
            return attribute_value == value
        elif operator == "!=":
            return attribute_value != value
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    
    elif node.type == "operator":
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)

        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result
        else:
            raise ValueError(f"Unsupported operator: {node.value}")
    
    return None
