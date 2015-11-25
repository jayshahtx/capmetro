import pdb
from api_fns.api import get_bus_data

def main():

    vehicles = get_bus_data()
    print vehicles
       

if __name__ == "__main__":
    main()

