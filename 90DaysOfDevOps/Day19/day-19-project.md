#### Shell Scripting Project: Log Rotation, Backup \& Crontab





##### 1\. Log Rotation Script



log\_rotate.sh



\#!/bin/bash

set -euo pipefail



LOG\_DIR="${1:-}"



if \[ -z "$LOG\_DIR" ]; then

&nbsp;   echo "Usage: $0 <log\_directory>"

&nbsp;   exit 1

fi



if \[ ! -d "$LOG\_DIR" ]; then

&nbsp;   echo "Error: Directory does not exist."

&nbsp;   exit 1

fi



COMPRESSED\_COUNT=0

DELETED\_COUNT=0



\# Compress .log files older than 7 days

while IFS= read -r file; do

&nbsp;   gzip "$file"

&nbsp;   ((COMPRESSED\_COUNT++))

done < <(find "$LOG\_DIR" -name "\*.log" -mtime +7)



\# Delete .gz files older than 30 days

while IFS= read -r file; do

&nbsp;   rm -f "$file"

&nbsp;   ((DELETED\_COUNT++))

done < <(find "$LOG\_DIR" -name "\*.gz" -mtime +30)



echo "Compressed files: $COMPRESSED\_COUNT"

echo "Deleted files: $DELETED\_COUNT"





##### 2️⃣ Backup Script



backup.sh



\#!/bin/bash

set -euo pipefail



SOURCE="${1:-}"

DEST="${2:-}"



if \[ -z "$SOURCE" ] || \[ -z "$DEST" ]; then

&nbsp;   echo "Usage: $0 <source\_dir> <backup\_destination>"

&nbsp;   exit 1

fi



if \[ ! -d "$SOURCE" ]; then

&nbsp;   echo "Error: Source directory does not exist."

&nbsp;   exit 1

fi



mkdir -p "$DEST"



TIMESTAMP=$(date +%Y-%m-%d)

ARCHIVE="$DEST/backup-$TIMESTAMP.tar.gz"



tar -czf "$ARCHIVE" "$SOURCE"



if \[ -f "$ARCHIVE" ]; then

&nbsp;   echo "Backup created: $ARCHIVE"

&nbsp;   du -h "$ARCHIVE"

else

&nbsp;   echo "Backup failed."

&nbsp;   exit 1

fi



\# Delete backups older than 14 days

find "$DEST" -name "backup-\*.tar.gz" -mtime +14 -delete



echo "Old backups cleaned."





##### 3\. Crontab Entries





Check existing cron jobs:



crontab -l

Cron Syntax Reminder

\* \* \* \* \* command

| | | | |

| | | | └─ Day of week

| | | └─── Month

| | └───── Day of month

| └─────── Hour

└───────── Minute

Cron Entries



Run log\_rotate daily at 2 AM:



0 2 \* \* \* /path/to/log\_rotate.sh /var/log/myapp



Run backup every Sunday at 3 AM:



0 3 \* \* 0 /path/to/backup.sh /home /backup



Run health check every 5 minutes:



\*/5 \* \* \* \* /path/to/health\_check.sh





##### 4\. Combined Maintenance Script



maintenance.sh

\#!/bin/bash

set -euo pipefail



LOG\_FILE="/var/log/maintenance.log"



log\_message() {

&nbsp;   echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG\_FILE"

}



log\_message "Maintenance started."



/path/to/log\_rotate.sh /var/log/myapp >> "$LOG\_FILE" 2>\&1

log\_message "Log rotation completed."



/path/to/backup.sh /home /backup >> "$LOG\_FILE" 2>\&1

log\_message "Backup completed."



log\_message "Maintenance finished."



Cron entry for daily 1 AM:



0 1 \* \* \* /path/to/maintenance.sh







##### What I Learned



Real scripts must validate arguments



set -euo pipefail prevents silent failures



find + -mtime is powerful for log cleanup



Cron scheduling is essential for automation



Logging output is critical for maintenance scripts

