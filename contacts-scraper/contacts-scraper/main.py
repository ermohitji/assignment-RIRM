from print_output import print_output
from read_input import read_input_url
from scraper import get_links

if __name__ == '__main__':
    input_url = read_input_url(standalone_mode=False)
    results = get_links('https://ful.io')
    print_output(results)
