"""
This is data type S3Parameters
"""
import typing


class Locators(typing.NamedTuple):
    """
    The data type class ⇾ Locators

    Attributes
    ----------
    boards : str<br>
      <a href="https://www.opendata.nhs.scot/dataset/geography-codes-and-labels/resource/652ff726-e676-4a20-abda-435b98dd7bdc" target="_blank">Boards</a>

    institutions : str
      <a href="https://www.opendata.nhs.scot/dataset/hospital-codes/resource/c698f450-eeed-41a0-88f7-c1e40a568acc" target="_blank">Institutions</a>

    data : str
      <a href="https://www.opendata.nhs.scot/dataset/weekly-accident-and-emergency-activity-and-waiting-times" target="_blank">Data</a>
    """

    boards: str
    institutions: str
    data: str