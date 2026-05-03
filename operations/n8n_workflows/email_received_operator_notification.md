# n8n workflow spec — email received → operator notification

> Workflow specification only.
>
> This file does not install n8n, create an n8n JSON workflow, configure credentials, access email, send messages or authorize production use.

---

## 1. Purpose

Define the first safe n8n workflow candidate for Pantheon Next:

```text
email_received -> operator_notification
```

The workflow detects a synthetic/test email event and creates an internal operator notification. It must not execute Hermes, write Pantheon memory, ingest Knowledge, send external replies or mutate repository files.

---

## 2. Doctrine

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
n8n déclenche ou notifie sous policy.
```

n8n is a peripheral automation trigger. It is not the authority.

---

## 3. Status

```yaml
workflow_id: email_received_operator_notification
status: candidate_spec_only
runtime_created: false
n8n_installed: false
credentials_configured: false
external_messages_enabled: false
memory_write_enabled: false
knowledge_ingestion_enabled: false
hermes_execution_enabled: false
approval_level: C3_for_sandbox_test
```

---

## 4. Intended first test

Use a fake/test mailbox or label and a synthetic email.

Trigger condition:

```text
subject contains [PANTHEON-TEST]
```

Allowed result:

```text
operator sees an internal notification that a test email was detected
```

Forbidden result:

```text
external reply
Hermes execution
OpenWebUI Knowledge ingestion
Pantheon memory write
repository write
attachment processing
```

---

## 5. Workflow shape

```text
[Email Trigger]
  ↓
[Filter: test-only marker]
  ↓
[Normalize metadata]
  ↓
[Classify privacy/risk as metadata only]
  ↓
[Create internal operator notification]
  ↓
[Stop]
```

No branch may continue to external send, memory write, Knowledge ingestion or Hermes execution in this first workflow.

---

## 6. Nodes

### 6.1 Email Trigger

Purpose:

```text
Detect a new email in a test mailbox or dedicated test label.
```

Constraints:

```text
mailbox_or_label: test only
full_body_read: false preferred
attachment_download: false
mark_as_read: false unless explicitly approved
external_reply: false
```

Required configuration before real test:

```yaml
mailbox: to_define
label: to_define
trigger_mode: new_email
credential_ref: n8n_internal_only_not_in_repo
```

### 6.2 Filter

Purpose:

```text
Reject all emails except synthetic test emails.
```

Condition:

```yaml
subject_contains: "[PANTHEON-TEST]"
```

Failure path:

```text
ignore and stop
```

### 6.3 Normalize metadata

Purpose:

```text
Create a safe metadata-only event summary.
```

Allowed fields:

```yaml
email_event:
  received_at: string
  sender_domain: string
  subject_excerpt: string
  has_attachment: boolean
  attachment_count: integer
  mailbox_or_label: string
  workflow_id: email_received_operator_notification
```

Forbidden fields in logs or repo examples:

```text
full sender email
recipient email
full subject if private
full email body
raw attachment names if private
client names
project names
addresses
personal names
```

### 6.4 Classify privacy/risk

Purpose:

```text
Assign a conservative risk label from metadata only.
```

Default output:

```yaml
privacy_assessment: unknown
approval_required: C3
reason: metadata_only_test
```

Escalation rules:

```text
has_attachment = true -> potential C4 if real data
sender_domain unknown -> keep unknown
subject suggests client/project/legal/finance -> C4 if real data
```

### 6.5 Create operator notification

Purpose:

```text
Notify the operator that an email event candidate exists.
```

Allowed notification targets for first test:

```text
n8n execution log
internal-only notification channel later if approved
OpenWebUI manual review later if approved
```

Forbidden notification targets for first test:

```text
external email
client email
authority email
public webhook
SMS / WhatsApp / Telegram
GitHub issue / PR
Pantheon repository file
Pantheon memory file
```

---

## 7. Operator notification format

```yaml
operator_notification:
  workflow_id: email_received_operator_notification
  event_type: email_received
  status: candidate_detected
  received_at: string
  sender_domain: string
  subject_excerpt: string
  has_attachment: boolean
  attachment_count: integer
  privacy_assessment: unknown | internal | private | sensitive
  approval_required: C3 | C4 | C5
  allowed_next_actions:
    - ignore
    - manually_review_email
    - create_task_contract_candidate
  forbidden_next_actions:
    - auto_reply
    - auto_execute_hermes
    - auto_promote_memory
    - auto_ingest_knowledge
```

---

## 8. Future OpenWebUI handoff

Not implemented in this workflow.

Possible future handoff after separate approval:

```text
n8n notification
→ OpenWebUI action/card
→ human validates intent
→ Pantheon Task Contract candidate
→ Hermes execution only if approved
```

This requires a separate specification.

---

## 9. Future Task Contract candidate

Not implemented in this workflow.

Possible future candidate schema:

```yaml
task_contract_candidate:
  source: n8n_email_event
  workflow_id: email_received_operator_notification
  user_intent: to_be_validated_by_operator
  domain: unknown
  criticality: C3_or_C4
  input_summary: metadata_only
  attachments: not_loaded
  approvals_required:
    - operator_validation
  evidence_required: true
  execution_allowed: false
```

---

## 10. Evidence requirements

Even for the first test, the run report should capture:

```yaml
n8n_workflow_run_report:
  workflow_id: email_received_operator_notification
  workflow_version: 0.1.0
  trigger_type: email
  test_marker_required: true
  input_data_mode: metadata_only
  full_body_read: false
  attachment_downloaded: false
  external_message_sent: false
  file_created: false
  repo_modified: false
  memory_written: false
  knowledge_ingested: false
  hermes_called: false
  operator_notified: true
  limitations:
    - sandbox_spec_only
    - no_real_connector_configured_in_repo
```

---

## 11. Acceptance criteria

The first implementation may pass only if:

```text
workflow runs only on test mailbox/label
workflow requires [PANTHEON-TEST] marker
no external reply is sent
no attachment is downloaded
no full email body is stored
no secret is printed or committed
no Pantheon repo file is touched
no memory file is touched
no Knowledge ingestion is triggered
no Hermes execution is triggered
operator can manually decide next step
```

---

## 12. Rollback

If anything behaves unexpectedly:

```text
disable workflow
revoke test mailbox credential
rotate credential if exposed
stop n8n container if needed
review execution logs
record incident note if real/private data was touched
```

---

## 13. Open questions before implementation

```text
which dedicated mailbox or label should be used?
what internal-only notification target should be used first?
where should workflow run reports be reviewed?
should attachment handling be a separate workflow?
should OpenWebUI receive notifications directly or only after manual approval?
```

---

## 14. Final rule

```text
This workflow detects.
It does not decide.
It does not execute.
It does not remember.
It does not reply.
```
