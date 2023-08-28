import pandas as pd
import os


class PandaTools:
    @staticmethod
    def open_df_in_libre_office(df: pd.DataFrame, path: str = 'assets/_temp', filetype: str = 'ods') -> None:
        """
        Open a pandas DataFrame in LibreOffice Calc
        :param df: the input dataframe
        :param path: the path to save the file to (without file extension)
        :param filetype: either 'csv' or 'ods'
        """

        if filetype == 'csv':
            path += '.csv'
            df.to_csv(path, index=False)
        elif filetype == 'ods':
            path += '.ods'
            df.to_excel(path, index=False)
        else:
            raise Exception(f'Unsupported file type {filetype}')

        # Open file in LibreOffice Calc
        os.system(f'soffice --calc {path} &')
