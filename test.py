import arxiv

search = arxiv.Search(
  query = "ti:contrastive",
  max_results = 10,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

for result in search.results():
  print(result.title)