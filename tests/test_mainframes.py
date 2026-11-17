from nbresult import ChallengeResultTestCase


class TestMainframes(ChallengeResultTestCase):
    def test_main_df_shape(self):
        self.assertEqual(
            self.result.main_shape[0],
            6,
            "DataFrame should have 6 rows")
        self.assertGreaterEqual(
            self.result.main_shape[1],
            6,
            "DataFrame should have at least 6 columns")

    def test_main_df_required_columns(self):
        required_columns = ['A', 'B', 'C', 'D', 'E', 'F']
        self.assertTrue(
            all(col in self.result.main_columns for col in required_columns),
            f"DataFrame must contain required columns: {required_columns}. Extra columns are fine!"
        )

    def test_main_df_not_empty(self):
        self.assertGreater(
            self.result.main_shape[0], 0,
            "DataFrame is empty. Did you accidentally filter out all rows?"
        )

    def test_main_df_f_column(self):
        self.assertEqual(self.result.main_f, [12, 12, 12, 12, 12, 12])
