from src.ticket import TicketAPI

def delete_all_tickets(ticket_api: TicketAPI):
    tickets = ticket_api.list_tickets()

    for ticket in tickets:
        ticket_api.delete_ticket(ticket["id"])

    assert len(ticket_api.list_tickets()) == 0