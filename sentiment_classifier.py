from src.ticket import TicketAPI
from pysentimiento import create_analyzer
import logging
logging.getLogger().setLevel(logging.INFO)


class SentimentClassifier:

    def __init__(self):
        self.positive_sentiment = "POS"
        self.negative_sentiment = "NEG"

    def classify_tickets_and_update_status(self, ticket_api: TicketAPI):
        analyzer = create_analyzer(task="sentiment", lang="en")

        tickets = ticket_api.list_tickets()

        for ticket in tickets:
            ticket_id = ticket["id"]
            ticket_body = ticket_api.get_articles_by_ticket_id(ticket_id)[0]["body"]
            sentiment = analyzer.predict(ticket_body).output

            if sentiment == self.positive_sentiment:
                priority_id = 1
            elif sentiment == self.negative_sentiment:
                priority_id = 2
            else:
                priority_id = 3

            ticket_api.update_ticket(ticket_id, priority_id)

        logging.info("Successfully reprioritized and updated all tickets")
