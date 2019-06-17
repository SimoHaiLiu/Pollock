from src.database import Database

class Portfolio:

    portfolio = []

    @staticmethod
    def insert_in_portfolio(invoice):
        Portfolio.portfolio.append(invoice)

    @staticmethod
    def delete_from_portfolio(invoice):
        Portfolio.portfolio.remove(invoice)

    def to_csv_file(self):
        pass

    def draw_chart(self):
        pass

