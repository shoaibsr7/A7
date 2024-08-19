"""
Generates performance reports for your stock portfolio.
"""
import argparse
import csv
import yfinance as yf

def main():
    """
    Entrypoint into program.
    """
    args = get_args()
    portfolio_data = read_portfolio(args.source)
    # print("Portfolio Data:", portfolio_data)  # Debugging line
    market_data = get_market_data([row['symbol'] for row in portfolio_data])
    # print("Market Data:", market_data)  # Debugging line
    output_data = calculate_metrics(portfolio_data, market_data)
    save_portfolio(output_data, args.target)

def read_portfolio(filename):
    """
    Returns data from a CSV file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def get_args(args=None):
    """
    Parse and return command line argument values
    """
    parser = argparse.ArgumentParser(description='Generate stock portfolio performance report.')
    parser.add_argument('--source', required=True, help='Path to input portfolio CSV file')
    parser.add_argument('--target', required=True, help='Path to output report CSV file')
    return parser.parse_args(args)

def get_market_data(stocks_list):
    """
    Get the latest market data for the given stock symbols using yfinance
    """
    market_data = {}
    for symbol in stocks_list:
        ticker = yf.Ticker(symbol)
        stock_info = ticker.history(period="1d")
        if not stock_info.empty:
            latest_price = stock_info['Close'].iloc[-1]
            market_data[symbol] = latest_price
        else:
            print(f"Warning: No data found for {symbol}")
    return market_data

def calculate_metrics(portfolio_data, market_data):
    """
    Calculates the various metrics of each of the stocks
    """
    output_data = []
    for row in portfolio_data:
        symbol = row['symbol']
        units = int(row['units'])
        cost = float(row['cost'])
        if symbol in market_data:
            latest_price = market_data[symbol]
            book_value = units * cost
            market_value = units * latest_price
            gain_loss = market_value - book_value
            change = (gain_loss / book_value) * 100
            output_data.append({
                'symbol': symbol,
                'units': units,
                'cost': cost,
                'latest_price': latest_price,
                'book_value': book_value,
                'market_value': market_value,
                'gain_loss': gain_loss,
                'change': change
            })
        else:
            print(f"Warning: No market data found for {symbol}")
    return output_data

def save_portfolio(output_data, filename):
    """
    Saves data to a CSV file
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = [
            'symbol', 'units', 'cost', 'latest_price',
            'book_value', 'market_value', 'gain_loss', 'change'
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)

if __name__ == '__main__':
    main()
