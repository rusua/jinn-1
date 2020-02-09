"""
protocol and performative constants
"""

NEGOTIATE_PROTOCOL = "NEGOTIATE"
BID_PROTOCOL = "BID" # Si usamos un manager
#REGISTER_PROTOCOL = "REGISTER"
#CREATE_PROTOCOL = "CREATE"
#REQUEST_PROTOCOL = "REQUEST"
#QUERY_PROTOCOL = "QUERY"
#TRAVEL_PROTOCOL = "INFORM"

BID_ACCEPT_PERFORMATIVE = "ACCEPT"
BID_REFUSE_PERFORMATIVE = "REFUSE"
BID_OFFER_PERFORMATIVE = "OFFER"
NEGOTIATION_ACK_PERFORMATIVE = "ACK"
NEGOTIATION_END_PERFORMATIVE = "END"

# Simplified
JINN_READY = "JINN_READY"
JINN_WAITING = "JINN_WAITING"
JINN_DONE = "JINN_DONE"

# Advanced
JINN_READY_TO_NEGOTIATE = "JINN_READY_TO_NEGOTIATE"
JINN_WAITING_OFFER_RESPONSE = "JINN_WAITING_OFFER_RESPONSE"
JINN_WAITING_ACCEPTANCE_RESPONSE = "JINN_WAITING_ACCEPTANCE_RESPONSE"
JINN_ACCEPTED_OFFER = "JINN_ACCEPTED_OFFER"
JINN_FINISHED_NEGOTIATION = "JINN_FINISHED_NEGOTIATION"

