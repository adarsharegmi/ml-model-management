import sys

from Source.domain.domain_handler import add_file
from Source.domain import model
from Source.adapters.repository import FileUploadRepository


def main():
    print("Hello jersey")


if __name__ == "__main__":
    # getting args from js file
    # name = sys.argv[1]
    # parameters = sys.argv[2]
    # placement_name = sys.argv[3]
    # effective_from = sys.argv[4]
    # effective_to = sys.argv[5]
    # upload_file = sys.argv[6]
    # active = sys.argv[7]
    model = add_file(
        {
            "name": "sadish",
            "source": "source",
            "parameters": "parameters",
            "placement_name": "placement_nam/e",
            "effective_from": "2021-8-8",
            "effective_to": "2025-8-8",
            "upload_file": "upload_file",
            "active": "True",
        }
    )

    # FileUploadRepository()._add(model)(
    print(FileUploadRepository().get_all())
