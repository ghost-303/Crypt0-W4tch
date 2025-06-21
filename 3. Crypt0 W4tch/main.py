import argparse
import btc_data
import eth_data
import xrp_data
import doge_data
import pengu_data
import headings

headings.cli_ascii_heading("Crypt0 W4tch")



def main():
    parser = argparse.ArgumentParser(description="Crypt0 W4tch")
    parser.add_argument("--btc",action="store_true", help="Bitcoin Data")
    parser.add_argument("--eth",action="store_true", help="Etherium Data")
    parser.add_argument("--xrp",action="store_true", help="XRP Data")
    parser.add_argument("--doge",action="store_true", help="DOGE COIN Data")
    parser.add_argument("--pengu", action="store_true", help="PUDGY PENGUIN COIN Data")
    args = parser.parse_args()

    # bitcoin
    if args.btc:
        btc_data.btc_info()

    # ethereum
    if args.eth:
        eth_data.eth_info()

    # xrp
    if args.xrp:
        xrp_data.xrp_info()

    # doge coin
    if args.doge:
        doge_data.doge_info()

    # pengu
    if args.pengu:
        pengu_data.pengu_info()

if __name__=="__main__":
    main()
