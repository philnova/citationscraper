"""
Driver function for the CitationScraper class

Takes newline-delimited text file of citations to search, and outputs a sorted
set of unique citations into output.txt. Any failures are logged in output_failures.txt.

N.B. Google Scholar won't be happy about being scraped. Repeated use of this script
may lead to you being temporarily locked out.
"""

from scraper import CitationScraper
import time
import random

MAX_DELAY = 30 # build in a sleep time between queries
# 30 s is pretty long, but longer times stop Google from complaining

if __name__ == "__main__":

	to_process = "to_process.txt"
	output = "output.txt"
	output_failures = "output_failures.txt"

	all_citations = list()
	failures = list()

	with open(to_process, "r") as fo:
		scraper = CitationScraper("")

		for line in fo:
			query = line.strip()

			if len(query): # ignore empty lines
				scraper.set_paper_name(query)

				try:
					response = scraper.get_citation()
					all_citations.append(response.encode('utf-8')) #response is Unicode, not str

				# handle case where paper isn't found, timeout, etc.
				except:
					failures.append(query)

			time.sleep(random.randint(0, MAX_DELAY))

	all_citations = list(set(all_citations)) # fiter out duplicates
	all_citations.sort()

	with open(output, "w") as fo:
		for citation in all_citations:
			fo.write(citation)
			fo.write("\n")
			fo.write("\n")

	with open(output_failures, "w") as fo:
		for failure in failures:
			fo.write(failure)
			fo.write("\n")
			fo.write("\n")
