When I was dealing with Enterprise Entity list and Customer List for KYC(know your customer) team in a financial company, I want to see how many matches between the two list.
Unfortunately, there were plenty of variations among those company names.


To do this:
Firstly, standardization of company name. This step is quite common because there are multiple data sources, and data reside in different systems. This step would include removing punctuation and some highly frequent words in the tail, such as ltd and Inc.


Secondly, get substrings of the company name. Considering the variation of companies and their subsidiaries name, we should use substrings to match. If the name is long enough, like more than five words, we can use all substrings with three consecutive words. Otherwise, we can use all consecutive two words. Another consideration is the TF(term frequency), the part would have too many matches. For example, this substring, "investment management", matches too many names.


Thirdly, match substrings to lists. When doing this step, I can see which words contain this substring.
