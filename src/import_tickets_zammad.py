import pandas as pd
from datasets import load_dataset_builder, Dataset
from datasets import load_dataset, load_from_disk
from src.ticket import TicketAPI
import os
import logging
logging.getLogger().setLevel(logging.INFO)


class TicketCreator:

    def __init__(self, dataset_name_local, dataset_name_huggingface):
        self.dataset_name_local = dataset_name_local
        self.dataset_name_huggingface = dataset_name_huggingface

    def download_ds(self, path="src/consumer_complaints_ds"):

        if not os.path.isdir(path):
            logging.info("Downloading dataset")
            ds_name = self.dataset_name_huggingface
            ds_builder = load_dataset_builder(ds_name)
            print(ds_builder.info.description)

            dataset = load_dataset(ds_name, split="train")
            dataset.save_to_disk(self.dataset_name_local)
            logging.info("Downloading dataset completed")
        else:
            logging.info("Dataset is already locally available")

    def delete_all_existing_tickets(self, ticket_api:TicketAPI):
        tickets = ticket_api.list_tickets()

        for ticket in tickets:
            ticket_api.delete_ticket(ticket["id"])

        assert len(ticket_api.list_tickets()) == 0

    def load_training_samples(self, num_samples: int) -> pd.DataFrame:
        dataset_hub = load_from_disk("./src/consumer_complaints_ds")
        df = dataset_hub.to_pandas()
        df_training_samples = df.iloc[:num_samples, :]
        return df_training_samples

    def all_tickets_created(self, samples: pd.DataFrame, ticket_api: TicketAPI):
        df_length = samples.shape[0]
        num_tickets = len(ticket_api.list_tickets())
        assert num_tickets == df_length

    def create_tickets_from_samples(self, samples: pd.DataFrame, ticket_api: TicketAPI):

        for idx, row in samples.iterrows():
            article_body = row["Consumer Complaint"]
            ticket_title = "Complaint " + str(idx)
            article_subject = row["Issue"]+ " " + str(idx)
            response, _, status_code = ticket_api.create_ticket_with_article(ticket_title, article_subject, article_body)

            if not status_code == 201:
                print(response)
                raise Exception("Error creating ticket")
