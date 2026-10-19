import re
from pathlib import Path

bob_line = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+ .+$", re.MULTILINE)
bob_ip = re.compile(r"\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"r"(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}\b")
bob_error = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "r"(?:ERROR|WARNING|WARN) .+$",re.MULTILINE)

log_path = Path(__file__).with_name("system.txt")
log_text = log_path.read_text(encoding="utf-8")
log_lines = re.findall(bob_line, log_text)
error_warning_lines = re.findall(bob_error, log_text)
ip_lines = [line for line in log_lines if re.search(bob_ip, line)]

print("Строки уровня ERROR, WARNING или WARN:")
print("\n".join(error_warning_lines) if error_warning_lines else "Подходящих строк нет.")
print("Строки с IPv4-адресами:")
print("\n".join(ip_lines) if ip_lines else "Подходящих строк нет.")