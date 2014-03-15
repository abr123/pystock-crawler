# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ReportItem(Item):
    # Trading symbol
    symbol = Field()

    # If this doc is an amendment to previously filed doc
    amend = Field()

    # Quarterly (10-Q) or annual (10-K) report
    doc_type = Field()

    # Q1, Q2, Q3, or FY for annual report
    period_focus = Field()

    end_date = Field()

    revenues = Field()
    net_income = Field()

    eps_basic = Field()
    eps_diluted = Field()

    dividend = Field()

    assets = Field()
    equity = Field()
    cash = Field()


class PriceItem(Item):
    # Trading symbol
    symbol = Field()

    # YYYY-MM-DD
    date = Field()

    open = Field()
    close = Field()
    high = Field()
    low = Field()
    adj_close = Field()
    volume = Field()