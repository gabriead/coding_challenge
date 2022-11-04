import unittest

from src.sentiment_classifier import SentimentClassifier
from src.ticket import TicketAPI
from src.ticket_utils import delete_all_tickets
from src.app_config import setup


class SentimentClassifierTest(unittest.TestCase):


    def test_classification_updates_priority_correctly(self):
        setup()
        sentiment_classifier = SentimentClassifier()
        ticket_api = TicketAPI()

        delete_all_tickets(ticket_api)
        ticket_api.create_ticket_with_article("test_title", "test_subject", "negative sentiment")
        ticket_before_update = ticket_api.list_tickets()[0]
        curr_ticket_id = ticket_before_update["id"]
        ticket_api.update_ticket(curr_ticket_id, 1)
        ticket_before_update = ticket_api.list_tickets()[0]
        priority_before_sentiment_classification = ticket_before_update["priority_id"]

        self.assertEqual(priority_before_sentiment_classification, 1)

        sentiment_classifier.classify_tickets_and_update_status(ticket_api)

        ticket_after_update = ticket_api.list_tickets()[0]
        priority_after_sentiment_classification = ticket_after_update["priority_id"]

        self.assertEqual(priority_after_sentiment_classification, 2)


if __name__ == '__main__':
    unittest.main()
