"""Reference idempotent consumer pattern using an in-memory processed-event store."""

processed_events = set()

def handle_event(event: dict) -> str:
    event_id = event["eventId"]
    if event_id in processed_events:
        return "duplicate_ignored"

    # Domain processing would occur here.
    processed_events.add(event_id)
    return "processed"
