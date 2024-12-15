import re

from collections import Counter


def parse_log_line(line):
    log_pattern = r'(?P<ip>[\d\.]+) - - \[(?P<date_time>[^\]]+)\] "(?P<method>[A-Z]+) (?P<url>[^\s]+) HTTP/[0-9\.]+" (?P<status_code>\d+) (?P<size>\d+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)" (?P<response_time>\d+)'

    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    else:
        return None


def get_log(path):
    logs=[]
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            log_entry = parse_log_line(line)
            if log_entry:
                logs.append(log_entry)
    return logs


def get_top_ips(logs):
    counter_ip = Counter([log.get('ip') for log in logs])
    sorted_counter_ip = dict(sorted(counter_ip.items(),key=lambda x:x[1], reverse=True))
    return dict(list(sorted_counter_ip.items())[:3])


def get_top_longest(logs):
    sorted_logs_response_time = sorted(logs, key=lambda x: x.get('response_time'), reverse=True)
    data_top_longest = [
        {
            'ip': response.get('ip'),
            'date':response.get('date_time'),
            'method':response.get('method'),
            'url':response.get('url'),
            'duration':response.get('response_time'),
        } for response in sorted_logs_response_time[:3]
    ]
    return data_top_longest


def get_total_stat(logs):
    counter_methods= Counter([log.get('method') for log in logs])
    sorted_counter_ip = dict(sorted(counter_methods.items(), key=lambda x: x[1], reverse=True))
    return sorted_counter_ip