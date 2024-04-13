# 			Approved Loans Report Outage Incident Report 

# Issue Summary
From 2nd Feb 4pm EAT to 5th Feb 11am EAT, the loan application system experienced a 404 error message on the view of approved loans report. The server was unable to fetch data/process requests causing disruption to user service. No user (100%) was able to view their approved loans during the outage.

# Timeline
- 2nd Feb 4pm: Outage occurred.
- 5th Feb 8am: Team identified issue
- 5th Feb 8am: Investigation began. Investing api routes of the application for approved loans report.
- 5th Feb 10am: Cause identified and fix implemented
5th Feb 11am: Service restored to normal operations

# Root Cause and Resolution
- The outage cause was changing the API route point and pushing the code to production codbase instead of testing codebase. This was done to implement a new feature, leading to misconfiguration and the 404 error.
- The team reviewed the API route used to trigger function to fetch the report's data and figured it had been changed. This was immediately reverted to the correct route restoring the service.

# Corrective and Preventive measures
- We are working on strict deployment procedures and guidelines to prevent such changes and misconfiguration.
- We are setting up several reviews and approvals before codebases are updated.
- We are creating automatic alerting systems for immediate response to future outages.

**apologies to our users,**
loan-app Team

* Author:
- Eljones Odongo
