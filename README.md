# citationscraper
Short script to pull well-formatted citations from Google scholar

Works with all the citation formats available on Scholar:
- MLA
- APA
- Chicago
- Harvard
- Vancouver

In order to run, you will need to install selenium and chromedriver. If on OSX, you can just run `brew install chromedriver` for the latter.

to_process.txt is an example input file. Any citation found will be printed, in sorted order and sans duplicates, into output.txt. Any queries that are unsuccessful will be printed to output_failures.txt.
