from ticket import TicketAPI
from import_tickets_zammad import TicketCreator
from sentiment_classifier import SentimentClassifier
import logging
logging.getLogger().setLevel(logging.INFO)
from app_config import setup

setup()
ticket_api = TicketAPI()
ticket_creator = TicketCreator(dataset_name_local = "consumer_complaints_ds",
                               dataset_name_huggingface = "milesbutler/consumer_complaints")
sentiment_classifier = SentimentClassifier()

ticket_creator.download_ds()
ticket_creator.delete_all_existing_tickets(ticket_api)
training_samples = ticket_creator.load_training_samples(num_samples=51)
ticket_creator.create_tickets_from_samples(training_samples, ticket_api)
sentiment_classifier.classify_tickets_and_update_status(ticket_api)

logging.info("Successfully created and classified tickets")