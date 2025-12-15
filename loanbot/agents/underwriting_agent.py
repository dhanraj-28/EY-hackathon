class UnderwritingAgent:
    def evaluate(self, user, offer, credit_score, salary_slip_uploaded=False):

        pre_limit = offer["pre_approved_limit"]
        requested = user["loan_requested"]
        salary = user["monthly_salary"]
        existing_emi = user["existing_loan_emi"]

        # RULE 1: Credit Score
        if credit_score < 700:
            return {"decision": "reject", "reason": "Low credit score"}

        # RULE 2: Instant Approval
        if requested <= pre_limit:
            return {"decision": "approve", "mode": "instant"}

        # RULE 3: Salary Slip Required
        if requested <= 2 * pre_limit:
            if not salary_slip_uploaded:
                return {"decision": "need_salary_slip"}

            expected_emi = requested / user["tenure_months"]
            if (existing_emi + expected_emi) <= 0.5 * salary:
                return {"decision": "approve", "mode": "post_salary_check"}
            else:
                return {"decision": "reject", "reason": "EMI exceeds 50% salary"}

        # RULE 4: Hard Reject
        return {"decision": "reject", "reason": "Requested amount too high"}
