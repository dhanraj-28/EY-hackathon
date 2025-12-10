class SanctionAgent:
    def sanction(self, underwriting_result):
        if underwriting_result["underwriting_decision"] == "eligible":
            return {"loan_status": "approved", "amount": 500000}
        return {"loan_status": "rejected", "amount": 0}
