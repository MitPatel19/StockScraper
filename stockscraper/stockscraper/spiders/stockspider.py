import scrapy


class StockspiderSpider(scrapy.Spider):
    name = "stockspider"
    allowed_domains = ["moneycontrol.com"]
    start_urls = ["https://moneycontrol.com/stocks/marketstats/bse-gainer/all-companies_-1/more/"]

    def parse(self, response):
        # Assuming the data is in a <div> with class "bsr_table hist_tbl_hm"
        table_rows = response.css('div.bsr_table.hist_tbl_hm tbody tr')

        for row in table_rows:
            # Extracting data from each row
            company_name = row.css('td.PR a::text').get()
            high = row.css('td:nth-child(2)::text').get()
            low = row.css('td:nth-child(3)::text').get()
            last_price = row.css('td:nth-child(4)::text').get()
            prev_close = row.css('td:nth-child(5)::text').get()
            change = row.css('td:nth-child(6)::text').get()
            percent_gain = row.css('td:nth-child(7)::text').get()

            # Check if any of the extracted data is None
            if all([company_name, high, low, last_price, prev_close, change, percent_gain]):
                # If all data is present, print the record
                print({
                    'Company Name': company_name,
                    'High': high,
                    'Low': low,
                    'Last Price': last_price,
                    'Prev Close': prev_close,
                    'Change': change,
                    '% Gain': percent_gain
                })
