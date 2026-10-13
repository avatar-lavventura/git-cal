from collections import Counter
from datetime import date, timedelta
from importlib.machinery import SourceFileLoader
from pathlib import Path

gc = SourceFileLoader("gc", str(Path(__file__).with_name("git-cal"))).load_module()

# Fri, Sat(empty), Sun(empty), Mon: weekday streak survives the weekend, full streak does not
fri = date(2026, 10, 9)
days = [fri + timedelta(days=i) for i in range(4)]
s = gc.compute_stats(days, Counter({days[0]: 1, days[3]: 5}))
assert s["total"] == 6 and s["max"] == 1 and s["wmax"] == 2, s
assert s["wmax_range"] == (days[0], days[3]) and s["q"] == (1, 5, 5), s
assert [gc.level(v, s["q"]) for v in (0, 1, 5, 9)] == [0, 1, 2, 4]
assert gc.date_range(3, date(2026, 10, 13)) == (date(2026, 3, 1), date(2026, 4, 1))
assert gc.date_range(12, date(2026, 10, 13)) == (date(2025, 12, 1), date(2026, 1, 1))
assert gc.date_range(-1, date(2026, 1, 13)) == (date(2025, 12, 1), date(2026, 1, 14))
assert gc.compute_stats(days, Counter())["q"] == (0, 0, 0)
print("ok")
