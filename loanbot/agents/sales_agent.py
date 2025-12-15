class SalesAgent:
    def engage(self, user, offer):
        return {
            "message": f"""
Hi {user['name']} 👋
You’re eligible for a Tata Capital Personal Loan up to ₹{offer['pre_approved_limit']} 
at an attractive interest rate of {offer['interest_rate']}%.

This loan can be used for travel, medical needs, or lifestyle upgrades.
Shall I help you proceed?
"""
        }
