class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """Keep track of times a paper has been cited
        Lower bound is fixed at 0,upper bound is anything greater or equal to the number of papers"""
        citation_count = [0 for _ in range(len(citations) + 1)]

        # Iterate through citations
        for paper in citations:
            if paper >= len(citations):
                citation_count[-1] += 1
            else:
                citation_count[paper] += 1
        
        """Iterate backwards with the max possible h index to check if 
        at least that many papers have been cited.
        """
        papers = 0
        for h_index in range(len(citation_count) - 1, -1, -1):
            papers += citation_count[h_index]
            if papers >= h_index:
                return h_index

