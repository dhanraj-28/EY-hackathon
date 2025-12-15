class CreditAgent:
    def assess_credit(self, user):

        # Feature engineering
        dti_ratio = user["monthly_emi"] / user["monthly_income"]
        loan_to_income = user["loan_amount_requested"] / user["annual_income"]
        savings_to_emi = user["savings_balance"] / user["monthly_emi"]
        payment_reliability = 1 - (user["missed_payments_12m"] / 12)

        # Weighted risk score (proxy for ML)
        score = (
            0.30 * (user["credit_score"] / 900) +
            0.20 * (1 - dti_ratio) +
            0.15 * payment_reliability +
            0.10 * (user["credit_history_years"] / 10) +
            0.10 * (user["employment_years"] / 10) +
            0.10 * (1 - user["credit_utilization"]) +
            0.05 * (savings_to_emi / 10)
        )

        # Probability of Default
        probability_of_default = round(1 - score, 3)

        if probability_of_default < 0.25:
            risk = "low"
        elif probability_of_default < 0.5:
            risk = "medium"
        else:
            risk = "high"

        return {
            "credit_score": user["credit_score"],
            "probability_of_default": probability_of_default,
            "risk_level": risk
        }
