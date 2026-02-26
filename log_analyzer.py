import re
from datetime import datetime

# -----------------------------
# Simple Security Log Analyzer
# Author: Lucia Santillan Arriaga
# -----------------------------

FAILED_LOGIN_PATTERN = r"Failed password for invalid user (\w+) from (\d+\.\d+\.\d+\.\d+)"
SUCCESS_LOGIN_PATTERN = r"Accepted password for (\w+) from (\d+\.\d+\.\d+\.\d+)"

def analyze_log(file_path):
    failed_attempts = {}
    successful_logins = []

    with open(file_path, "r") as log:
        for line in log:
            failed_match = re.search(FAILED_LOGIN_PATTERN, line)
            success_match = re.search(SUCCESS_LOGIN_PATTERN, line)

            if failed_match:
                user, ip = failed_match.groups()
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            if success_match:
                user, ip = success_match.groups()
                successful_logins.append((user, ip))

    return failed_attempts, successful_logins


def generate_report(failed_attempts, successful_logins):
    print("\nSECURITY LOG ANALYSIS REPORT")
    print("----------------------------------")

    print("\nFailed Login Attempts:")
    if failed_attempts:
        for ip, count in failed_attempts.items():
            print(f" - {ip}: {count} failed attempts")
    else:
        print(" - None detected")

    print("\nSuccessful Logins:")
    if successful_logins:
        for user, ip in successful_logins:
            print(f" - User '{user}' logged in from {ip}")
    else:
        print(" - None detected")

    print("\nReport generated:", datetime.now())


if __name__ == "__main__":
    log_file = "auth.log"  # Replace with your log file name
    failed, success = analyze_log(log_file)
    generate_report(failed, success)