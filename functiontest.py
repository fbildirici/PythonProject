# Replace these variables with your actual details
jira_url = "https://your-jira-instance.atlassian.net"
project_key = "YOUR_PROJECT_KEY"
api_token = "YOUR_API_TOKEN"
user_email = "your-email@example.com"

# Fetch data from JIRA
jira_data = fetch_jira_data(jira_url, project_key, api_token, user_email)

# Check the fetched data
print(jira_data)
