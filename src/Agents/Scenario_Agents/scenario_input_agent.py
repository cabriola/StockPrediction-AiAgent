
import re
from pydantic import BaseModel, Field
from textwrap import dedent
import crewai as crewai
from datetime import datetime
import os
from src.Agents.base_agent import BaseAgent
from src.Agents.Analysis.Tools.search_tools import SearchTools


class ScenarioInputAgent(BaseAgent):
    def __init__(self, **kwargs):
        super().__init__(
            role='Scenario Input Agent',
            goal='Find and interpret market scenarios',
            backstory='Find and interpret market scenarios',
            tools=[SearchTools.search_news],
            **kwargs)

    def get_scenarios_from_news(self):
        if os.name == 'nt':  # For Windows
            formatted_date = datetime.now().strftime('%b %#d, %Y')  # Example: 'Jan 1, 2024'
        else:  # For Unix/Linux/Mac
            formatted_date = datetime.now().strftime('%b %-d, %Y')  

        return crewai.Task(
            description=dedent(f"""
                Collect and summarize recent news articles, press
                releases, and market analyses related to events that
                could affect tickers in the portfolio.
                               
                Pay special attention to any inflation, interest rate,
                and large movements in the stock market.
                                                         
               Make sure to use the most recent data as possible. Do not consider news older than 1 week from {formatted_date}.

               "If you do your BEST WORK, I'll give you a $10,000 commission!"
          
          
            """),
            agent=self,
            expected_output="A comprehensive report summarizing the latest news, market sentiments, and potential best case and worst case impacts on the stock market."
        )

