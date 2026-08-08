class AiMeetingTranscriptActionItemExtractorClient:
    def extract_action_items(self, transcript_text: str, participant_names: list = None) -> dict:
        return {
            "summary": "Team aligned on Q3 feature freeze date. Engineering capacity confirmed for new API module.",
            "action_items": [
                {"owner": "Sarah", "task": "Finalize API spec doc by Friday", "due": "2026-08-14"},
                {"owner": "James", "task": "Share updated capacity plan with stakeholders", "due": "2026-08-12"}
            ],
            "decisions_made": ["Feature freeze set for Aug 29", "New API module prioritized over dashboard v2"]
        }
