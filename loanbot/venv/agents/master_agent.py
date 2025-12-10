from agents.kyc_agent import KYCAgent
from agents.credit_agent import CreditAgent
from agents.underwriting_agent import UnderwritingAgent
from agents.sanction_agent import SanctionAgent


class MasterAgent:
    def process_loan(self, customer):
        kyc = KYCAgent().verify(customer)
        if kyc["kyc_status"] != "verified":
            return {"status": "Rejected due to KYC failure"}

        credit = CreditAgent().check_score(customer)
        underwriting = UnderwritingAgent().evaluate(customer, credit)
        sanction = SanctionAgent().sanction(underwriting)

        return {
            "kyc": kyc,
            "credit": credit,
            "underwriting": underwriting,
            "sanction": sanction
        }
