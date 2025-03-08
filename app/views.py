from django.shortcuts import render
import requests

def home(request):
    query = request.GET.get('query', '').strip()  # Get user input
    papers = []

    print(f"\n🔍 Received Query: '{query}'")  # Debugging

    if query:
        api_url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {"query": query, "fields": "title,venue,s2FieldsOfStudy,paperId"}

        print(f"📡 Sending API Request: {params}")  # Debugging API query

        try:
            response = requests.get(api_url, params=params)
            print(f"🔄 API Status Code: {response.status_code}")

            if response.status_code == 200:
                response_data = response.json()
                papers = response_data.get('data', [])
                print(f"✅ Papers Found: {len(papers)}")  # Debugging

            else:
                print(f"❌ API Error: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"🚨 Request Error: {e}")

    return render(request, "home.html", {"papers": papers, "query": query})