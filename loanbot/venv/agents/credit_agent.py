class CreditAgent:
    def check_score(self, customer):
        score = customer.get("credit_score", 0)

        if score >= 750:
            risk = "low"
        elif score >= 650:
            risk = "medium"
        else:
            risk = "high"

        return {
            "credit_score": score,
            "risk_level": risk
        }
