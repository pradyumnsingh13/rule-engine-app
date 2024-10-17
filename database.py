import sqlite3

def init_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_string TEXT,
        rule_ast TEXT -- You can store the serialized version of the AST
    )
    ''')
    conn.commit()
    conn.close()

def save_rule(rule_string, ast):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO rules (rule_string, rule_ast)
    VALUES (?, ?)
    ''', (rule_string, str(ast)))  # Convert AST to string for simplicity

    conn.commit()
    conn.close()
