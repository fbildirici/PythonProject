class ReleaseNoteTemplate:
    def __init__(self, title="Release Note"):
        self.title = title
        self.release_date = ""
        self.version = ""
        self.summary = ""
        self.features = []
        self.bug_fixes = []
        self.improvements = []
        self.known_issues = []
        self.acknowledgements = ""
        self.additional_notes = ""

    def add_feature(self, feature):
        self.features.append(feature)

    def add_bug_fix(self, bug_fix):
        self.bug_fixes.append(bug_fix)

    def add_improvement(self, improvement):
        self.improvements.append(improvement)

    def add_known_issue(self, issue):
        self.known_issues.append(issue)

    def set_release_date(self, date):
        self.release_date = date

    def set_version(self, version):
        self.version = version

    def set_summary(self, summary):
        self.summary = summary

    def set_acknowledgements(self, acknowledgements):
        self.acknowledgements = acknowledgements

    def set_additional_notes(self, notes):
        self.additional_notes = notes

    def __str__(self):
        features_str = "\n- ".join(self.features) if self.features else "None"
        bug_fixes_str = "\n- ".join(self.bug_fixes) if self.bug_fixes else "None"
        improvements_str = "\n- ".join(self.improvements) if self.improvements else "None"
        known_issues_str = "\n- ".join(self.known_issues) if self.known_issues else "None"

        return (
            f"{self.title}\n"
            f"Version: {self.version}\n"
            f"Release Date: {self.release_date}\n\n"
            f"Summary:\n{self.summary}\n\n"
            f"New Features:\n- {features_str}\n\n"
            f"Bug Fixes:\n- {bug_fixes_str}\n\n"
            f"Improvements:\n- {improvements_str}\n\n"
            f"Known Issues:\n- {known_issues_str}\n\n"
            f"Acknowledgements:\n{self.acknowledgements}\n\n"
            f"Additional Notes:\n{self.additional_notes}"
        )
