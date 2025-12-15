import json
from agents.master_agent import MasterAgent

user = json.load(open("data/users.json"))
crm = json.load(open("data/crm_data.json"))
offers = json.load(open("data/offers.json"))

agent = MasterAgent()
result = agent.process(user, crm, offers)

print(json.dumps(result, indent=4))
