from datetime import datetime

def extract_logs_between_timestamps(log_file_path, start_timestamp, end_timestamp):
    start_time = datetime.strptime(start_timestamp, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_timestamp, '%Y-%m-%d %H:%M:%S')
    
    extracted_logs = []
    
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Extract the timestamp from the log line
            timestamp_str = line.split(' - ')[0]
            log_time = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            
            # Check if the log time is within the specified range
            if start_time <= log_time <= end_time:
                extracted_logs.append(line.strip())
    
    return extracted_logs

# Example usage
log_file_path = 'logfile.log'
start_timestamp = '2023-04-06 10:05:00'
end_timestamp = '2023-04-06 10:15:00'

logs = extract_logs_between_timestamps(log_file_path, start_timestamp, end_timestamp)
for log in logs:
    print(log)
