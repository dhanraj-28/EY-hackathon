class VerificationAgent:
    def verify(self, user_id, crm_data):
        kyc = crm_data.get(user_id)
        if kyc and kyc["phone_verified"] and kyc["address_verified"]:
            return {"status": "verified"}
        return {"status": "failed"}
