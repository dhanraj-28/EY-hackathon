class SanctionAgent:
    def generate(self, user, offer):
        return {
            "sanction_letter": f"""
--- TATA CAPITAL SANCTION LETTER ---

Name: {user['name']}
Loan Amount: ₹{user['loan_requested']}
Tenure: {user['tenure_months']} months
Interest Rate: {offer['interest_rate']}%

Congratulations! Your loan is approved.
"""
        }
