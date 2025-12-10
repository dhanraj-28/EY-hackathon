class KYCAgent:
    def verify(self, customer):
        if customer.get("aadhaar") and customer.get("pan"):
            return {"kyc_status": "verified"}
        return {"kyc_status": "failed"}
