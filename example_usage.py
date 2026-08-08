from client import AiMeetingTranscriptActionItemExtractorClient

def main():
    client = AiMeetingTranscriptActionItemExtractorClient()
    res = client.extract_action_items("Sarah: Let's freeze features by Aug 29... James: I can share capacity plan...", ["Sarah", "James"])
    print(f"Summary: {res['summary']}")
    print("Action Items:")
    for item in res["action_items"]:
        print(f"  [{item['owner']}] {item['task']} (Due: {item['due']})")

if __name__ == "__main__":
    main()
