import unittest
import time_series_visualizer as tsv
import matplotlib.pyplot as plt
import pandas as pd

class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        # Prepare cleaned data for testing
        self.df = tsv.load_and_clean_data()

    def test_clean_data(self):
        lower_bound = self.df["value"].quantile(0.025)
        upper_bound = self.df["value"].quantile(0.975)
        self.assertTrue((self.df["value"] >= lower_bound).all() and (self.df["value"] <= upper_bound).all())

    def test_draw_line_plot(self):
        fig = tsv.draw_line_plot()
        self.assertIsInstance(fig, plt.Axes)

    def test_draw_bar_plot(self):
        ax = tsv.draw_bar_plot()
        self.assertIsInstance(ax, plt.Axes)

    def test_draw_box_plot(self):
        fig = tsv.draw_box_plot()
        self.assertIsInstance(fig, plt.Figure)

if __name__ == "__main__":
    unittest.main()
