import requests
from requests.auth import HTTPBasicAuth

def fetch_jira_data(jira_url, project_key, api_token, user_email):
    """
    Fetches data from JIRA for a given project.

    :param jira_url: URL of the JIRA instance.
    :param project_key: Key of the project in JIRA.
    :param api_token: API token for authentication.
    :param user_email: Email associated with JIRA account.
    :return: JSON response with JIRA data.
    """
    auth = HTTPBasicAuth(user_email, api_token)
    headers = {
       "Accept": "application/json"
    }

    query = {
       'jql': f'project = {project_key}'
    }

    response = requests.get(f"{jira_url}/rest/api/2/search", headers=headers, auth=auth, params=query)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data: ", response.status_code)
        return None

# Example usage
jira_data = fetch_jira_data("https://your-jira-instance.atlassian.net", "YOUR_PROJECT_KEY", "YOUR_API_TOKEN", "your-email@example.com")
