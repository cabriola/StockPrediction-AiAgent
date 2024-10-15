import unittest
from unittest.mock import patch, MagicMock
from src.Agents.Analysis.stock_analysis_agents import StockAnalysisAgents
from src.Agents.Analysis.stock_analysis_tasks import StockAnalysisTasks
from src.UI.predict_sectors_main import EconomicCrew

# Mocking the FRED API response for macroeconomic data
mock_macroeconomic_data = {
    "GDP": "Real GDP data",
    "Inflation": "CPI data",
    "UnemploymentRate": "Unemployment rate data"
}

mock_combined_data = {
    "MacroeconomicData": mock_macroeconomic_data,
    "FinancialReports": "Financial Reports Mock Data",
    "PolicyChanges": "Policy Changes Mock Data"
}


class TestEconomicCrew(unittest.TestCase):
    @patch('src.UI.predict_sectors_main.Fred.get_series')
    def test_fetch_macroeconomic_data(self, mock_get_series):
        # Mock FRED API data fetching
        mock_get_series.side_effect = lambda series_id: mock_macroeconomic_data[series_id]
        
        economic_crew = EconomicCrew()
        result = economic_crew.fetch_macroeconomic_data()

        # Check if the result matches the mock data
        self.assertEqual(result['GDP'], "Real GDP data")
        self.assertEqual(result['Inflation'], "CPI data")
        self.assertEqual(result['UnemploymentRate'], "Unemployment rate data")

    def test_get_combined_data(self):
        economic_crew = EconomicCrew()
        result = economic_crew.get_combined_data(mock_macroeconomic_data)

        # Validate that the combined data contains correct financial reports, policy changes, and macroeconomic data
        self.assertEqual(result["MacroeconomicData"], mock_macroeconomic_data)
        self.assertEqual(result["FinancialReports"], "Financial Reports Mock Data")
        self.assertEqual(result["PolicyChanges"], "Policy Changes Mock Data")


if __name__ == '__main__':
    unittest.main()
