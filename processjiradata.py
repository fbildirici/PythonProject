def process_jira_data(jira_data):
    features = []
    bug_fixes = []

    for issue in jira_data.get("issues", []):
        summary = issue.get("fields", {}).get("summary", "No Summary")
        issue_type = issue.get("fields", {}).get("issuetype", {}).get("name", "")

        if issue_type.lower() == "feature":
            features.append(summary)
        elif issue_type.lower() == "bug":
            bug_fixes.append(summary)

    return features, bug_fixes

# Process the fetched JIRA data
features, bug_fixes = process_jira_data(jira_data)

# Example of how to add this data to the template
release_note = ReleaseNoteTemplate()
release_note.set_release_date("2023-12-17")  # Set a release date
release_note.set_summary("This is an example release summary.")  # Set a summary

for feature in features:
    release_note.add_feature(feature)

for bug_fix in bug_fixes:
    release_note.add_bug_fix(bug_fix)

print(release_note)
