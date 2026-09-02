from src.event_consumer import handle_event

def test_consumer_is_idempotent():
    event = {"eventId": "E1", "eventType": "claim.status-updated"}
    assert handle_event(event) == "processed"
    assert handle_event(event) == "duplicate_ignored"
