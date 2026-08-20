# lead-enquiry-triage-demo

Runtime dependencies for `lead_enquiry_triage_demo.robot`, a local rpaframework demo of a
"lead enquiry triage" automation (Trigger -> Agentic "Interpret the enquiry" -> API
"Create the Salesforce lead" -> Decision -> confirm/request-info -> Human assign -> API
notify rep).

The `.robot` file downloads these at runtime so it can be shared as a single file:

- `generate_gmail_mirror.py` - renders a static, Gmail-styled "Sent" results page at the
  end of a run and opens it in the browser.
- `assets/lead_email_complete.png` / `assets/lead_email_incomplete.png` - synthetic sample
  "inbound enquiry email" screenshots (all data is fictitious - `.example` domains, no
  real company or person) used as input to a real Gemini Vision extraction call.

Everything here is dummy/demo content - nothing sensitive.
