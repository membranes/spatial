"""Module specimens.py"""
import logging

import pandas as pd


class Specimens:
    """
    Description
    -----------

    This class builds the expected data structure for ...
    """

    def __init__(self, data: pd.DataFrame, elements: pd.DataFrame) -> None:
        """

        :param data:
        :param elements:
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

        # The viable data instances vis-à-vis viable tags
        self.__data: pd.DataFrame = data.copy().loc[data['category'].isin(values=elements['category'].unique()), :]
        self.__data.info()

    @staticmethod
    def __sentences(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        sentences: pd.DataFrame = blob.copy().drop(columns='tag').groupby(
            by=['sentence_identifier'])['word'].apply(lambda x: ' '.join(x)).to_frame()

        return sentences

    @staticmethod
    def __labels(blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        labels: pd.DataFrame = blob.copy().drop(columns='word').groupby(
            by=['sentence_identifier'])['tag'].apply(lambda x: ','.join(x)).to_frame()

        return labels

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        blob = self.__data[['sentence_identifier', 'word', 'tag']].copy()
        blob.info()

        # Re-build the sentences, and a string of the corresponding labels per sentence word.
        sentences = self.__sentences(blob=blob)
        labels = self.__labels(blob=blob)

        # The frames <sentences> & <labels> each have a _sentence identifiers_ index field.
        frame: pd.DataFrame = sentences.join(labels).drop_duplicates()
        frame.reset_index(inplace=True)
        frame.rename(columns={'word': 'sentence', 'tag': 'tagstr'}, inplace=True)

        return frame
