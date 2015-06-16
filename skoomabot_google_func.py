"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/druggiebot

Helper functions for Google Sheets. Used within druggiebot.
Note: Needs an access token in order to authenticate.
Authentication process requires the functions in druggiebot_google.
"""
import druggiebot_google as dbg

# Autenticate with Google for Google Sheets.
sheet_id = '1_iRNUZc5CwAQmUg11bgzIrLrmzGkS1d-N3Nz68--gYg'
sheet_name = 'druggiebot'
creds_google = dbg.authenticate_google_docs()


class Worksheet:
    """Container and parser for Google Sheet."""
    def __init__(self, sheet_id):
        self.sheet = creds_google.open_by_key(sheet_id)

    def _worksheet(self):
        """Get the worksheets available inside sheed_id."""
        self.ws_list = self.sheet.worksheets()
        self.ws_slang = self.sheet.worksheet('slang')
        self.ws_setting = self.sheet.worksheet('setting')
        self.ws_test = self.sheet.worksheet('TEST')

    def _records_list(self, worksheet):
        """Returns a list of lists of the records found inside
        the worksheet. Provides the amount of records in the worksheet."""
        lists_of_records = worksheet.get_all_values()
        return(lists_of_records)

    def _get_amount(self, worksheet):
        """Returns the amount of rows found within a given worksheet.
        Used as a way to find the next available empty row."""
        amount = 0
        for record in worksheet.get_all_values():
            amount += 1
        return amount

    def _insert_record(self, worksheet, payload):
        """Take a record as a list and inserts data to the next empty row.
        Uses cell coordinates."""
        row = self._get_record(worksheet)
        column = len(payload)
        # WIP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        for field in payload:
            for col in range(1,column):
                worksheet.update_cell(row, column, field)

        # Google Sheets - Date: COL A | ID: COL B | Title: COL C
        # post_data = {id_num: self.id_num, date: self.date, title: self.title, text: self.text}
        # ws_test.update_cell(1, 2, post_data)
        # ws_test.update_cell(1, 2, 'Test')
        # ws_test.update_cell(2, 2, 'Test')
        # ws_test.update_cell(4, 2, 'Test')
        # ws_test.update_acell('N1', 'Test')
        # print records
