# code before changes:
#
# from enum import Enum
#
#
# class CSVExportStatus(Enum):
#     PENDING = 1
#     PROCESSING = 2
#     SUCCESS = 3
#     FAILURE = 4
#
#
# def get_csv_status(status, data):
#     pass
#
# actual code:

from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match (status):
        case CSVExportStatus.PENDING:
            pending_data = list(map(lambda x: list(map(lambda y: str(y), x)), data))
            return ("Pending...", pending_data)

        case CSVExportStatus.PROCESSING:
            processed_data = "\n".join(list(map(lambda lst: ",".join(lst), data)))
            return ("Processing...", processed_data)

        case CSVExportStatus.SUCCESS:
            return ("Success!", data)

        case CSVExportStatus.FAILURE:
            pending_data = list(map(lambda x: list(map(lambda y: str(y), x)), data))
            processed_data = "\n".join(list(map(lambda lst: ",".join(lst), pending_data)))

            return ("Unknown error, retrying...", processed_data)
        case _:
            raise Exception("unknown export status")






