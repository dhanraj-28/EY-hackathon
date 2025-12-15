from agents.sales_agent import SalesAgent
from agents.verification_agent import VerificationAgent
from agents.underwriting_agent import UnderwritingAgent
from agents.sanction_agent import SanctionAgent
import random

def purify_leads(users, credit_scores, offers):
    eligible = []

    for user in users:
        score = credit_scores[user["user_id"]]
        offer = offers[user["user_id"]]

        emi_ratio = user["existing_loan_emi"] / user["monthly_salary"]

        if (
            score >= 700 and
            emi_ratio <= 0.5 and
            user["loan_requested"] <= offer["pre_approved_limit"]
        ):
            eligible.append({
                "user": user,
                "score": score
            })

    # Sort by credit score (descending)
    eligible.sort(key=lambda x: x["score"], reverse=True)

    # Pick top 3
    return eligible[:3]


class MasterAgent:
    def process(self, users, crm_data, offers):

        sales = SalesAgent()
        verify = VerificationAgent()
        underwrite = UnderwritingAgent()
        sanction = SanctionAgent()

        # Mock credit scores for all users
        credit_scores = {
            user["user_id"]: random.randint(650, 850)
            for user in users
        }

        # 🔥 LEAD PURIFICATION STEP
        shortlisted = purify_leads(users, credit_scores, offers)

        results = []

        for item in shortlisted:
            user = item["user"]
            score = item["score"]

            print(sales.engage(user, offers[user["user_id"]])["message"])

            if verify.verify(user["user_id"], crm_data)["status"] != "verified":
                continue

            underwriting_result = underwrite.evaluate(
                user,
                offers[user["user_id"]],
                score,
                salary_slip_uploaded=True
            )

            if underwriting_result["decision"] == "approve":
                sanction_letter = sanction.generate(user, offers[user["user_id"]])
                results.append({
                    "user_id": user["user_id"],
                    "name": user["name"],
                    "credit_score": score,
                    "sanction": sanction_letter
                })

        return {
            "total_leads": len(users),
            "shortlisted": len(shortlisted),
            "sanctioned": len(results),
            "sanctioned_users": results
        }
