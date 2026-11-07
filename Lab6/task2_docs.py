
DOCS = {
    "assessment": (
        "Assessment Policy. All coursework must be submitted through the "
        "learning portal before the stated deadline. Late submission is "
        "normally penalized by ten percent of the available marks for each "
        "calendar day after the deadline. However, students who are ill may "
        "request an extension, and an extension will be granted only when "
        "medical evidence signed by a registered doctor is provided to the "
        "course coordinator before the original deadline has passed. Work "
        "submitted more than five days late without an approved extension "
        "receives zero marks. Submissions must be a single PDF file no "
        "larger than twenty megabytes, and the file name should contain the "
        "student roll number followed by the course code. Group assignments "
        "are submitted once by the group leader, and every member should "
        "confirm the submission by email to the instructor within one "
        "working day. If the portal is unavailable near the deadline, "
        "students should take a screenshot of the error and email the "
        "coordinator immediately, because technical problems reported late "
        "are not normally accepted as a reason for an extension. "
        "Plagiarism, including the reuse of earlier work without "
        "permission, e.g. a previous semester report, is reported to the "
        "disciplinary committee. Dr. Khan chairs this committee and its "
        "decisions are final."
    ),
    "it_help": (
        "IT Help Desk Guide. A forgotten password can be reset by selecting "
        "the recovery link on the login page and entering the university "
        "email address registered with the account. A reset message is sent "
        "to the registered recovery email, and the link inside it works for "
        "thirty minutes only. Accounts are locked after five failed sign-in "
        "attempts, and a locked account cannot be reset until the lock "
        "expires after one hour, unless the help desk verifies the student "
        "identity in person with a valid student card. Never share recovery "
        "codes or reset links with anyone, including staff members, because "
        "the help desk will never ask for them. Campus WiFi is available in "
        "all academic buildings through the CampusNet network, and students "
        "sign in with their student ID and the same password used for the "
        "learning portal, while guest devices must be registered at the "
        "help desk before they can join any network on campus. Printing is "
        "available in the library at five rupees per page, and blank pages "
        "usually mean the ink level is low. Visitors may not use lab "
        "computers. The help desk is open from nine in the morning until "
        "four in the afternoon on weekdays."
    ),
    "fees": (
        "Fee Rules. The semester fee must be paid by the end of the second "
        "week of classes through the bank challan or the online payment "
        "page. A late fee of five hundred rupees is charged for each week "
        "of delay after the due date. Students receiving a scholarship are "
        "exempt from the late fee, but only if the scholarship letter has "
        "been uploaded to the finance portal before the due date. Students "
        "who miss this step are charged the full late fee until the finance "
        "office confirms the letter. Fee refunds are possible only before "
        "the start of the third week, and a refund request must include the "
        "paid challan and a written reason. After that date no refund is "
        "issued, except when the university cancels a course, in which case "
        "the fee for that course is returned within thirty days. "
        "Installment plans can be requested once per academic year, and "
        "each installment must be paid on time or the plan is cancelled "
        "automatically. For example, a student on a three-part plan who "
        "misses the second payment loses the plan. Questions are answered "
        "by the finance office on weekdays."
    ),
}

EVIDENCE = [
    {"id": "late_exception", "doc": "assessment",
     "evidence": (
         "Late submission is normally penalized by ten percent of the "
         "available marks for each calendar day after the deadline. "
         "However, students who are ill may request an extension, and an "
         "extension will be granted only when medical evidence signed by a "
         "registered doctor is provided to the course coordinator before "
         "the original deadline has passed.")},
    {"id": "portal_outage", "doc": "assessment",
     "evidence": (
         "If the portal is unavailable near the deadline, students should "
         "take a screenshot of the error and email the coordinator "
         "immediately, because technical problems reported late are not "
         "normally accepted as a reason for an extension.")},
    {"id": "lockout_exception", "doc": "it_help",
     "evidence": (
         "Accounts are locked after five failed sign-in attempts, and a "
         "locked account cannot be reset until the lock expires after one "
         "hour, unless the help desk verifies the student identity in "
         "person with a valid student card.")},
    {"id": "scholarship_exception", "doc": "fees",
     "evidence": (
         "Students receiving a scholarship are exempt from the late fee, "
         "but only if the scholarship letter has been uploaded to the "
         "finance portal before the due date.")},
    {"id": "refund_exception", "doc": "fees",
     "evidence": (
         "Fee refunds are possible only before the start of the third "
         "week, and a refund request must include the paid challan and a "
         "written reason. After that date no refund is issued, except when "
         "the university cancels a course, in which case the fee for that "
         "course is returned within thirty days.")},
]
