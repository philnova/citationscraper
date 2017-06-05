from selenium import webdriver

class CitationScraper(object):

	def __init__(self, paper_name, desired_format = "APA"):
		self._paper_name = paper_name
		self._desired_format = desired_format
		self._driver = webdriver.Chrome()

	def get_citation(self):
		query = self._paper_name.replace(" ", "+")
		url = "https://scholar.google.com/scholar?hl=en&q=" + query

		self._driver.get(url)

		self._driver.find_element_by_link_text("Cite").click() # open modal
		self._driver.find_element_by_id("gs_top").text # switch to modal context
		citation_table = self._driver.find_element_by_id("gs_citt").find_element_by_tag_name("table").find_elements_by_tag_name("tr")

		for citation in citation_table:
			cite_text = citation.text
			cite_split = cite_text.split("\n")
			if cite_split[0] == self._desired_format:
				return cite_split[1]
		raise selenium.common.exceptions.NoSuchElementException

	def __del__(self):
		self._driver.close()


if __name__ == "__main__":
	# example run
	scrap = CitationScraper("Ovarian cycle-linked changes in GABAA receptors mediating tonic inhibition alter seizure susceptibility and anxiety", "APA")
	print scrap.get_citation()
