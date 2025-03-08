import datetime


def get_datetime_utc_now() -> str:
	return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
