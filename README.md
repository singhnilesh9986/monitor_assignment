*** Content Monitoring System (Backend) ***

*** Project Overview ***
This is a Django-based REST API designed to monitor digital content for specific keywords, assign risk scores to matches, and provide a streamlined review workflow. The system was built as a technical assessment to demonstrate backend architecture, data modeling, and business logic implementation.

A core feature of this system is the Suppression Logic, which ensures that once a reviewer marks a match as "irrelevant," it remains hidden from the pending queue unless the source content is updated with a newer timestamp.

*** Key Features ***
Keyword Management: Full CRUD API to manage the list of monitored terms.

Automated Scoring Engine: Matches are scored based on placement and precision:

100: Exact match in the title.

70: Partial match in the title.

40: Match found in the body text.

Review Workflow: API endpoints to list all flags and update their status (Pending, Relevant, Irrelevant).

Intelligent Suppression: Compares ContentItem.last_updated against Flag.created_at to determine if a previously dismissed item requires a re-review.

*** Technical Decisions & Assumptions ***
Service Layer Pattern: All business logic (scoring and suppression) is encapsulated in monitoring/services.py. This approach ensures the API views remain "thin" and the core logic is maintainable and independently testable.

Mock Data Integration: As permitted by the requirements, the /scan/ endpoint utilizes a pre-defined mock dataset. This ensures the application is self-contained and immediately testable by reviewers without requiring external API keys.

Timezone Awareness: The system uses Django's parse_datetime to ensure accurate comparisons between mock data strings and database-stored datetime objects, preventing type errors during logic execution.

*** Setup & Installation ***
1. Environment Setup
# Clone the repository
git clone https://github.com/singhnilesh9986/monitor_assignment
cd monitor_assignment

# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

2. Database Initialization
python manage.py migrate

3. Running the Application
python manage.py runserver
The API will be accessible at: http://127.0.0.1:8000/api/

*** How to Test ***
Add a Keyword: Navigate to /api/keywords/ and add a word like "Django".

Trigger a Scan: Use the /api/scan/ POST endpoint to process the mock content.

Review Flags: Check /api/flags/ to see the generated scores and matches.

Verify Suppression:

Update a flag's status to irrelevant via a PATCH request to /api/flags/{id}/.

Run the scan again; the flag will remain irrelevant.

Update the last_updated date in views.py to a future date and re-scan; the flag will return to pending.
