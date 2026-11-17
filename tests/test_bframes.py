from nbresult import ChallengeResultTestCase
import pandas as pd


class TestBframes(ChallengeResultTestCase):
    def test_df_B_shape(self):
        self.assertEqual(
            self.result.df_B_shape[0],
            6,
            "DataFrame should have 6 rows")
        self.assertGreaterEqual(
            self.result.df_B_shape[1],
            1,
            "DataFrame should have at least 1 column")

    def test_df_B_required_columns(self):
        required_columns = ['B']
        self.assertTrue(
            all(col in self.result.df_B_columns for col in required_columns),
            f"DataFrame must contain required columns: {required_columns}. Extra columns are fine!"
        )

    def test_df_B_not_empty(self):
        self.assertGreater(
            self.result.df_B_shape[0], 0,
            "DataFrame is empty. Did you accidentally filter out all rows?"
        )

    def test_df_B_type(self):
        self.assertEqual(self.result.df_B_type, type(pd.DataFrame()))
