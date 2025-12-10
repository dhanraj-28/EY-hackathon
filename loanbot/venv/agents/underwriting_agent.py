class UnderwritingAgent:
    def evaluate(self, customer, credit_info):
        income = customer.get("monthly_income", 0)
        risk = credit_info["risk_level"]

        if income >= 50000 and risk != "high":
            decision = "eligible"
        else:
            decision = "not_eligible"

        return {"underwriting_decision": decision}
