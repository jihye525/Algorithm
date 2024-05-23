from datetime import datetime, timezone, timedelta

kst_time = datetime.now(timezone.utc)+timedelta(hours=9)
print(str(kst_time)[:10])

