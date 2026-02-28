#### Log Analyzer \& Report Generator





##### Script Overview



The script:



Validates input file



Counts ERROR and Failed entries



Identifies CRITICAL events with line numbers



Extracts top 5 most frequent ERROR messages



Generates structured summary report



Archives processed log file



##### Commands Used



grep (search patterns)



wc -l (count lines)



sort



uniq -c



head



sed (clean log lines)



mv (archive file)



date (dynamic report naming)



##### Sample Output



Console Output:



Analyzing log file: sample\_log.log

Total Errors/Failures: 42

Report generated: log\_report\_2026-02-27.txt

Log file moved to archive/



Report File:



===== Log Analysis Report =====

Date: 2026-02-27

Log File: sample\_log.log

Total Lines Processed: 1245

Total Errors/Failures: 42



----- Top 5 Error Messages -----

45 Connection timed out

32 File not found

15 Disk I/O error

9  Out of memory



----- Critical Events -----

Line 84: CRITICAL Disk space below threshold

Line 217: CRITICAL Database connection lost



##### What I Learned



Log parsing requires pattern filtering and aggregation



grep + sort + uniq is powerful for quick analytics



Automation reduces manual log inspection effort



Input validation prevents script misuse



Structured output improves readability

