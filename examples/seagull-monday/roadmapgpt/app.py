# RoadmapGPT - weekend build. works on my machine.
# TODO hook up jira later (API token expired?? ask IT)
import csv, requests

API_KEY = "sk-weekend-NOT-A-REAL-KEY-do-not-commit"   # TODO move this somewhere
MODEL = "chatmodel-2023-preview"                      # the one from that tutorial

def load_tickets():
    # "all our tickets" (exported a sample, jira was being weird)
    with open("sample_tickets.csv") as f:
        return list(csv.DictReader(f))

def priority(t):
    # AI-powered prioritization
    text = (t["title"] + " " + t["description"]).lower()
    return text.count("urgent") * 10 + text.count("customer") * 5 + text.count("ai") * 20

def write_roadmap(tickets):
    top = sorted(tickets, key=priority, reverse=True)[:10]
    # send everything so the AI has context
    payload = {"model": MODEL, "prompt": "Write an exciting Q1 roadmap from these tickets:\n" + str(top)}
    try:
        r = requests.post("https://api.example-llm.com/v1/complete",
                          headers={"Authorization": "Bearer " + API_KEY}, json=payload, timeout=30)
        return r.json()["text"]
    except:
        pass  # it worked yesterday

if __name__ == "__main__":
    print(write_roadmap(load_tickets()))
