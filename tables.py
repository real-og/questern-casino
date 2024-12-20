import gspread
import os


SHEET_LINK = str(os.environ.get('SHEET_LINK'))


class WorkSheet:
    def __init__(self, link: str):
        self.link = link
        self.account = gspread.service_account(filename='key.json')
        self.sheet = self.account.open_by_url(self.link).sheet1

    def update_range(self, range, data):
        self.sheet.update(range, data)

    def get_data(self):
        return self.sheet.get_all_values()
        



sheet = WorkSheet(SHEET_LINK)


