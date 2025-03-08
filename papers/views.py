import requests
#from django.shortcuts import render, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Paper

SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_papers(request):
    query = request.GET.get("query", "")
    if not query:
        return render(request, "papers/search.html", {"papers": []})

    response = requests.get(
        SEMANTIC_SCHOLAR_API,
        params={"query": query, "offset": 0, "limit": 5}
    )
    
    data = response.json().get("data", [])

    papers = [
        {
            "paper_id": paper["paperId"],
            "title": paper["title"]
        }
        for paper in data
    ]

    return render(request, "papers/search.html", {"papers": papers, "query": query})

def paper_details(request, paper_id):
    api_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
    params = {"fields": "title,year,authors,abstract,url,openAccessPdf"}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)

    return JsonResponse({"error": "Paper not found"}, status=404)