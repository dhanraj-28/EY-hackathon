import json
import os
from agents.master_agent import MasterAgent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input file
input_path = os.path.join(BASE_DIR, "data", "users.json")

# Output file
output_path = os.path.join(BASE_DIR, "data", "loan_decision_result.json")

with open(input_path, "r") as f:
    customer = json.load(f)

master = MasterAgent()
result = master.process_loan(customer)

# Print to console
print("Loan Decision Result:")
print(result)

# ✅ Save result to file
with open(output_path, "w") as f:
    json.dump(result, f, indent=4)

print(f"\n✅ Result saved to: {output_path}")
