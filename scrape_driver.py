"""
Driver function for the CitationScraper class

Takes newline-delimited text file of citations to search, and outputs a sorted
set of unique citations into output.txt. Any failures are logged in output_failures.txt.

N.B. Google Scholar won't be happy about being scraped. Repeated use of this script
may lead to you being temporarily locked out.
"""

from scraper import CitationScraper

if __name__ == "__main__":

	to_process = "to_process.txt"
	output = "output.txt"
	output_failures = "output_failures.txt"

	all_citations = list()
	failures = list()

	with open(to_process, "r") as fo:
		for line in fo:
			query = line.strip()

			if len(query): # ignore empty lines
				scraper = CitationScraper(query)

				try:
					response = scraper.get_citation()
					all_citations.append(response.encode('utf-8')) #response is Unicode, not str

				# handle case where paper isn't found, timeout, etc.
				except:
					failures.append(query)

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
