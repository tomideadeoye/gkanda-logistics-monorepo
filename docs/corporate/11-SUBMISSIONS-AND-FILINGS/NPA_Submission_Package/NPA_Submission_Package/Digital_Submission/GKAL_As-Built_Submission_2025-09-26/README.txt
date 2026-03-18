GK & A Logistics Services Ltd – As-Built Submission (ZIP builder)
Date: 26 September 2025

This package contains 19 RTF documents (letters, statements, logs, covers, and summaries) for NPA submission, plus this README.

How to use
- The script writes GKAL_As-Built_Submission_2025-09-26.zip to the current folder.
- It also prints a base64 block you can copy to transfer elsewhere and decode.

Decode base64 elsewhere
- macOS/Linux: base64 -d GKAL_As-Built_Submission_2025-09-26_base64.txt > GKAL_As-Built_Submission_2025-09-26.zip
- Windows (PowerShell): [IO.File]::WriteAllBytes("GKAL_As-Built_Submission_2025-09-26.zip",[Convert]::FromBase64String((Get-Content GKAL_As-Built_Submission_2025-09-26_base64.txt -Raw)))
