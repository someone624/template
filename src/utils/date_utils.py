from datetime import datetime, timezone

def get_current_timestamp() -> int:
    """Return the current timestamp in seconds."""
    return int(datetime.now(tz=timezone.utc).timestamp())

def format_date(date: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime object as a string."""
    return date.strftime(format_string)