class ReleaseNoteTemplate:
    def __init__(self):
        self.title = "Release Note"
        self.release_date = ""
        self.summary = ""
        self.features = []
        self.bug_fixes = []
        self.acknowledgements = ""

    def add_feature(self, feature):
        self.features.append(feature)

    def add_bug_fix(self, bug_fix):
        self.bug_fixes.append(bug_fix)

    def set_release_date(self, date):
        self.release_date = date

    def set_summary(self, summary):
        self.summary = summary

    def set_acknowledgements(self, acknowledgements):
        self.acknowledgements = acknowledgements

    def __str__(self):
        return f"{self.title}\nRelease Date: {self.release_date}\n\nSummary:\n{self.summary}\n\nFeatures:\n- " + "\n- ".join(self.features) + "\n\nBug Fixes:\n- " + "\n- ".join(self.bug_fixes) + "\n\nAcknowledgements:\n{self.acknowledgements}"
